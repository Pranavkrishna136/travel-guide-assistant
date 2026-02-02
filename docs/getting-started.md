# Getting started

This page covers how to set up the project locally (dev environment), install dependencies, and run the demo.

Prerequisites
- Python 3.9+ (3.10 recommended)
- Git
- An OpenAI API key or credentials for your chosen LLM backend

Install

1. Clone the repository:

   git clone https://github.com/Pranavkrishna136/travel-guide-assistant.git

2. Create and activate a virtual environment (PowerShell):

   python -m venv .venv
   .\.venv\Scripts\Activate.ps1

3. Install project requirements (core project + docs):

   pip install -r requirements.txt

4. Set environment variables (example):

   $env:OPENAI_API_KEY = 'your_key_here'

Run locally

- To run the Streamlit demo (if present):

  streamlit run app.py

- To preview the docs locally using MkDocs:

  mkdocs serve

Troubleshooting
- If an import error occurs, confirm you installed the correct requirements file and that the virtual environment is active.
