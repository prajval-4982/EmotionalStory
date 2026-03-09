import os
from llama_cpp import Llama
from prompt_builder import build_chat_messages

# --- CONFIGURATION ---
# Get current directory of this script
current_dir = os.path.dirname(os.path.abspath(__file__))
model_filename = "Llama-3.2-3B-Instruct.Q4_K_M.gguf"

# Construct path: backend/models/filename
MODEL_PATH = os.path.join(current_dir, "models", model_filename)

# Initialize Model (Loads into RAM once)
try:
    print(f"🔍 Loading Model from: {MODEL_PATH}")
    if not os.path.exists(MODEL_PATH):
         raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")

    llm = Llama(
        model_path=MODEL_PATH,
        n_ctx=4096,       # Context window
        n_gpu_layers=0,   # Set to -1 if you have a GPU, 0 for CPU
        verbose=False 
    )
    print("✅ Model Loaded and Ready!")
except Exception as e:
    print(f"❌ FATAL ERROR: {e}")
    llm = None

def generate_story_stream(seed, emotion, strength, creativity):
    if not llm:
        yield "Error: AI Model is not loaded. Please check the server logs."
        return

    # 1. Build the messages
    messages = build_chat_messages(seed, emotion, strength)

    # 2. Dynamic Temperature Logic
    temp = creativity + (strength - 5) * 0.05
    temp = max(0.65, min(1.1, temp)) 

    # 3. Generate Stream
    stream = llm.create_chat_completion(
        messages=messages,
        max_tokens=1024,
        temperature=temp,
        top_p=0.9,
        top_k=40,
        repeat_penalty=1.2,
        stream=True 
    )

    # 4. Yield content
    for chunk in stream:
        if "content" in chunk["choices"][0]["delta"]:
            yield chunk["choices"][0]["delta"]["content"]