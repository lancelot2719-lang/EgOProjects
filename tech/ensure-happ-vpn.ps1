param([string]$TargetApp = "")

$HappGui = "D:\Happ\Happ.exe"
$LogFile = "$env:TEMP\happ-vpn-launch.log"

function Write-Log { param([string]$Msg)
    $time = Get-Date -Format "HH:mm:ss"
    "$time $Msg" | Out-File -LiteralPath $LogFile -Append
}

Write-Log "=== Check Happ VPN ==="

# 1) Start Happ.exe if not running (activates subscription)
$happProcess = Get-Process -Name "Happ" -ErrorAction SilentlyContinue
if (-not $happProcess) {
    Write-Log "Happ.exe not running. Starting..."
    Start-Process -FilePath $HappGui
    Start-Sleep -Seconds 5
    Write-Log "Happ.exe started."
} else {
    Write-Log "Happ.exe already running (PID: $($happProcess.Id))."
}

# 2) Wait for TUN interface or SOCKS5 port
$connected = $false
for ($i = 0; $i -lt 20; $i++) {
    $tun = Get-NetAdapter -Name "*happ*" -ErrorAction SilentlyContinue
    $port = netstat -ano 2>&1 | Select-String "127.0.0.1:10808" -SimpleMatch
    if ($tun -or $port) {
        if ($tun) { Write-Log "VPN OK: TUN $($tun.Name)" }
        if ($port) { Write-Log "VPN OK: port 10808 open" }
        $connected = $true
        break
    }
    Write-Log "Waiting for VPN... ($($i+1)/20)"
    Start-Sleep -Seconds 2
}

if (-not $connected) {
    Write-Log "WARNING: VPN not connected after 40s. Continuing anyway."
}

# 3) Launch target app if specified
if ($TargetApp) {
    Write-Log "Launching: $TargetApp"
    Start-Process -FilePath $TargetApp
}

Write-Log "=== Done ==="
