# 🛍️ Clothes Store Chatbot

A simple AI-powered chatbot built with **OpenAI** and **Gradio**.  
The chatbot acts as a helpful store assistant that **encourages customers to explore items on sale** (especially hats 🧢) and handles special rules for different product requests.

---

## ✨ Features
- 💬 **Conversational AI** using OpenAI’s Chat Completions API  
- 🧢 **Sales-focused assistant** – encourages customers to buy items on sale (hats 60% off, most others 50%)  
- 👞 **Custom rules** – e.g. shoes are not on sale, belts are not sold  
- 🎨 **Interactive UI** powered by [Gradio](https://gradio.app)  
- ⚡ **Streaming responses** for a smooth real-time chat experience  

---

## 🗂️ Project Structure
```bash
├── config.py       # Loads environment variables (API key, model name)
├── prompts.py      # All system prompt messages and rules
├── chatbot.py      # Chat logic (builds messages, streams responses)
├── main.py         # Entry point, launches Gradio chat interface
├── requirements.txt
└── README.md
```

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/clothes-store-chatbot.git
cd clothes-store-chatbot
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up environment variables
Create a .env file in the project root:
```bash
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL_NAME=gpt-4o-mini
```

### 4. Run the app
```bash
python main.py
```

This will launch a Gradio web interface (by default on http://127.0.0.1:7860).
