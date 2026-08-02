# Whisper Flow — запуск
# Нажми RIGHT ALT и говори — текст появится в активном окне
# Отпусти RIGHT ALT — запись остановится

$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path
$mainScript = Join-Path $scriptPath "whisper_flow.py"

Write-Host "Whisper Flow — локальная голосовая диктовка" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""

# Проверка Python
try {
    $pyVersion = python --version
    Write-Host "[OK] $pyVersion" -ForegroundColor Green
} catch {
    Write-Host "[FAIL] Python не найден. Установи Python 3.10+ с python.org" -ForegroundColor Red
    Read-Host "Нажми Enter для выхода"
    exit 1
}

# Проверка зависимостей
try {
    python -c "import faster_whisper, keyboard, sounddevice, silero_vad" 2>$null
    Write-Host "[OK] Все зависимости установлены" -ForegroundColor Green
} catch {
    Write-Host "[...] Устанавливаю зависимости..." -ForegroundColor Yellow
    pip install -r (Join-Path $scriptPath "requirements.txt") 2>&1
}

Write-Host ""
Write-Host "Нажми RIGHT ALT и говори в микрофон" -ForegroundColor Yellow
Write-Host "Текст появится там, где стоит курсор." -ForegroundColor Yellow
Write-Host "Для выхода: закрой окно или нажми Ctrl+C" -ForegroundColor Yellow
Write-Host ""

try {
    python $mainScript
} catch {
    Write-Host "Ошибка: $_" -ForegroundColor Red
    Read-Host "Нажми Enter для выхода"
}
