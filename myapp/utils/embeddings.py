import ollama
from typing import List
from langchain.embeddings.base import Embeddings

class OllamaEmbeddings(Embeddings):
    def __init__(self, model: str):
        self.model = model

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        embeddings = []
        for t in texts:
            response = ollama.embed(model=self.model, input=t)
            embeddings.append(response["embeddings"][0])
        return embeddings

    def embed_query(self, text: str) -> List[float]:
        response = ollama.embed(model=self.model, input=text)
        return response["embeddings"][0]
