Write-Host "=== Claude Code + VPN Launcher ===" -ForegroundColor Cyan
Write-Host "[1/3] Checking Aitek VPN..." -ForegroundColor Yellow

$log = "$env:TEMP\claude-vpn.log"
& "D:\AI_Project\tech\start-aitek-vpn.ps1" *>> $log

$portOpen = $false
for ($i = 0; $i -lt 10; $i++) {
    $listening = netstat -ano 2>&1 | Select-String "127.0.0.1:10808" -SimpleMatch | Select-String "LISTENING" -SimpleMatch
    if ($listening) { $portOpen = $true; break }
    Write-Host "   Waiting for Xray... ($($i+1)/10)" -ForegroundColor Gray
    Start-Sleep 2
}

if (-not $portOpen) {
    Write-Host "[!] Xray not started. Check log: $log" -ForegroundColor Red
} else {
    Write-Host "[2/3] VPN active (SOCKS5 :10808)" -ForegroundColor Green
}

Write-Host "[3/3] Starting Claude Code..." -ForegroundColor Yellow
Start-Process -FilePath "cmd.exe" -ArgumentList "/c cd /d D:\AI_Project && claude.cmd"

Write-Host "=== Done ===" -ForegroundColor Cyan
Start-Sleep 2
