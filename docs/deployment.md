# Deployment

This page describes how to deploy both the docs site and the app.

Docs (GitHub Pages via Actions)
- We provide a GitHub Actions workflow that builds MkDocs and deploys to `gh-pages` branch.

App deployment options
- Streamlit Cloud — easiest for Streamlit demos (free tier available)
- Vercel / Heroku / Railway — containerize app or use build packs

Example: GitHub Actions for docs (automatic)
- See `.github/workflows/deploy-docs.yml` (included in repo)

Environment variables
- OPENAI_API_KEY (or other provider keys)
- VECTOR_INDEX_PATH (optional)

Security
- Do not store API keys in the repo. Use GitHub Secrets for Actions.
