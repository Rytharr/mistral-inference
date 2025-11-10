@echo off
REM Uncensored Chat Launcher - Double-click to run

echo ========================================
echo Starting Uncensored Chat...
echo ========================================
echo.

REM Add Ollama to PATH
set PATH=%PATH%;%LOCALAPPDATA%\Programs\Ollama

REM Change to script directory
cd /d "%~dp0"

REM Run the chat
python uncensored_chat.py

REM Keep window open if there's an error
if errorlevel 1 (
    echo.
    echo ========================================
    echo An error occurred!
    echo ========================================
    pause
)
