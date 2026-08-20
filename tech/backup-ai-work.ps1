# Регулярный бэкап C:\AI\Projects -> HDD (E:\Backup\AI_Project)
#
# Работает НА НОВОЙ разметке дисков после переустановки Windows и переноса
# работы на новый SSD (см. tech/pc-build-plan.md, раздел "Разметка дисков").
# Дополняет (не заменяет) git+GitHub: сюда попадает и то, что исключено из
# git через .gitignore (например крупные файлы Книги/Аудиокниги > 100MB).
# Модели (ollama/hf-cache) сознательно НЕ бэкапятся - они перекачиваются.
#
# Регистрация в Task Scheduler (запустить один раз от обычного пользователя):
#   schtasks /Create /TN "AI_Project HDD Backup" ^
#     /TR "powershell.exe -NoProfile -ExecutionPolicy Bypass -File \"C:\AI\Projects\tech\backup-ai-work.ps1\"" ^
#     /SC DAILY /ST 23:30 /RL LIMITED /F

$Source = 'C:\AI\Projects'
$Dest   = 'E:\Backup\AI_Project'
$Log    = Join-Path $Source 'tech\backup-ai-work.log'
$MaxLog = 512KB

# Регенерируемое/мусор - не копируем (совпадает с исходной оценкой AI_Project и .gitignore)
$ExcludeNames = @('ollama', 'hf-cache', 'temp', '__pycache__', 'venv', '.git')

function Write-Log {
    param([string]$m)
    $line = "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')  $m"
    Add-Content -LiteralPath $Log -Value $line -Encoding utf8
    Write-Host $line
}

if (!(Test-Path $Source)) {
    Write-Log "ABORT: source $Source not found (работа ещё не перенесена на новый SSD?)"
    exit 1
}
$destParent = Split-Path $Dest -Parent
if (!(Test-Path $destParent)) {
    Write-Log "ABORT: HDD backup target parent $destParent not reachable"
    exit 1
}
New-Item -ItemType Directory -Path $Dest -Force | Out-Null

$xd = $ExcludeNames | ForEach-Object { Join-Path $Source $_ }
$null = robocopy $Source $Dest /MIR /XD $xd /R:2 /W:5 /NFL /NDL /NP /NJH /NJS 2>&1
$rc = $LASTEXITCODE

# Коды robocopy 0-7 = успех (см. robocopy /?), 8+ = ошибка
if ($rc -ge 8) {
    Write-Log "ROBOCOPY FAILED rc=$rc"
    exit 1
}

$size = (Get-ChildItem $Dest -Recurse -Force -ErrorAction SilentlyContinue | Measure-Object Length -Sum).Sum
Write-Log "OK rc=$rc  size=$([math]::Round($size/1GB,2)) GB"

if ((Test-Path $Log) -and (Get-Item -LiteralPath $Log).Length -gt $MaxLog) {
    Get-Content -LiteralPath $Log -Tail 300 | Set-Content -LiteralPath $Log -Encoding utf8
}
