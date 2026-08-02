# Варианты транскрибации

> Сравнение бесплатных решений для текущей системы (RX 6700 XT 12GB, 16GB RAM)

## 1. Whisper (оригинальный OpenAI) — уже есть
- **Модель на диске:** `D:\AI_Project\ollama\xkeyC\whisper-large-v3-turbo-gguf\model_q4_k.gguf` (453 MB)
- **Как использовать:** `pip install openai-whisper`, Python API
- **Скорость:** средняя, работает через PyTorch
- **Русский:** ✅ отлично (large-v3)
- **VRAM:** ~6 GB для turbo, ~10 GB для large-v3
- **Минус:** требует ffmpeg + PyTorch (тяжёлый)

## 2. Whisper.cpp (рекомендуется) — быстрее в 2-4x
- **Репозиторий:** github.com/ggml-org/whisper.cpp
- **Язык:** C/C++, без зависимостей
- **GPU:** поддержка AMD ROCm (твоя RX 6700 XT — gfx1031)
- **Квантование:** int8, q5, q4 — модель меньше, быстрее
- **VAD (Silero):** встроенный голосовой детектор
- **Как установить:**
  ```
  git clone https://github.com/ggml-org/whisper.cpp.git
  cd whisper.cpp
  cmake -B build -DGGML_HIP=1  # для AMD ROCm
  cmake --build build -j --config Release
  ```
- **Модели:** те же, в ggml-формате (~75 MB tiny — ~3 GB large-v3)
- **Бенчмарк:** на RX 6700 XT — large-v3 ~2-3x быстрее оригинального Whisper

## 3. Faster-Whisper (CTranslate2) — быстрее оригинала
- **Репозиторий:** github.com/SYSTRAN/faster-whisper
- **Суть:** тот же Whisper, но через CTranslate2 (оптимизированный инференс)
- **Скорость:** до 4x быстрее оригинала
- **VRAM:** ~4 GB для large-v3
- **Минус:** нет нативной поддержки AMD ROCm (только CUDA)
- **На RX 6700 XT:** будет работать через CPU, смысла нет

## 4. SenseVoice (Alibaba) — конкурент Whisper
- **Репозиторий:** github.com/modelscope/SenseVoice
- **Особенность:** многоязычный, очень быстрый
- **Русский:** ✅ хорошо
- **Минус:** меньшая экосистема, нет VAD

## Итог для текущей системы

| Решение | Скорость | Русский | ROCm | Память | Сложность |
|---------|----------|---------|------|--------|-----------|
| Whisper (оригинал) | ⭐⭐ | ⭐⭐⭐⭐⭐ | ❌ | 6-10 GB VRAM | Низкая |
| **Whisper.cpp** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ✅ | 2-4 GB VRAM | Средняя |
| Faster-Whisper | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ❌ | 4 GB VRAM | Средняя |
| SenseVoice | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ❌ | 2 GB VRAM | Средняя |

**Вывод:** Whisper.cpp — лучший выбор. Собирается с флагом `-DGGML_HIP=1` для работы через ROCm на RX 6700 XT. Намного быстрее оригинала, меньше жрёт памяти, есть Silero-VAD.

## Для будущего rig (RX 580 x4-6)
Whisper.cpp поддерживает Vulkan — можно распределить инференс по всем картам.
