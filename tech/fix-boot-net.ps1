# Ставится в автозагрузку — убирает TUN-адаптер, если он остался без Xray

$log = "$env:TEMP\boot-net-fix.log"
"--- Boot: $(Get-Date) ---" | Out-File $log

# TUN-адаптер висит без Xray? — интернета не будет
$tun = Get-NetAdapter -Name "aitek-tun" -ErrorAction SilentlyContinue
$xray = Get-Process -Name "xray" -ErrorAction SilentlyContinue

if ($tun -and (-not $xray)) {
    "TUN adapter found without Xray. Disabling..." | Out-File $log -Append
    Disable-NetAdapter -Name "aitek-tun" -Confirm:$false
    Start-Sleep 2
    # DNS flush
    ipconfig /flushdns | Out-Null
    "TUN disabled. Internet should work now." | Out-File $log -Append
} elseif ($tun -and $xray) {
    "TUN + Xray OK. VPN is active." | Out-File $log -Append
} else {
    "No TUN adapter. Internet should work." | Out-File $log -Append
}
