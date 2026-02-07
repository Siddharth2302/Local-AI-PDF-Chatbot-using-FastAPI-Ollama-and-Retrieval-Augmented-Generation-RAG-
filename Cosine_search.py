import math
from embeddings import get_embedding
from data_store import document
def cosine_similarity(vec1, vec2):
    dot_product = sum(a * b for a, b in zip(vec1, vec2))
    magnitude1 = math.sqrt(sum(a * a for a in vec1))
    magnitude2 = math.sqrt(sum(b * b for b in vec2))
    return dot_product / (magnitude1 * magnitude2)

def query_search(query , top_k=3):
    query_embedding = get_embedding(query)
    
    scored_chunks = []
    
    for item in document:
        score = cosine_similarity(query_embedding , item["embedding"])
        scored_chunks.append((score,item["text"]))
        
    scored_chunks.sort(reverse=True , key=lambda x : x[0])
    
    return [text for score, text in scored_chunks[:top_k]]
