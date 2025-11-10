# Running Mistral 7B on RTX 3060 Ti (8GB) - Ollama Setup

## Problem with mistral-inference

The `mistral-inference` library tries to load the entire 13.8GB model into GPU memory at once, which won't work with your 8GB VRAM.

## Solution: Use Ollama (Recommended)

Ollama is specifically designed for consumer GPUs and automatically manages memory.

### Step 1: Install Ollama

1. Download from: https://ollama.ai/download
2. Run the installer (it's a simple .exe for Windows)

### Step 2: Run Mistral 7B

Open PowerShell and run:

```powershell
# Pull and run Mistral 7B Instruct (quantized, ~4.1GB)
ollama run mistral

# Or for uncensored variants:
ollama run dolphin-mistral
```

### Available Models for Your 8GB GPU:

```powershell
# Mistral 7B (Official)
ollama run mistral              # 4.1GB

# Dolphin Mistral (Uncensored)
ollama run dolphin-mistral      # 4.1GB  

# Mistral OpenOrca
ollama run mistral-openorca     # 4.1GB

# Neural Chat 7B
ollama run neural-chat          # 4.1GB

# CodeLlama 7B (for coding)
ollama run codellama:7b         # 3.8GB

# Llama 2 7B Chat
ollama run llama2:7b-chat       # 3.8GB
```

### Usage:

```powershell
# Interactive chat
ollama run mistral

# One-off question
ollama run mistral "Explain quantum computing"

# List installed models
ollama list

# Remove a model to save space
ollama rm mistral
```

### Ollama API (for programming):

```python
# Install
pip install ollama

# Use in Python
import ollama

response = ollama.chat(model='mistral', messages=[
    {'role': 'user', 'content': 'Why is the sky blue?'}
])
print(response['message']['content'])
```

## Alternative: Use llama.cpp with GGUF

If you prefer command-line tools:

1. Download llama.cpp from: https://github.com/ggerganov/llama.cpp
2. Get GGUF quantized models from Hugging Face
3. Run with GPU offloading

```powershell
# Example (after setup)
.\main.exe -m mistral-7b-Q4_K_M.gguf -n 512 -p "Your prompt here" --n-gpu-layers 32
```

## Why Ollama is Better for Your Setup:

✅ Automatic memory management (CPU + GPU offloading)
✅ Quantized models (4-bit, fits easily in 8GB)
✅ Simple installation and usage
✅ Fast performance on consumer GPUs
✅ Large model library
✅ Built-in API server
✅ Regular updates

## Memory Usage Comparison:

| Model | Full Precision | 4-bit Quantized (Ollama) |
|-------|----------------|--------------------------|
| Mistral 7B | ~14GB VRAM | ~4.1GB VRAM ✅ |
| Mixtral 8x7B | ~94GB VRAM | ~26GB VRAM ❌ |
| Mistral Nemo 12B | ~24GB VRAM | ~7GB VRAM ✅ |

---

**Next Step:** Install Ollama from https://ollama.ai and run `ollama run mistral`
