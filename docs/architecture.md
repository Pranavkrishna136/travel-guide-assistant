# Architecture

High-level components:

- Frontend: Streamlit application for user inputs and displaying itineraries
- Backend: Python code that orchestrates retrieval and generation
- RAG pipeline: Embeddings (SentenceTransformers) → Vector DB (FAISS) → Retriever → Prompting to LLM
- Storage: compressed travel guide documents (WikiVoyage, scraped reviews)

Flow
1. Preprocessing: scrape or collect travel source documents, split into chunks, compute embeddings, and store in FAISS.
2. Query: user provides destination and constraints; system forms a retrieval query.
3. Retrieve: the system fetches top-k relevant chunks from FAISS.
4. Generate: the retrieved context plus a prompt template are sent to the LLM to produce an itinerary.

Diagram (ASCII)

User -> Streamlit -> Backend -> Retriever -> FAISS
                             \-> LLM -> Response

Edge cases
- Missing coverage for a destination — fall back to top-level guides or provide a graceful message asking for more specificity.
- Long responses — paginate or summarize large itineraries.
