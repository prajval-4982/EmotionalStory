import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ API Key not found!")
else:
    client = genai.Client(api_key=api_key)
    print("Searching for available models...\n")
    
    try:
        # List all models
        for m in client.models.list():
            # We specifically want models that can generate images
            # But let's print everything just to be safe
            print(f"Model: {m.name}")
            print(f"   - Supported Actions: {m.supported_generation_methods}")
            print("-" * 20)
            
    except Exception as e:
        print(f"Error listing models: {e}")