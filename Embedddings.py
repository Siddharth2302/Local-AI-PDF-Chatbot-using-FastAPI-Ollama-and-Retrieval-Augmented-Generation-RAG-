import requests

ollama_embed_URL = "http://localhost:11434/api/embeddings"

def get_embedding(text : str):
    response = requests.post(
        ollama_embed_URL,
        json = {
            "model" : "nomic-embed-text",
            "prompt" : text
        }
    )
    result = response.json()
    return result["embedding"]
