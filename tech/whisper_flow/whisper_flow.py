#!/usr/bin/env python3
"""
Whisper Flow — локальная голосовая диктовка для Windows.
Аналог Wispr Flow (https://wisprflow.ai/).

Горячая клавиша: Right Alt (правый Alt).
Нажми и говори — текст появится в активном окне.
Отпусти — запись остановится.

Зависимости: pip install faster-whisper keyboard sounddevice silero-vad pystray pyperclip soundfile Pillow
"""

import argparse
import json
import logging
import os
import queue
import sys
import threading
import time
import ctypes
import ctypes.wintypes as wintypes
from collections import deque
from dataclasses import dataclass, asdict
from pathlib import Path

logging.getLogger().setLevel(logging.WARNING)
log = logging.getLogger("whisper_flow")
log.setLevel(logging.DEBUG)
_sh = logging.StreamHandler()
_sh.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))
log.addHandler(_sh)

SAMPLE_RATE = 16000
CHUNK_MS = 32
CHUNK_SIZE = int(SAMPLE_RATE * CHUNK_MS / 1000)  # 512 samples (silero VAD minimum)
CONFIG_PATH = Path(__file__).parent / "config.json"


# ═══════════════════════════════════════════════════════════════════════
#  Configuration
# ═══════════════════════════════════════════════════════════════════════
@dataclass
class Config:
    hotkey: str = "right alt"
    model: str = "medium"
    language: str = "ru"
    vad_threshold: float = 0.5
    min_silence_ms: int = 400
    compute_type: str = "int8"
    device: str = "cpu"
    beam_size: int = 1
    insert_space: bool = True

    @classmethod
    def load(cls) -> "Config":
        if CONFIG_PATH.exists():
            try:
                data = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
                valid = {k: v for k, v in data.items() if k in cls.__dataclass_fields__}
                return cls(**valid)
            except Exception as e:
                log.warning("config error: %s", e)
        return cls()

    def save(self):
        CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
        CONFIG_PATH.write_text(
            json.dumps(asdict(self), indent=2, ensure_ascii=False), encoding="utf-8"
        )


# ═══════════════════════════════════════════════════════════════════════
#  Text Inserter — clipboard + Ctrl+V
# ═══════════════════════════════════════════════════════════════════════
class TextInserter:
    _lock = threading.Lock()

    @classmethod
    def insert(cls, text: str):
        if not text:
            return
        with cls._lock:
            import pyperclip
            import keyboard as kb
            import time as _time
            saved = pyperclip.paste()
            pyperclip.copy(text)
            _time.sleep(0.04)
            kb.send("ctrl+v")
            _time.sleep(0.04)
            try:
                pyperclip.copy(saved)
            except Exception:
                pass


# ═══════════════════════════════════════════════════════════════════════
#  Audio Capture
# ═══════════════════════════════════════════════════════════════════════
class AudioCapture:
    def __init__(self):
        self.stream = None
        self.recording = False
        self.queue: queue.Queue = queue.Queue()
        self._lock = threading.Lock()

    def _callback(self, indata, frames, _time_info, _status):
        if self.recording:
            self.queue.put(indata.copy())

    def start(self):
        import sounddevice as sd
        with self._lock:
            if self.stream is not None:
                return
            self.recording = True
            self.stream = sd.InputStream(
                samplerate=SAMPLE_RATE, channels=1, blocksize=CHUNK_SIZE,
                callback=self._callback, dtype="float32",
            )
            self.stream.start()

    def stop(self):
        with self._lock:
            self.recording = False
            if self.stream is not None:
                self.stream.stop()
                self.stream.close()
                self.stream = None
            # drain queue
            while not self.queue.empty():
                try:
                    self.queue.get_nowait()
                except queue.Empty:
                    break

    def drain(self) -> list:
        chunks = []
        while not self.queue.empty():
            try:
                chunks.append(self.queue.get_nowait())
            except queue.Empty:
                break
        return chunks


