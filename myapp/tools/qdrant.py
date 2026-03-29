from __future__ import annotations
from typing import Optional, Dict, Any

from myapp.repositories import QdrantRepository
from myapp.utils.config import Config
from myapp.utils.embeddings import OllamaEmbeddings


class QdrantToolClass:
    def __init__(self, embedding_client: OllamaEmbeddings):
        self.embedding_client = embedding_client

    async def run(
        self,
        query: str,
        filter_payload: Optional[Dict[str, Any]] = None,
        k: int = 5,
    ) -> str:
        """
        Выполняет поиск в Qdrant и возвращает текстовый результат для LLM
        """

        with QdrantRepository() as repo:
            results = repo.search(
                query=query,
                k=k,
                filter_payload=filter_payload
            )

        if not results:
            return "No relevant medical cases found."

        formatted = []
        for i, doc in enumerate(results, 1):
            text = doc.page_content
            meta = doc.metadata

            formatted.append(
                f"{i}. {text}\nMetadata: {meta}"
            )

        return "\n\n".join(formatted)