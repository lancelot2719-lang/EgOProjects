# Run this ONCE as Administrator to install the TUN proxy service
# This creates system-wide VPN (like Happ does via TUN)

$ServiceName = "AitekTun"
$Tun2Proxy = "D:\Happ\tun2\tun2proxy-bin.exe"
$LogFile = "$env:TEMP\aitek-tun-service.log"

# Check if already installed
$svc = Get-Service -Name $ServiceName -ErrorAction SilentlyContinue
if ($svc) {
    Write-Output "Service '$ServiceName' already exists (Status: $($svc.Status))."
    if ($svc.Status -eq 'Stopped') {
        Start-Service -Name $ServiceName
        Write-Output "Service started."
    }
    exit
}

# Create the service
$params = @{
    Name = $ServiceName
    BinaryPathName = "`"$Tun2Proxy`" --proxy socks5://127.0.0.1:10808 --tun aitek-tun --bypass 158.160.169.14 --setup --dns over-tcp --daemonize --exit-on-fatal-error"
    DisplayName = "Aitek VPN TUN"
    Description = "System-wide VPN via Aitek subscription. Routes all traffic through SOCKS5 proxy. VPN server bypasses tunnel."
    StartupType = "Manual"
}
try {
    New-Service @params
    Write-Output "Service '$ServiceName' installed (manual start)."
    Write-Output "Use start-aitek-vpn.ps1 to start Xray and TUN together."
} catch {
    Write-Output "FAILED: $_"
    Write-Output "Run this script as Administrator."
    exit 1
}