# ═══════════════════════════════════════════════════════════════════════
#  VAD (Silero)
# ═══════════════════════════════════════════════════════════════════════
class VAD:
    """Voice Activity Detection — wraps Silero VAD, no internal buffering."""

    def __init__(self, config: Config):
        self.config = config
        self._model = None
        self._triggered = False
        self._silence_chunks = 0
        self._max_silence = config.min_silence_ms // CHUNK_MS

    def _lazy_init(self):
        if self._model is not None:
            return
        from silero_vad import load_silero_vad
        log.info("loading Silero VAD ...")
        self._model = load_silero_vad()

    def reset(self):
        self._triggered = False
        self._silence_chunks = 0

    def process(self, audio_chunk) -> dict:
        """Process audio (buffered to 512-sample blocks). Returns {} / {'start'} / {'end'}."""
        self._lazy_init()
        import torch
        import numpy as np

        result = {}
        buf = audio_chunk.flatten()
        idx = 0
        while idx < len(buf):
            block = buf[idx:idx + 512]
            idx += 512
            if len(block) < 512:
                block = np.pad(block, (0, 512 - len(block)))
            prob = self._model(torch.from_numpy(block).float(), SAMPLE_RATE).item()

            if prob >= self.config.vad_threshold:
                if not self._triggered:
                    self._triggered = True
                    result["start"] = True
                self._silence_chunks = 0
            else:
                if self._triggered:
                    self._silence_chunks += 1
                    if self._silence_chunks >= self._max_silence:
                        self._triggered = False
                        result["end"] = True
                        self._silence_chunks = 0
        return result


# ═══════════════════════════════════════════════════════════════════════
#  Transcriber — faster-whisper
# ═══════════════════════════════════════════════════════════════════════
class Transcriber:
    def __init__(self, config: Config):
        self.config = config
        self.model = None
        self._lock = threading.Lock()

    def _lazy_init(self):
        if self.model is not None:
            return
        from faster_whisper import WhisperModel
        log.info("loading faster-whisper '%s' on %s (%s) ...",
                 self.config.model, self.config.device, self.config.compute_type)
        self.model = WhisperModel(
            self.config.model,
            device=self.config.device,
            compute_type=self.config.compute_type,
            download_root=str(Path.home() / ".cache" / "faster_whisper"),
            cpu_threads=os.cpu_count() or 4,
            num_workers=1,
        )

    def transcribe(self, audio_chunks) -> str:
        if not audio_chunks:
            return ""
        self._lazy_init()
        import numpy as np
        samples = np.concatenate(audio_chunks).flatten().astype(np.float32)
        if len(samples) < SAMPLE_RATE * 0.1:  # < 100ms
            return ""
        with self._lock:
            segments, _info = self.model.transcribe(
                samples, language=self.config.language,
                beam_size=self.config.beam_size,
                vad_filter=False, condition_on_previous_text=True,
            )
            return " ".join(s.text for s in segments).strip()


