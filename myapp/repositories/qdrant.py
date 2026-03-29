from __future__ import annotations
from types import TracebackType
from typing import Optional, Dict, Any, List

from qdrant_client import QdrantClient
from qdrant_client.http import models as qm

from langchain_qdrant import QdrantVectorStore

from myapp.utils.config import config
from myapp.utils.embeddings import OllamaEmbeddings


class QdrantRepository:
    def __init__(self) -> None:
        self._client: Optional[QdrantClient] = None
        self._vectorstore: Optional[QdrantVectorStore] = None

    def __enter__(self) -> "QdrantRepository":
        self._client = QdrantClient(
            host=config.qdrant_host,
            port=config.qdrant_port,
        )

        embeddings = OllamaEmbeddings(
            model=config.ollama_embed_model
        )
        self.ensure_collection("medical_cases", vector_size=1024)

        self._vectorstore = QdrantVectorStore(
            client=self._client,
            collection_name="medical_cases",
            embedding=embeddings,
        )

        return self


    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        self._client = None
        self._vectorstore = None

    @property
    def client(self) -> QdrantClient:
        if self._client is None:
            raise RuntimeError("Use inside 'with'")
        return self._client

    def ensure_collection(self, name: str, vector_size: int) -> None:
        print(self.client.collection_exists(name))
        if not self.client.collection_exists(name):
            self.client.create_collection(
                collection_name=name,
                vectors_config=qm.VectorParams(
                    size=vector_size,
                    distance=qm.Distance.COSINE,
                ),
            )

    def upsert_points(
            self,
            texts: List[str],
            metadatas: List[Dict[str, Any]],
    ) -> None:

        if self._vectorstore is None:
            raise RuntimeError("Use inside 'with'")

        self._vectorstore.add_texts(
            texts=texts,
            metadatas=metadatas
        )

    @property
    def vs(self) -> QdrantVectorStore:
        if self._vectorstore is None:
            raise RuntimeError("Use inside 'with'")
        return self._vectorstore


    def search(
            self,
            query: str,
            k: int = 10,
            filter_payload: Optional[Dict[str, Any]] = None,
    ):
        q_filter = None

        if filter_payload:
            must_clauses = []
            for key, condition in filter_payload.items():
                if "any" in condition:
                    must_clauses.append(
                        qm.FieldCondition(
                            key=key,
                            match=qm.MatchAny(any=condition["any"]),  # 🔹 теперь просто any
                        )
                    )
                elif "match" in condition:
                    must_clauses.append(
                        qm.FieldCondition(
                            key=key,
                            match=qm.MatchValue(value=condition["match"])
                        )
                    )
            if must_clauses:
                q_filter = qm.Filter(must=must_clauses)

        return self.vs.similarity_search(
            query=query,
            k=k,
            filter=q_filter,
        )