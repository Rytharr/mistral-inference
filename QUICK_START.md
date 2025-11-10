# Quick Launcher Guide

## Easiest Way to Run (No VS Code needed)

### Option 1: Double-Click Batch File (Simplest)
1. Navigate to: `c:\GitHub\mistral-inference\`
2. Double-click: `start_chat.bat`
3. Chat window opens automatically!

### Option 2: PowerShell Script (Recommended)
1. Navigate to: `c:\GitHub\mistral-inference\`
2. Right-click `start_chat.ps1`
3. Select "Run with PowerShell"

### Option 3: Maximum Uncensored Version
1. Navigate to: `c:\GitHub\mistral-inference\`
2. Right-click `start_chat_max.ps1`
3. Select "Run with PowerShell"
   - Uses wizard-uncensored-max model
   - Includes DAN mode option

## Create Desktop Shortcuts

### For Batch File:
1. Right-click `start_chat.bat`
2. Select "Send to" → "Desktop (create shortcut)"
3. Double-click desktop shortcut anytime to launch

### For PowerShell (if needed):
1. Right-click desktop → New → Shortcut
2. Location: `powershell.exe -ExecutionPolicy Bypass -File "c:\GitHub\mistral-inference\start_chat.ps1"`
3. Name it: "Uncensored Chat"
4. Click Finish

## Command Line Options

### From Any PowerShell Window:
```powershell
cd c:\GitHub\mistral-inference
.\start_chat.ps1
```

### From Any Command Prompt:
```cmd
cd c:\GitHub\mistral-inference
start_chat.bat
```

### Quick One-Liner:
```powershell
cd c:\GitHub\mistral-inference; python uncensored_chat.py
```

## Available Models

Once chat starts, you can switch models by typing:
- `model dolphin-mistral` - Default uncensored
- `model wizard-uncensored-max` - Custom jailbroken version
- `model wizard-vicuna-uncensored:7b` - Base uncensored
- `model nous-hermes2` - Very uncensored

## Files Overview

| File | Purpose |
|------|---------|
| `start_chat.bat` | Windows batch launcher (easiest) |
| `start_chat.ps1` | PowerShell launcher with checks |
| `start_chat_max.ps1` | Launches maximum uncensored version |
| `uncensored_chat.py` | Main chat script |
| `uncensored_chat_max.py` | Enhanced with DAN mode |

## Troubleshooting

**"Python not found"**
- Install Python from https://www.python.org/
- Make sure "Add to PATH" is checked during install

**"ollama not found"**
- The scripts automatically add Ollama to PATH
- If still not working, reinstall Ollama from https://ollama.ai/

**"Model not found"**
- Type `model dolphin-mistral` in the chat to switch
- Or download: `ollama pull dolphin-mistral`

---

**TL;DR:** Just double-click `start_chat.bat` - that's it! 🚀
