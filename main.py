# main.py

from data.documents import DOCUMENTS
from src.embeddings import EmbeddingModel
from src.vector_store import VectorStore
from src.retriever import Retriever
from src.benchmark import Benchmark


def main():

    # Step 1: Generate Embeddings
    embedding_model = EmbeddingModel()

    embeddings = embedding_model.generate_embeddings(DOCUMENTS)

    # Step 2: Initialize Vector Store
    embedding_dimension = len(embeddings[0])

    vector_store = VectorStore(embedding_dimension)

    vector_store.add_documents(embeddings, DOCUMENTS)

    # Step 3: Initialize Retriever
    retriever = Retriever(vector_store)

    # Step 4: Run Benchmark
    benchmark = Benchmark(retriever)

    results = benchmark.run()

    # Step 5: Print Results
    for result in results:
        print("\n" + "=" * 80)
        print(f"Query: {result['query']}")

        print("\nStrategy A - Raw Vector Search")
        for item in result['strategy_a_raw_vector_search']:
            print(f"- {item}")

        print("\nStrategy B - AI Enhanced Retrieval")
        for item in result['strategy_b_ai_enhanced']:
            print(f"- {item}")

    # Step 6: Save Results
    benchmark.save_results()


if __name__ == "__main__":
    main()