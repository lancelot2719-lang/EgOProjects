sc.exe stop AitekTun
Start-Sleep -Seconds 5
sc.exe delete AitekTun
Start-Sleep -Seconds 2
ipconfig /flushdns
Write-Output "Done"
