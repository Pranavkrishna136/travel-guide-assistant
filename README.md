# Travel Guide Assistant

An AI-powered travel assistant that generates personalized itineraries using a Retrieval-Augmented Generation (RAG) pipeline.

Project status
- README and project README: completed
- Documentation site: scaffolded with MkDocs (`mkdocs.yml` + `docs/` pages)

Docs preview
- To preview docs locally:

  mkdocs serve

- After you push to GitHub, the docs will be deployed via GitHub Actions to GitHub Pages. Expected docs URL:

  https://Pranavkrishna136.github.io/travel-guide-assistant/

What I added locally
- `mkdocs.yml` — MkDocs configuration
- `docs/` — documentation pages (index, getting-started, usage, architecture, rag_pipeline, data_sources, creative_feature, deployment, contributing)
- `.github/workflows/deploy-docs.yml` — action to build and publish the docs
- `requirements.txt` — dependencies for building docs

Next recommended steps
1. Commit and push these files to your GitHub repo (main branch). The GitHub Actions workflow will run and deploy the docs to the above URL.
2. Add `scripts/build_index.py` (I can scaffold this) and sample `data/` so users can reproduce the FAISS index.
3. Implement the Itinerary Composer feature in the Streamlit app (I can implement a minimal version and docs).
4. Draft a LinkedIn post announcing the project and docs (I can prepare a short post and images/screenshots if you provide them).

If you'd like, I can scaffold the indexing script and the minimal itinerary-composer UI next.
