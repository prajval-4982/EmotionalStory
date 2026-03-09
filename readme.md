# ✒️ Emotional Story Generator

A local AI-powered application that weaves creative, emotion-driven stories based on your inputs. By adjusting parameters like **Emotional Intensity** and **Creativity**, you can generate unique narratives that feel alive—all running locally on your machine without external API costs.

---

## ✨ Features

* **🧠 Local AI Inference:** Runs entirely on your computer using the **Llama 3.2** model (via `llama.cpp`). No data leaves your device.
* **🎭 Multi-Emotion Logic:** Select complex emotional blends (e.g., "Sadness" + "Hope") to guide the story's mood.
* **🎚️ Fine-Grained Control:**
* **Intensity Slider:** Control how heavily the emotion impacts the writing.
* **Creativity (Temperature):** Switch between deterministic logic and wild creativity.


* **⚡ Real-Time Streaming:** Watch the story be typed out token-by-token, just like ChatGPT.
* **💾 Export:** Download your generated stories as text files.
* **🎨 Modern UI:** A clean, dark-themed interface built with vanilla HTML/CSS/JS.

---

## 📂 Project Structure

```text
Gen-ai/
├── backend/
│   ├── models/
│   │   └── Llama-3.2-3B-Instruct.Q4_K_M.gguf  <-- Your AI Model (download separately)
│   ├── app.py                 # FastAPI Server (Main Entry Point)
│   ├── story_generator.py     # AI Inference & Streaming
│   ├── prompt_builder.py      # System & User Prompt Construction
│   ├── dataset_utils.py       # Emotion Style Blending Logic
│   └── requirements.txt       # Python Dependencies
│
├── frontend/
│   ├── index.html             # User Interface
│   ├── style.css              # Styling
│   ├── script.js              # Frontend Logic
│   └── pen-icon.png           # Favicon
│
├── .gitignore
└── readme.md

```

---

## 🚀 Installation & Setup

### 1. Prerequisites

* **Python 3.10** or higher.
* **RAM:** At least 8GB (4GB for the model + OS overhead).

### 2. Clone the Repository

```bash
git clone https://github.com/prajval-4982/EmotionalStory.git
cd EmotionalStory

```

### 3. Set Up Virtual Environment

It is recommended to use a virtual environment to keep dependencies clean.

**Windows (PowerShell):**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate

```

**Mac/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate

```

### 4. Install Dependencies

```bash
pip install -r backend/requirements.txt

```

*(Note: If you have an NVIDIA GPU, install the CUDA version of `llama-cpp-python` for faster generation).*

### 5. Download the Model

You need the **Llama 3.2** GGUF model file.

1. Go to [Hugging Face - Llama-3.2-3B-Instruct-GGUF](https://huggingface.co/bartowski/Llama-3.2-3B-Instruct-GGUF).
2. Download the file named: **`Llama-3.2-3B-Instruct.Q4_K_M.gguf`** (~2.0 GB).
3. Place it inside the `backend/models/` folder.

---

## 🏃‍♂️ How to Run

1. **Start the Backend Server:**
From the project root, run:
```bash
python backend/app.py

```


2. **Access the App:**
Open your web browser and go to:
👉 **`http://127.0.0.1:8001`**
3. **Weave a Story:**
* Enter a **Story Seed** (e.g., *"An astronaut lost in space"*).
* Select an **Emotion** (e.g., *Fear*).
* Adjust **Intensity** and **Creativity**.
* Click **Weave Story**.



---

## 🛠️ Troubleshooting

**Error: `[Errno 10048] Address already in use**`

* This means Port 8000 or 8001 is busy.
* **Fix:** The code is currently set to use port **8001**. Ensure no other instance is running. You can kill old processes or change the port in the `if __name__ == "__main__":` block in `app.py`.

**Error: `Model not found**`

* Ensure the `.gguf` file is exactly named `Llama-3.2-3B-Instruct.Q4_K_M.gguf` and is located in `backend/models/`.

**Slow Generation?**

* Running on CPU is slower than GPU. Lower the `max_tokens` in `story_generator.py` if you need faster results.

---

## 📜 License

This project is open-source and available for educational purposes.

---

*Built with ❤️ using Llama 3 & FastAPI.*