@echo off
echo Installing Text Humanizer dependencies...
echo.

REM Get the Python executable path
set PYTHON_EXE=C:\Users\yasee\AppData\Local\Programs\Python\Python310\python.exe

if not exist "%PYTHON_EXE%" (
    echo ERROR: Python not found at %PYTHON_EXE%
    echo Please update PYTHON_EXE in this script with your Python path
    pause
    exit /b 1
)

echo Installing Flask and dependencies...
"%PYTHON_EXE%" -m pip install flask werkzeug

echo Installing PDF and Word processing libraries...
"%PYTHON_EXE%" -m pip install python-docx PyMuPDF reportlab

echo.
echo ============================================
echo Installation complete!
echo ============================================
echo.
echo To run the app, double-click run.bat or type:
echo python app.py
echo.
pause
