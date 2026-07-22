# 🤖 AI Chat Assistant (Python)

An intermediate-level AI chatbot/assistant project built with Python and an LLM API (supports both Anthropic Claude and OpenAI). It includes conversation memory, a local knowledge base (lightweight RAG via TF-IDF), and a clean CLI interface. Ready to upload to GitHub.

## ✨ Features

- 💬 **Chat with AI** — Talk to Claude or GPT models (provider is switchable via `.env`)
- 🧠 **Persistent Memory** — Conversations are saved to JSON files and can be reloaded later
- 📚 **Local Knowledge Base (RAG)** — Drop your own `.txt` files into `data/knowledge/`; the assistant finds relevant content and uses it as context (TF-IDF based, no heavy model downloads required)
- ⌨️ **CLI Commands** — `/help`, `/reset`, `/save`, `/load`, `/docs`, `/exit`
- 🔒 **Environment-based config** — API keys live in `.env`, never hardcoded in code
- 🧩 **Modular code** — Each feature lives in its own file, easy to extend (web UI, Discord bot, etc.)

## 📁 Project Structure

```
ai-chat-assistant/
├── main.py                     # Entry point — CLI loop
├── requirements.txt
├── .env.example                 # Copy to .env and add your API key
├── assistant/
│   ├── __init__.py
│   ├── config.py                # Loads env vars
│   ├── llm_client.py             # Anthropic/OpenAI API calls
│   ├── memory.py                 # Conversation history save/load
│   └── knowledge_base.py         # TF-IDF based simple RAG
├── data/
│   ├── knowledge/
│   │   └── sample.txt            # Example knowledge doc
│   └── conversations/            # Saved chat history is stored here
└── README.md
```

## 🚀 Setup

1. **Clone / download** the repo, then move into the folder:
   ```bash
   cd ai-chat-assistant
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set your API key:**
   ```bash
   cp .env.example .env
   ```
   Open `.env` and fill in your key:
   ```
   LLM_PROVIDER=anthropic         
   ANTHROPIC_API_KEY=sk-ant-xxxx
   OPENAI_API_KEY=sk-xxxx
   MODEL_NAME=claude-sonnet-4-6    
   ```

5. **Run it:**
   ```bash
   python main.py
   ```

## 💻 Usage

```
You: What are decorators in Python?
Assistant: A decorator is a function that wraps another function to modify its behavior...

You: /docs
📚 Knowledge base contains 3 documents: sample.txt, notes.txt, faq.txt

You: /save
✅ Conversation saved as conversations/chat_20260722_143210.json

You: /reset
🔄 Conversation history cleared.

You: /exit
👋 Bye!
```

### Commands

| Command   | Description                                      |
|-----------|---------------------------------------------------|
| `/help`   | Shows all available commands                       |
| `/reset`  | Clears the current conversation memory              |
| `/save`   | Saves the current conversation to a JSON file       |
| `/load`   | Loads a previously saved conversation               |
| `/docs`   | Lists the files currently in the knowledge base     |
| `/exit`   | Quits the assistant                                 |

## 🧠 How the Knowledge Base (RAG-lite) Works

Drop `.txt` files into `data/knowledge/` (your notes, docs, FAQs, whatever you need). Whenever you ask something, the assistant uses TF-IDF similarity to find the most relevant chunk and sends it as context to the AI — this lets the assistant give accurate, grounded answers about your own data without needing to download a large embedding model.

## 🛠️ Tech Stack

- **Python 3.9+**
- **Anthropic SDK** / **OpenAI SDK** — for LLM API calls
- **scikit-learn** — TF-IDF vectorization (lightweight RAG)
- **python-dotenv** — environment variables

## 📤 Uploading to GitHub

```bash
git init
git add .
git commit -m "Initial commit: AI Chat Assistant"
git branch -M main
git remote add origin https://github.com/<your-username>/ai-chat-assistant.git
git push -u origin main
```

> ⚠️ **Never commit your `.env` file** — it's already excluded via `.gitignore`. Only push `.env.example`.

## 🔮 Future Ideas (ways to extend this)

- Add a Flask/FastAPI web UI
- Voice input/output (speech-to-text, text-to-speech)
- Multi-user support with a database
- Real embeddings (sentence-transformers) for better RAG
- Telegram / Discord / WhatsApp bot integration

## 📄 License

MIT License — free to use, modify, and share.
