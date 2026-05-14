# tests/test_embeddings.py


from src.embeddings import EmbeddingModel


def test_embedding_generation():
    model = EmbeddingModel()

    texts = ["hello world"]

    embeddings = model.generate_embeddings(texts)

    assert len(embeddings) == 1