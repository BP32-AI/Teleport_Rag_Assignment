# src/retriever.py

from src.embeddings import EmbeddingModel
from src.query_expander import MockQueryExpander


class Retriever:
    def __init__(self, vector_store):
        self.embedding_model = EmbeddingModel()
        self.vector_store = vector_store
        self.query_expander = MockQueryExpander()

    def retrieve_raw(self, query, top_k=3):
        query_embedding = self.embedding_model.generate_embeddings([query])[0]

        return self.vector_store.search(query_embedding, top_k)

    def retrieve_enhanced(self, query, top_k=3):
        expanded_query = self.query_expander.expand_query(query)

        query_embedding = self.embedding_model.generate_embeddings([expanded_query])[0]

        return self.vector_store.search(query_embedding, top_k)