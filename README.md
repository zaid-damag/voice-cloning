# 🎙️ Voice Cloning with Python & Coqui TTS

## 📌 Overview
This project provides a **voice cloning system** using [Coqui TTS](https://github.com/coqui-ai/TTS).  
It converts **text to speech** and clones voices from a reference audio sample.  
Includes a **GUI interface (Gradio)** with **multi-language support** for easy interaction.

---

## 🚀 Features
- ✅ Text-to-Speech (TTS) using Coqui TTS
- ✅ Voice cloning from reference audio
- ✅ GUI interface with [Gradio](https://www.gradio.app/)
- ✅ Multi-language support
- ✅ Ready-to-use Docker environment

---

## 📂 Project Structure
.
├── Docker/ # Docker build and environment files

├── clone_tts.py # Main Python script

├── pyproject.toml # Dependencies and project configuration

├── README.md # Project documentation

├── LICENSE # License file

└── .gitignore # Ignored files

yaml
Copy code

---

## 🖥️ Requirements
- **Python 3.10+** (recommended 3.11)
- **Coqui TTS**
- **Gradio**

Or simply use **Docker** (no need to install Python manually).

---

## 🔧 Installation (without Docker)
```bash
# Clone the repository
git clone https://github.com/zaid-damag/voice-cloning.git
cd voice-cloning

# Install dependencies
pip install -e .
🐳 Run with Docker
bash
Copy code
# Build the Docker image
docker build -t voice-cloning .

# Run the container
docker run -it --rm -p 7860:7860 voice-cloning
Now open http://localhost:7860 in your browser to access the Gradio interface.

▶️ Usage
Run with Python
bash
Copy code
python clone_tts.py
Run with Docker
bash
Copy code
docker run -it --rm -p 7860:7860 voice-cloning
📝 Example
Provide a reference audio file (voice sample).

Enter your text in the Gradio interface.

Click Generate → You get cloned speech output.

📜 License
This project is licensed under the GPL-3.0 License.
See the LICENSE file for details.

# voice-cloning
Voice cloning project using Python and Coqui TTS. Converts text to speech and clones voices based on reference audio. Simple setup and usage for generating high-quality speech from text. 
