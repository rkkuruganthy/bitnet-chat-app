
# 🧠 BitNet Chat App (Fully Local LLM Assistant)

A **completely offline** Local LLM (Large Language Model) app running on macOS (M1/M2) using `BitNet` models powered by `llama.cpp` backend with a Streamlit UI and FastAPI backend. Ideal for developers who want secure, low-latency general chat and coding assistance **without relying on OpenAI APIs or the cloud**.

---
---

## 🤖 What is BitNet.cpp?

BitNet.cpp is an optimized way to run **BitNet** models via `llama.cpp`, using Apple Metal for acceleration. BitNet (by Microsoft Research) is a Transformer-like architecture designed with binary or quantized weights to:

- Reduce memory usage significantly
- Enable faster inference (compared to LLaMA-sized models)
- Maintain competitive performance with fewer parameters

### 🔍 Why BitNet?

- 🧠 **Compact + Smart**: BitNet-3B can match or beat larger models like LLaMA 7B on many tasks.
- ⚡ **Fast & Efficient**: Smaller memory footprint makes it ideal for on-device use (macOS, iOS).
- 🔐 **Offline Privacy**: No API keys, no cloud, 100% local.

---

## 📁 Project Structure

```
bitnet-chat-app/
├── app.py                       # Streamlit UI (user prompt input/output)
├── api_server.py               # FastAPI backend API to route prompt requests
├── bitnet_runner.py            # Calls llama.cpp with BitNet model via subprocess
├── llama.cpp/                  # llama.cpp engine (Metal-enabled build)
│   └── build/bin/llama-cli     # Compiled CLI binary used to run inference
├── models/
│   └── BitNet/
│       └── bitnet_b1_58-3b-q8_0.gguf  # Downloaded BitNet GGUF model (3.3 GB)
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions (macOS M1/M2)

### 1. Clone llama.cpp and build with Metal

```bash
git clone https://github.com/ggerganov/llama.cpp.git
cd llama.cpp
mkdir build && cd build
cmake .. -DLLAMA_METAL=on
cmake --build . --config Release
```

Verify:
```bash
./bin/llama-cli --help
```

### 2. Download a BitNet GGUF model

You can get BitNet models from HuggingFace, e.g.:

- [`bitnet_b1_58-3b-q8_0.gguf`](https://huggingface.co/TheBloke/BitNet-b1_58-3B-GGUF)

Place it in:

```bash
bitnet-chat-app/models/BitNet/bitnet_b1_58-3b-q8_0.gguf
```

### 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

Contents of `requirements.txt`:

```
streamlit
fastapi
uvicorn
requests
```

---

## 🚀 Running the App

### Terminal 1 – Start FastAPI Server

```bash
uvicorn api_server:app --reload --port 8000
```

### Terminal 2 – Start Streamlit UI

```bash
streamlit run app.py
```

Then open your browser: [http://localhost:8501](http://localhost:8501)

You can now chat with the BitNet model locally!


## ✅ Example CURL Test

```bash
curl -X POST http://localhost:8000/generate \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Explain BitNet in 2 sentences", "max_tokens": 200}'
```

---

## 🧠 Future Enhancements

- [ ] Model selector dropdown in UI
- [ ] Prompt/response caching
- [ ] Streaming token output
- [ ] Docker container for easy deployment

---

## 🛡️ Disclaimer

This app is intended for local experimentation with open-source LLMs. BitNet models and llama.cpp are subject to their respective licenses.

---
