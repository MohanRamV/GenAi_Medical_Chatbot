# Medibot - AI-Powered Medical Chatbot 🤖💊

Medibot is a context-aware, document-grounded AI chatbot designed to assist users with health-related queries. It uses Retrieval-Augmented Generation (RAG) to ensure factual accuracy by answering only from verified medical content.

---

## 🔍 Features

- 💬 Conversational memory: understands follow-up questions
- 📚 Retrieval from custom medical documents using Pinecone
- 💡 Medicine recommendations only when present in context (e.g., ibuprofen)
- ❌ Avoids hallucinations using strict prompt engineering
- 🌐 Web UI built with Flask & Bootstrap
- 🔐 Session-based context tracking

---

## 🧠 Tech Stack

| Layer         | Tools Used                       |
|---------------|----------------------------------|
| LLM           | Gemini 2.0 Flash via LangChain   |
| Vector DB     | Pinecone                         |
| Embeddings    | HuggingFace MiniLM-L6-v2         |
| Backend       | Flask (Python)                   |
| Frontend      | Bootstrap + jQuery               |
| Memory        | Flask sessions                   |

---

## 🚀 Setup Instructions

```bash
# Clone the repository
git clone https://github.com/your-username/medibot-chatbot.git
cd medibot-chatbot

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Set environment variables in .env file
PINECONE_API_KEY=your_key_here
GOOGLE_API_KEY=your_key_here
FLASK_SECRET_KEY=anything_secure

# Run the app
python app.py
```

Access it at: [http://localhost:8080](http://localhost:8080)

---

## 📦 Folder Structure
```
├── app.py                  # Flask backend
├── templates/
│   └── chat.html           # UI template
├── static/
│   └── style.css           # Custom styles
├── src/
│   ├── helper.py           # Embedding logic
│   └── prompt.py           # Custom prompts (if any)
├── .env                    # API keys (excluded)
├── requirements.txt        # Dependencies
└── README.md
```

---

## 📌 Important Notes
- **Medicine suggestions** are only returned if found in source docs.
- **Conversation memory** resets on page refresh.
- Ensure Pinecone index is populated with domain-relevant content.

---

## 🏁 Future Enhancements
- Add PDF uploader for dynamic document ingestion
- UI improvements for chat history and citations
- Authentication + user session tracking

---

## 🙌 Acknowledgements
- Code inspiration and snippets referenced from [Bappy Ahmed]
- [LangChain](https://github.com/langchain-ai/langchain)
- [Google Gemini](https://ai.google.dev/)
- [Pinecone](https://www.pinecone.io/)
- [HuggingFace Transformers](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)

---

> Made with ❤️ for safe and smart medical assistance.
