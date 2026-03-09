import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse, FileResponse
from fastapi.staticfiles import StaticFiles 
from pydantic import BaseModel, Field

# 1. Import Local Llama (Text)
from story_generator import generate_story_stream

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class StoryRequest(BaseModel):
    prompt: str = Field(min_length=1, max_length=2000)
    emotion: str = Field(min_length=1, max_length=100)
    strength: int = Field(ge=1, le=10)
    creativity: float = Field(ge=0.6, le=1.2)

# --- ONLY STORY GENERATION ENDPOINT ---
@app.post("/generate")
async def generate(data: StoryRequest):
    # Llama Text Generation
    return StreamingResponse(
        generate_story_stream(data.prompt, data.emotion, data.strength, data.creativity),
        media_type="text/plain"
    )

# Static Files
current_dir = os.path.dirname(os.path.abspath(__file__))
frontend_dir = os.path.join(current_dir, "../frontend")
app.mount("/static", StaticFiles(directory=frontend_dir), name="static")

@app.get("/")
async def read_root():
    return FileResponse(os.path.join(frontend_dir, 'index.html'))

if __name__ == "__main__":
    import uvicorn
    # Using Port 8001 to prevent 'Address already in use'
    print("Starting Story Server on http://127.0.0.1:8001")
    uvicorn.run(app, host="127.0.0.1", port=8001)