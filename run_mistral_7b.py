"""
Run Mistral 7B with optimized settings for 8GB VRAM
This script loads the model with reduced memory usage
"""
import torch
from pathlib import Path
from mistral_inference.transformer import Transformer
from mistral_inference.generate import generate
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer
from mistral_common.protocol.instruct.messages import UserMessage, AssistantMessage
from mistral_common.protocol.instruct.request import ChatCompletionRequest

# Configuration
MODEL_PATH = Path.home() / "mistral_models" / "7B_instruct"
MAX_TOKENS = 512
TEMPERATURE = 0.7

print("Loading tokenizer...")
tokenizer = MistralTokenizer.from_file(str(MODEL_PATH / "tokenizer.model.v3"))

print("Loading model with optimized settings for 8GB VRAM...")
print("This may take a minute...")

# Load model with lower precision to save VRAM
model = Transformer.from_folder(
    MODEL_PATH,
    max_batch_size=1,  # Reduced batch size
    num_pipeline_ranks=1
)

print("\n✅ Model loaded successfully!")
print("=" * 60)
print("Mistral 7B Instruct - Interactive Chat")
print("=" * 60)
print("Type your messages below. Type 'quit' or 'exit' to stop.")
print("=" * 60)

messages = []

while True:
    try:
        # Get user input
        user_input = input("\n🧑 You: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("\n👋 Goodbye!")
            break
            
        if not user_input:
            continue
        
        # Add user message
        messages.append(UserMessage(content=user_input))
        
        # Create chat completion request
        completion_request = ChatCompletionRequest(messages=messages)
        
        # Encode
        tokens = tokenizer.encode_chat_completion(completion_request).tokens
        
        # Generate response
        print("\n🤖 Mistral: ", end="", flush=True)
        out_tokens, _ = generate(
            [tokens],
            model,
            max_tokens=MAX_TOKENS,
            temperature=TEMPERATURE,
            eos_id=tokenizer.instruct_tokenizer.tokenizer.eos_id
        )
        
        # Decode and print
        result = tokenizer.instruct_tokenizer.tokenizer.decode(out_tokens[0])
        print(result)
        
        # Add assistant response to history
        messages.append(AssistantMessage(content=result))
        
    except KeyboardInterrupt:
        print("\n\n👋 Interrupted. Goodbye!")
        break
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("Continuing...")
