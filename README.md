# Teleport_Rag_Assignment

# Semantic RAG & Vector Search Assignment

## Overview

This project implements a local Retrieval-Augmented Generation (RAG) pipeline using:

* sentence-transformers
* FAISS vector database
* semantic search
* mocked AI query expansion
* retrieval benchmarking

The project compares two retrieval strategies:

1. Strategy A — Raw Vector Search
2. Strategy B — AI Enhanced Retrieval

The implementation demonstrates:

* document ingestion
* embedding generation
* vector similarity search
* semantic retrieval
* query expansion
* benchmarking and evaluation

---

# Technologies Used

* Python
* sentence-transformers
* FAISS
* NumPy
* Pytest

---

# Project Structure

```bash
Teleport_Rag_Assignment/
│
├── data/
│   ├── __init__.py
│   └── documents.py
│
├── src/
│   ├── __init__.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── query_expander.py
│   ├── retriever.py
│   └── benchmark.py
│
├── tests/
│   ├── __init__.py
│   ├── test_embeddings.py
│   ├── test_query_expansion.py
│   └── test_retrieval.py
│
├── benchmark_results.json
├── retrieval_benchmark.md
├── requirements.txt
├── README.md
└── main.py
```

---

# How the System Works

## Step 1 — Document Ingestion

Technical documents are stored inside:

```bash
data/documents.py
```

These documents act as the knowledge base for semantic retrieval.

---

## Step 2 — Embedding Generation

The project uses:

```python
SentenceTransformer("all-MiniLM-L6-v2")
```

to generate vector embeddings for all documents.

File:

```bash
src/embeddings.py
```

---

## Step 3 — Vector Storage

Generated embeddings are stored in a FAISS vector index.

File:

```bash
src/vector_store.py
```

FAISS performs similarity search using Euclidean distance (L2).

---

## Step 4 — Retrieval Strategies

### Strategy A — Raw Vector Search

Flow:

```text
User Query
   ↓
Embedding Generation
   ↓
FAISS Similarity Search
   ↓
Top 3 Results
```

---

### Strategy B — AI Enhanced Retrieval

Flow:

```text
User Query
   ↓
Mock Query Expansion
   ↓
Expanded Query
   ↓
Embedding Generation
   ↓
FAISS Similarity Search
   ↓
Top 3 Results
```

The query expansion simulates a Generative AI model by rewriting the user query into a more embedding-friendly semantic format.

File:

```bash
src/query_expander.py
```

---

# Benchmarking

The benchmark compares retrieval quality between:

* Raw Vector Search
* AI Enhanced Retrieval

The benchmark runs on 3 complex queries.

File:

```bash
src/benchmark.py
```

Output files:

* benchmark_results.json
* retrieval_benchmark.md

---

# Installation

## Step 1 — Create Virtual Environment

```bash
python -m venv venv
```

---

## Step 2 — Activate Virtual Environment

### Mac/Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\\Scripts\\activate
```

---

## Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

---

# How To Run The Project

Run:

```bash
python main.py
```

This will:

1. Load documents
2. Generate embeddings
3. Store vectors in FAISS
4. Execute both retrieval strategies
5. Compare benchmark results
6. Save benchmark_results.json

---

# Expected Output

```bash
================================================================================
Query: How does the system handle peak load?

Strategy A - Raw Vector Search
- The platform uses autoscaling to handle peak traffic loads.
- Load balancing distributes incoming requests evenly.
- Monitoring systems continuously track server health.

Strategy B - AI Enhanced Retrieval
- The platform uses autoscaling to handle peak traffic loads.
- Load balancing distributes incoming requests evenly.
- Caching mechanisms reduce repeated database queries.
```

---

# Running Tests

Run:

```bash
python -m pytest
```

Expected Output:

```bash
============================= test session starts =============================

collected 3 items

tests/test_embeddings.py .
tests/test_query_expansion.py .
tests/test_retrieval.py .

============================= 3 passed =============================
```

---

# Similarity Metric Choice

This implementation uses Euclidean Distance (L2) through FAISS IndexFlatL2.

Why Euclidean Distance?

* Simple implementation
* Efficient local experimentation
* Native FAISS support
* Suitable for semantic vector retrieval

---

# Cosine Similarity vs Euclidean Distance

## Cosine Similarity

* Measures angular similarity between vectors
* Commonly used for semantic embeddings
* Better for normalized embeddings

## Euclidean Distance

* Measures geometric distance between vectors
* Faster and simpler for local experimentation
* Supported directly in FAISS IndexFlatL2

---

# Migration to Vertex AI Vector Search

To migrate this solution into production using Google Cloud Vertex AI:

1. Replace sentence-transformers with Vertex AI Embedding API
2. Replace FAISS with Vertex AI Matching Engine
3. Store embeddings inside Vertex AI Vector Search indexes
4. Deploy scalable retrieval endpoints
5. Replace mocked query expansion with Gemini or Vertex AI Generative Models

---

# Assignment Requirements Covered

1. Local RAG pipeline

2. Embedding generation

3. Semantic search

4. FAISS vector database

5. Query expansion

6. Mocked AI model

7. Benchmark comparison

8. Pytest testing

9. Retrieval report

10. Similarity metric explanation

11. Vertex AI migration explanation

---
