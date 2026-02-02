#!/usr/bin/env python3
"""
Build FAISS index for travel guide data.
"""

import os
import glob
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle

def load_documents(data_dir):
    """Load all text documents from data_dir."""
    documents = []
    for filepath in glob.glob(os.path.join(data_dir, '**', '*.txt'), recursive=True):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            # Split into chunks (simple: by paragraphs)
            chunks = [chunk.strip() for chunk in content.split('\n\n') if chunk.strip()]
            for i, chunk in enumerate(chunks):
                documents.append({
                    'text': chunk,
                    'source': filepath,
                    'chunk_id': i
                })
    return documents

def build_index(documents, model_name='all-MiniLM-L6-v2'):
    """Build FAISS index from documents."""
    print("Loading model...")
    model = SentenceTransformer(model_name, cache_folder=os.path.expanduser('~/.cache/sentence-transformers'))
    texts = [doc['text'] for doc in documents]
    print("Encoding documents to embeddings...")
    embeddings = model.encode(texts, show_progress_bar=True)
    
    # Create FAISS index
    dimension = embeddings.shape[1]
    print(f"Creating FAISS index with {dimension} dimensions...")
    index = faiss.IndexFlatIP(dimension)  # Inner product for cosine similarity
    faiss.normalize_L2(embeddings)  # Normalize for cosine
    index.add(embeddings)
    print(f"Added {len(embeddings)} embeddings to index.")
    
    return index, embeddings, model

def save_index(index, documents, embeddings, output_dir):
    """Save index and metadata."""
    os.makedirs(output_dir, exist_ok=True)
    
    # Save FAISS index
    faiss.write_index(index, os.path.join(output_dir, 'index.faiss'))
    
    # Save documents metadata
    with open(os.path.join(output_dir, 'documents.pkl'), 'wb') as f:
        pickle.dump(documents, f)
    
    # Save embeddings (optional, for inspection)
    np.save(os.path.join(output_dir, 'embeddings.npy'), embeddings)

if __name__ == '__main__':
    data_dir = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw')
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'data', 'index')
    
    print("Loading documents...")
    documents = load_documents(data_dir)
    print(f"Loaded {len(documents)} chunks.")
    
    print("Building index...")
    index, embeddings, model = build_index(documents)
    
    print("Saving index...")
    save_index(index, documents, embeddings, output_dir)
    
    print("Index built successfully!")