from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
import os
import requests
from pdf_reader import extract_text_from_pdf
from chunker import chunk_text
from embeddings import get_embedding
from cosine_search import query_search
from prompt import build_prompt
from data_store import document

app = FastAPI()


class InjestRequest(BaseModel):
    text: str

class QuestionRequest(BaseModel):
    question: str


@app.post("/injest")
def injest(data: InjestRequest):

    if not data.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty")

    
    chunks = chunk_text(data.text)

  
    for chunk in chunks:

        embedding = get_embedding(chunk)

        document.append({
            "text": chunk,
            "embedding": embedding
        })

    return {
        "message": "Text ingested successfully",
        "chunks_created": len(chunks),
        "total_chunks": len(document)
    }

@app.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):

    print("Step 1: File received:", file.filename)

    file_path = f"temp_{file.filename}"

    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)

    print("Step 2: File saved")

    text = extract_text_from_pdf(file_path)

    print("Step 3: Text extracted length:", len(text))

    os.remove(file_path)

    chunks = chunk_text(text)

    print("Step 4: Chunks created:", len(chunks))

    for chunk in chunks:
        embedding = get_embedding(chunk)
        document.append({
            "text": chunk,
            "embedding": embedding
        })

    print("Step 5: Embeddings stored")

    return {
        "message": "PDF uploaded and processed successfully",
        "chunks_created": len(chunks),
        "total_chunks": len(document)
    }

@app.post("/ask")
def ask_question(data: QuestionRequest):

    if not data.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty")

    context_chunks = query_search(data.question)

    prompt = build_prompt(context_chunks, data.question)

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "gemma3:1b",
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()

    return {
        "answer": result["response"],
        "context_used": context_chunks
    }

@app.get("/")
def home():
    return {"message": "RAG system running successfully"}
