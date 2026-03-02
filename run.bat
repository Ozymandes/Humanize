@echo off
echo Starting Text Humanizer Web App...
echo.

REM Get the Python executable path
set PYTHON_EXE=C:\Users\yasee\AppData\Local\Programs\Python\Python310\python.exe

if not exist "%PYTHON_EXE%" (
    echo ERROR: Python not found at %PYTHON_EXE%
    echo Please update PYTHON_EXE in this script with your Python path
    pause
    exit /b 1
)

"%PYTHON_EXE%" app.py

pause
