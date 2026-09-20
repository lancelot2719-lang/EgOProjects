# Clean-Audiobooks.ps1
$SourceDir = 'D:\AI_Project\Книги\Аудиокниги\Отработанные аудио'
$TargetDir = 'D:\AI_Project\Книги\Аудиокниги\Отработанные аудио\FinalBook'

if (!(Test-Path $TargetDir)) {
    New-Item -ItemType Directory -Path $TargetDir -Force | Out-Null
}

$StartMarkers = @('Предисловие','Введение','Глава','Часть','Эпилог','Послесловие','От автора','Посвящение','Благодарности')
$EndMarker = 'Эту книгу хорошо дополняют'

$Files = Get-ChildItem -LiteralPath $SourceDir -File -Filter '*.txt' | Sort-Object Name

$processed = 0; $errors = 0

foreach ($File in $Files) {
    try {
        Write-Host 'Processing:' $File.Name -ForegroundColor Cyan
        $Content = Get-Content -LiteralPath $File.FullName -Raw -Encoding UTF8

        $Content = $Content -replace 'Speaker A: Вы можете слушать и скачать эту и другие аудиокниги в Telegram[^.]*\.?\s*', ''

        $startPos = -1
        foreach ($m in $StartMarkers) {
            $pos = $Content.IndexOf($m)
            if ($pos -ge 0 -and ($startPos -eq -1 -or $pos -lt $startPos)) {
                $startPos = $pos
            }
        }

        if ($startPos -gt 0) {
            $Content = $Content.Substring($startPos)
        }

        $endPos = $Content.IndexOf($EndMarker)
        if ($endPos -gt 0) {
            $Content = $Content.Substring(0, $endPos)
        }

        $Content = $Content -replace '\[[^\]]*\]', ''
        $Content = $Content -replace '\s+', ' '
        $Content = $Content.Trim()

        $TargetPath = Join-Path $TargetDir $File.Name
        Set-Content -LiteralPath $TargetPath -Value $Content -Encoding UTF8

        $processed++
        Write-Host '  Done' -ForegroundColor Green
    } catch {
        $errors++
        Write-Host '  ERROR:' $File.Name '-' $_ -ForegroundColor Red
    }
}

Write-Host ''
Write-Host '=============================' -ForegroundColor Yellow
Write-Host 'Processed:' $processed '| Errors:' $errors -ForegroundColor Yellow
Write-Host '=============================' -ForegroundColor Yellow
