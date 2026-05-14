# src/benchmark.py

import json


class Benchmark:
    def __init__(self, retriever):
        self.retriever = retriever

    def run(self):

        queries = [
            "How does the system handle peak load?",
            "How are services protected from too many requests?",
            "How does the system recover from failures?"
        ]

        benchmark_results = []

        for query in queries:
            raw_results = self.retriever.retrieve_raw(query)
            enhanced_results = self.retriever.retrieve_enhanced(query)

            benchmark_results.append({
                "query": query,
                "strategy_a_raw_vector_search": raw_results,
                "strategy_b_ai_enhanced": enhanced_results
            })

        return benchmark_results

    def save_results(self, filename="benchmark_results.json"):
        results = self.run()

        with open(filename, "w") as file:
            json.dump(results, file, indent=4)

        print(f"Benchmark results saved to {filename}")