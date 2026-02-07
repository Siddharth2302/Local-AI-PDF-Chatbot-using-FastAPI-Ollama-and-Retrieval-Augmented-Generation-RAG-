# Local AI PDF Chatbot (RAG) using FastAPI + Ollama

A fully local Retrieval-Augmented Generation (RAG) chatbot that allows users to upload PDFs and ask questions based on their content. The system extracts text, generates embeddings, performs semantic search, and produces grounded responses using a locally running LLM via Ollama.

This project demonstrates production-style AI backend architecture including document ingestion, vector storage, semantic retrieval, and LLM prompt grounding.

---

## Features

- Upload and ingest PDF documents
- Extract and chunk text automatically
- Generate embeddings using local embedding model
- Perform semantic similarity search using cosine similarity
- Generate context-aware answers using a local LLM
- Fully local — no external API required
- REST API with automatic Swagger documentation
- Modular and scalable backend design

---

## Tech Stack

Backend:
- Python
- FastAPI
- Pydantic

AI / LLM:
- Ollama
- Gemma / LLaMA models
- nomic-embed-text embedding model

Document Processing:
- PyPDF

Other:
- Requests
- Uvicorn

## Architecture

PDF Upload
↓
Text Extraction
↓
Text Chunking
↓
Embedding Generation
↓
Vector Storage (In-Memory)
↓
Similarity Search
↓
Prompt Construction
↓
LLM Response Generation

## project structure
│
├── main.py # FastAPI server and endpoints
├── pdf_reader.py # PDF text extraction
├── chunker.py # Text chunking logic
├── embeddings.py # Embedding generation
├── cosine_search.py # Similarity search logic
├── prompt.py # Prompt construction
├── data_store.py # In-memory vector storage
├── requirements.txt # Dependencies
└── README.md


---

## How It Works

1. User uploads PDF
2. System extracts text using PyPDF
3. Text is split into smaller chunks
4. Embeddings are generated using local embedding model
5. Embeddings stored in memory
6. User asks question
7. Question embedding generated
8. Cosine similarity finds most relevant chunks
9. Prompt constructed with context
10. LLM generates grounded response

---

## Example Workflow

Upload PDF:

POST /upload-pdf

Ask question:

POST /ask

{
"question": "Explain neural networks"
}

Receive grounded answer based on uploaded document.

---

## Key Learning Outcomes

This project demonstrates:

- FastAPI backend development
- REST API design
- File upload handling
- Retrieval-Augmented Generation (RAG)
- Embedding generation
- Semantic search
- Prompt engineering
- Local LLM integration
- Modular AI system design

---

## Future Improvements

- Replace in-memory storage with FAISS vector database
- Add persistent storage
- Add frontend interface
- Support multiple documents
- Add conversation memory
- Deploy to cloud

---

## Author

Siddharth Rajesh

GitHub: https://github.com/Siddharth2302

---

## License

This project is for educational and portfolio purposes.


