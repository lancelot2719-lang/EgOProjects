@echo off
if "%~1"=="" (
    echo Перетащи файл книги или папку с частями на этот .bat, либо запусти:
    echo    analyze.bat "путь к книге или папке с частями"
    pause
    exit /b 1
)
python "%~dp0analyze.py" %1
pause
