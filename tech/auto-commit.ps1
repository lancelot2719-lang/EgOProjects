# Auto-save: коммит и пуш D:\AI_Project по расписанию
$Repo = 'D:\AI_Project'
$Log  = 'D:\AI_Project\tech\auto-commit.log'
$MaxLog = 512KB

function Write-Log($msg) {
    $line = "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')  $msg"
    Add-Content -LiteralPath $Log -Value $line -Encoding utf8
    Write-Host $line
}

Set-Location -LiteralPath $Repo
git fetch origin --quiet 2>$null

$changes = git status --porcelain 2>$null
if (-not $changes) {
    Write-Log 'NO_CHANGES - commit skipped'
    exit 0
}

$date = Get-Date -Format 'yyyy-MM-dd HH:mm'
git add -A 2>>$Log
if ($LASTEXITCODE -ne 0) { Write-Log "ADD FAILED rc=$LASTEXITCODE"; exit 1 }

git commit -m "Auto-save: $date" 2>>$Log
if ($LASTEXITCODE -ne 0) { Write-Log "COMMIT FAILED rc=$LASTEXITCODE"; exit 1 }
Write-Log "COMMIT ok ($(($changes | Measure-Object -Line).Lines) files)"

git push origin main 2>>$Log
if ($LASTEXITCODE -ne 0) {
    Write-Log "PUSH FAILED rc=$LASTEXITCODE (will retry next run)"
    exit 2
}
Write-Log 'PUSH ok'

if ((Get-Item -LiteralPath $Log).Length -gt $MaxLog) {
    Get-Content -LiteralPath $Log -Tail 300 | Set-Content -LiteralPath $Log -Encoding utf8
}
