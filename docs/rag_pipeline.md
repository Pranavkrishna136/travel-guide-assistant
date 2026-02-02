# RAG Pipeline

This document explains how the Retrieval-Augmented Generation pipeline is implemented and how to reproduce the index.

1) Data collection
- Sources: WikiVoyage, curated travel reviews, local datasets
- Store raw documents under `data/raw` (not included in repo)

2) Preprocessing
- Split documents into chunks (200-500 tokens) with overlap to preserve context
- Clean text (remove HTML, normalize whitespace)

3) Embeddings
- Model: sentence-transformers (e.g., all-MiniLM-L6-v2) for a good speed/quality balance
- Compute embeddings for each chunk and store them with metadata (source, title, chunk_id)

4) Vector store
- FAISS index for local fast nearest-neighbor retrieval
- Persist index artifacts under `data/index`

5) Retrieval and prompt design
- Retrieve top-k (typically 5-10) chunks
- Build a prompt that includes: system instruction, retrieved context (with citations), user constraints, and a templated prompt for itinerary structure.

6) LLM generation
- Use OpenAI or Hugging Face LLM to generate the itinerary. Limit output length and include follow-up instructions for clarifications.

Re-indexing
- Provide a script `scripts/build_index.py` (or similar) that takes raw data path → tokenizes → computes embeddings → writes faiss index.

Security and cost considerations
- Store API keys in environment variables
- Cache repeated queries to reduce costs
