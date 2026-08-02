param([string]$TargetApp = "")

$XrayPath = "D:\Happ\core\xray.exe"
$ConfigPath = "D:\AI_Project\tech\aitek-xray-config.json"
$LogFile = "$env:TEMP\aitek-vpn.log"

function Write-Log { param([string]$Msg)
    $time = Get-Date -Format "HH:mm:ss"
    "$time $Msg" | Out-File -LiteralPath $LogFile -Append
}

Write-Log "=== Aitek VPN launcher ==="

# 1) Start Xray SOCKS5 proxy
$portCheck = netstat -ano 2>&1 | Select-String "127.0.0.1:10808" -SimpleMatch | Select-String "LISTENING" -SimpleMatch
if ($portCheck) {
    Write-Log "Xray already running (port 10808 LISTENING)."
} else {
    Write-Log "Starting Xray..."
    $proc = Start-Process -FilePath $XrayPath -ArgumentList "run","-c","`"$ConfigPath`"" -WindowStyle Hidden -PassThru
    Write-Log "Xray started (PID: $($proc.Id))."

    $connected = $false
    for ($i = 0; $i -lt 15; $i++) {
        Start-Sleep -Seconds 2
        if (netstat -ano 2>&1 | Select-String "127.0.0.1:10808" -SimpleMatch) {
            $connected = $true
            break
        }
        Write-Log "Waiting Xray... ($($i+1)/15)"
    }
    if (-not $connected) {
        Write-Log "WARNING: Xray failed to start."
    } else {
        Write-Log "Xray OK (port 10808 open)."
    }
}

# 2) Start TUN service for system-wide routing (if installed)
$tunService = Get-Service -Name "AitekTun" -ErrorAction SilentlyContinue
if ($tunService -and $tunService.Status -ne 'Running') {
    $tunCheck = Get-NetAdapter -Name "aitek-tun" -ErrorAction SilentlyContinue
    if (-not $tunCheck) {
        Write-Log "Starting TUN service (may prompt UAC)..."
        try {
            Start-Process -FilePath "powershell.exe" -ArgumentList "-NoProfile -Command Start-Service -Name AitekTun" -Verb RunAs -Wait -ErrorAction Stop
            Start-Sleep -Seconds 5
            Write-Log "TUN service started."
        } catch {
            Write-Log "WARNING: Could not start TUN service (access denied). System-wide routing not active."
            Write-Log "Fallback: HTTPS_PROXY will be set for compatible apps."
            # Set proxy env vars as fallback
            [Environment]::SetEnvironmentVariable("HTTPS_PROXY", "socks5://127.0.0.1:10808", "User")
            [Environment]::SetEnvironmentVariable("HTTP_PROXY", "socks5://127.0.0.1:10808", "User")
        }
    } else {
        Write-Log "TUN interface 'aitek-tun' already active."
    }
} elseif ($tunService -and $tunService.Status -eq 'Running') {
    Write-Log "TUN service already running."
} else {
    Write-Log "TUN service not installed. Run install-aitek-tun-service.ps1 as Admin once."
}

# 3) Launch target app
if ($TargetApp) {
    Write-Log "Launching: $TargetApp"
    Start-Process -FilePath $TargetApp
}

Write-Log "=== Done ==="
