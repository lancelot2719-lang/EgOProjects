# Commit-only при завершении работы Windows (GPO shutdown script, контекст SYSTEM)
# Push НЕ делаем: сеть при выключении может быть недоступна — его догонит SecondBrainAutoSave.
$Git  = 'D:\AI_Project\Git\cmd\git.exe'
$Repo = 'D:\AI_Project'
$Log  = 'D:\AI_Project\tech\auto-commit-shutdown.log'

try {
    $stamp = Get-Date -Format 'yyyy-MM-dd HH:mm:ss'
    Add-Content -LiteralPath $Log -Value "$stamp  START" -Encoding utf8

    Set-Location -LiteralPath $Repo
    $env:GIT_TERMINAL_PROMPT = '0'

    $changes = & $Git -c safe.directory=$Repo status --porcelain 2>&1
    if (-not $changes -or $changes -match 'fatal|error') {
        Add-Content -LiteralPath $Log -Value "$stamp  NO_CHANGES or git error: $($changes -join ' ')" -Encoding utf8
        exit 0
    }

    & $Git -c safe.directory=$Repo add -A 2>&1 | Out-Null
    if ($LASTEXITCODE -ne 0) {
        Add-Content -LiteralPath $Log -Value "$stamp  ADD FAILED rc=$LASTEXITCODE" -Encoding utf8
        exit 1
    }

    $date = Get-Date -Format 'yyyy-MM-dd HH:mm'
    & $Git -c safe.directory=$Repo commit -m "Auto-save (shutdown): $date" 2>&1 | Out-Null
    if ($LASTEXITCODE -ne 0) {
        Add-Content -LiteralPath $Log -Value "$stamp  COMMIT FAILED rc=$LASTEXITCODE" -Encoding utf8
        exit 1
    }
    Add-Content -LiteralPath $Log -Value "$stamp  COMMIT ok" -Encoding utf8
} catch {
    Add-Content -LiteralPath $Log -Value "$stamp  EXCEPTION: $($_.Exception.Message)" -Encoding utf8
    exit 2
}
