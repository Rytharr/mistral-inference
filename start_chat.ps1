# Uncensored Chat Launcher - PowerShell version
# Right-click and "Run with PowerShell" or run from PowerShell terminal

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Starting Uncensored Chat..." -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Add Ollama to PATH
$env:Path += ";$env:LOCALAPPDATA\Programs\Ollama"

# Change to script directory
Set-Location $PSScriptRoot

# Check if Python is available
if (!(Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "ERROR: Python not found!" -ForegroundColor Red
    Write-Host "Please install Python from https://www.python.org/" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

# Check if ollama package is installed
python -c "import ollama" 2>$null
if ($LASTEXITCODE -ne 0) {
    Write-Host "Installing ollama package..." -ForegroundColor Yellow
    pip install ollama
}

# Run the chat
Write-Host "Launching chat interface..." -ForegroundColor Green
Write-Host ""
python uncensored_chat.py

# Keep window open if there's an error
if ($LASTEXITCODE -ne 0) {
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Red
    Write-Host "An error occurred!" -ForegroundColor Red
    Write-Host "========================================" -ForegroundColor Red
    Read-Host "Press Enter to exit"
}
