# Unlimited-OCR

**Репозиторий:** https://github.com/baidu/Unlimited-OCR
**Модель HF:** https://huggingface.co/baidu/Unlimited-OCR
**Статья:** https://arxiv.org/abs/2606.23050
**Демо:** https://huggingface.co/spaces/baidu/Unlimited-OCR

Open-source модель от Baidu для OCR длинных документов (книги, PDF до десятков страниц) за один проход. Построена на архитектуре R-SWA (Recurrent Sliding Window Attention).

## Возможности

- Обработка целых книг, PDF, научных статей одним проходом без разбиения на страницы
- Работа с PDF, изображениями, сканами
- Мультиязычность
- Сохранение структуры документа
- Не требует разрезать PDF на части

## Требования (официальные)

- **GPU:** NVIDIA с CUDA 12.9+
- **VRAM:** ~16 GB (модель 7B параметров)
- **Python:** 3.12.3 (рекомендуется)
- **ОЗУ:** 32+ GB
- **Диск:** ~7 GB для модели

## Установка (локальная)

Репозиторий уже склонирован в `D:\AI_Project\Unlimited-OCR`.

Зависимости установлены:
```
pip install torch torchvision transformers pymupdf pillow matplotlib einops addict easydict psutil
```

## Использование

### 1. Конвертация PDF в изображения

```python
import os, tempfile, fitz

def pdf_to_images(pdf_path, dpi=300):
    doc = fitz.open(pdf_path)
    tmp_dir = tempfile.mkdtemp(prefix='pdf_ocr_')
    mat = fitz.Matrix(dpi / 72, dpi / 72)
    paths = []
    for i, page in enumerate(doc):
        out = os.path.join(tmp_dir, f'page_{i+1:04d}.png')
        page.get_pixmap(matrix=mat).save(out)
        paths.append(out)
    doc.close()
    return paths
```

### 2. OCR одного PDF (HuggingFace Transformers, требуется GPU)

```python
import torch
from transformers import AutoModel, AutoTokenizer

model_name = 'baidu/Unlimited-OCR'

tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
model = AutoModel.from_pretrained(
    model_name,
    trust_remote_code=True,
    use_safetensors=True,
    torch_dtype=torch.bfloat16,
)
model = model.eval().cuda()

model.infer_multi(
    tokenizer,
    prompt='<image>Multi page parsing.',
    image_files=pdf_to_images('your_doc.pdf', dpi=300),
    output_path='./ocr_output',
    image_size=1024,
    max_length=32768,
    no_repeat_ngram_size=35,
    ngram_window=1024,
    save_results=True,
)
```

### 3. Пакетная обработка (SGLang, рекомендуется)

```bash
python infer.py \
    --pdf ./document.pdf \
    --output_dir ./outputs \
    --concurrency 8 \
    --image_mode base
```

Параметры:
- `--image_mode gundam` — для одного изображения (base_size=1024, image_size=640, crop_mode=True)
- `--image_mode base` — для PDF/многостраничных документов (base_size=1024, image_size=1024, crop_mode=False)

## Состояние на текущей системе

| Компонент | Статус |
|-----------|--------|
| Репозиторий | ✅ Склонирован |
| Зависимости | ✅ Установлены |
| Конвертация PDF→PNG | ✅ Работает |
| NVIDIA GPU / CUDA | ❌ Отсутствует |
| Загрузка модели | ❌ Недостаточно места на диске (~4.4 GB из ~7 GB) |
| Запуск на CPU | ❌ Модель 7B не запускается на CPU */

## Варианты запуска без GPU

1. **Google Colab** — бесплатный GPU (T4, 16GB VRAM):
   - https://colab.research.google.com/github/baidu/Unlimited-OCR
   - Или вручную: https://huggingface.co/spaces/baidu/Unlimited-OCR

2. **HuggingFace Spaces** — демо: https://huggingface.co/spaces/baidu/Unlimited-OCR

3. **Облачные GPU**: RunPod, Vast.ai, Lambda Labs, Paperspace

4. **vLLM Docker** (если появится GPU):
   ```bash
   docker pull vllm/vllm-openai:unlimited-ocr
   ```

## Структура проекта

```
D:\AI_Project\Unlimited-OCR\
├── assets/              # Картинки для README
├── wheel/               # SGLang wheel
├── infer.py             # Пакетный инференс через SGLang
├── README.md            # Документация
├── Unlimited-OCR.pdf    # Научная статья (14 стр.)
├── CONTRIBUTING.md
└── LICENSE
```

## Ссылки

- https://github.com/baidu/Unlimited-OCR
- https://huggingface.co/baidu/Unlimited-OCR
- https://arxiv.org/abs/2606.23050
- https://recipes.vllm.ai/baidu/Unlimited-OCR
- https://cloud.baidu.com/doc/OCR/s/fmr1p39gb (Baidu Cloud API)