# ═══════════════════════════════════════════════════════════════════════
#  System Tray
# ═══════════════════════════════════════════════════════════════════════
class TrayUI:
    def __init__(self, on_quit):
        self.icon = None
        self._on_quit = on_quit
        self._color = "#888888"
        self._text = "Whisper Flow"

    def _make_icon(self, color):
        from PIL import Image, ImageDraw
        img = Image.new("RGBA", (16, 16), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        draw.ellipse([2, 2, 13, 13], fill=color)
        return img

    @property
    def status(self):
        return "idle" if self._color == "#888888" else \
               "listening" if self._color == "#22c55e" else \
               "transcribing" if self._color == "#f59e0b" else "inserting"

    @status.setter
    def status(self, val):
        m = {"idle": "#888888", "listening": "#22c55e",
             "transcribing": "#f59e0b", "inserting": "#3b82f6"}
        self._color = m.get(val, "#888888")
        if self.icon:
            self.icon.icon = self._make_icon(self._color)

    def run(self):
        import pystray
        self.icon = pystray.Icon(
            "whisper_flow",
            self._make_icon(self._color),
            "Whisper Flow",
            pystray.Menu(
                pystray.MenuItem("Whisper Flow", None, enabled=False),
                pystray.Menu.SEPARATOR,
                pystray.MenuItem("Quit", lambda: self._on_quit()),
            ),
        )
        self.icon.run()


# ═══════════════════════════════════════════════════════════════════════
#  Application Core
# ═══════════════════════════════════════════════════════════════════════
class WhisperFlowApp:
    def __init__(self, config: Config):
        self.config = config
        self.audio = AudioCapture()
        self.vad = VAD(config)
        self.stt = Transcriber(config)
        self.tray = TrayUI(on_quit=self.shutdown)
        self._running = False
        self._recording = False

    # ── public ──

    def run(self):
        self._running = True
        log.info("Whisper Flow ready")
        log.info("  Hotkey: %s  |  Model: %s  |  Language: %s",
                 self.config.hotkey, self.config.model, self.config.language)
        log.info("  Press %s and speak — text appears in the active window.", self.config.hotkey)
        log.info("  Release to stop.")

        threading.Thread(target=self.tray.run, daemon=True).start()
        self._register_hotkey()

        try:
            while self._running:
                time.sleep(0.2)
        except KeyboardInterrupt:
            pass
        finally:
            self.shutdown()

    def shutdown(self):
        self._running = False
        self._recording = False
        self.audio.stop()
        try:
            import keyboard
            keyboard.unhook_all()
        except Exception:
            pass
        if self.tray.icon:
            self.tray.icon.stop()
        os._exit(0)

    # ── hotkey ──

    def _register_hotkey(self):
        import keyboard
        try:
            keyboard.on_press_key("right alt", self._on_press, suppress=False)
            keyboard.on_release_key("right alt", self._on_release, suppress=False)
        except Exception as e:
            log.error("hotkey registration failed: %s", e)
            log.error("Try running as Administrator.")

    def _on_press(self, _e):
        if not self._recording:
            self._recording = True
            threading.Thread(target=self._start_recording, daemon=True).start()

    def _on_release(self, _e):
        if self._recording:
            self._recording = False

    # ── recording ──

    def _start_recording(self):
        self.vad.reset()
        self.audio.start()
        self.tray.status = "listening"

        log.debug("recording started")
        speech_buffer = deque()
        in_speech = False
        last_transcribe = time.time()

        while self._recording:
            chunks = self.audio.drain()
            if not chunks:
                time.sleep(0.01)
                continue

            for chunk in chunks:
                if not self._recording:
                    break

                result = self.vad.process(chunk)

                # Handle VAD events first
                if result.get("start"):
                    in_speech = True
                    log.debug("speech start")

                if result.get("end"):
                    log.debug("speech end")
                    if speech_buffer:
                        text = self.stt.transcribe(list(speech_buffer))
                        speech_buffer.clear()
                        last_transcribe = time.time()
                        if text:
                            log.debug("-> %s", text[:80])
                            self._insert(text)
                    in_speech = False

                # Accumulate audio during speech (after processing VAD)
                if in_speech:
                    speech_buffer.append(chunk)

            # Force-transcribe every ~3s of continuous speech for real-time feel
            if in_speech and speech_buffer and time.time() - last_transcribe > 3.0:
                text = self.stt.transcribe(list(speech_buffer))
                speech_buffer.clear()
                last_transcribe = time.time()
                if text:
                    log.debug("-> (auto) %s", text[:80])
                    self._insert(text)

        # Finish: transcribe remaining audio after releasing hotkey
        remaining = list(speech_buffer)
        while not self._recording:
            extra = self.audio.drain()
            if not extra:
                break
            remaining.extend(c for c in extra)

        if remaining:
            text = self.stt.transcribe(remaining)
            if text:
                log.debug("→ (final) %s", text[:80])
                self._insert(text, trailing_space=False)

        self.audio.stop()
        self.tray.status = "idle"
        log.debug("recording stopped")

    def _insert(self, text: str, trailing_space: bool = True):
        if not text:
            return
        self.tray.status = "inserting"
        try:
            final = text + (" " if trailing_space else "")
            TextInserter.insert(final)
        except Exception as e:
            log.error("insert error: %s", e)
        self.tray.status = "listening"


# ═══════════════════════════════════════════════════════════════════════
#  Entry
# ═══════════════════════════════════════════════════════════════════════
def main():
    parser = argparse.ArgumentParser(description="Whisper Flow — local voice dictation")
    parser.add_argument("--configure", action="store_true", help="Generate config and exit")
    args = parser.parse_args()

    config = Config.load()

    if args.configure:
        config.save()
        print(f"Config saved to {CONFIG_PATH}")
        return

    app = WhisperFlowApp(config)
    app.run()


if __name__ == "__main__":
    main()
