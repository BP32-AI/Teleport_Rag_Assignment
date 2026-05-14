# tests/test_retrieval.py

from data.documents import DOCUMENTS
from src.embeddings import EmbeddingModel
from src.vector_store import VectorStore
from src.retriever import Retriever


def test_retrieval_returns_results():

    embedding_model = EmbeddingModel()

    embeddings = embedding_model.generate_embeddings(DOCUMENTS)

    vector_store = VectorStore(len(embeddings[0]))

    vector_store.add_documents(embeddings, DOCUMENTS)

    retriever = Retriever(vector_store)

    results = retriever.retrieve_raw(
        "How does the system handle peak load?"
    )

    assert len(results) == 3