"""
Travel Guide Assistant - RAG-based itinerary generator.
"""

import os
import pickle
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from openai import OpenAI
from typing import List, Dict

class TravelAssistant:
    def __init__(self, index_dir: str = 'data/index', model_name: str = 'all-MiniLM-L6-v2'):
        self.index_dir = index_dir
        self.model_name = model_name
        self.model = SentenceTransformer(model_name)
        self.index = None
        self.documents = None
        self.client = None
        self.load_index()
    
    def load_index(self):
        """Load FAISS index and documents."""
        index_path = os.path.join(self.index_dir, 'index.faiss')
        docs_path = os.path.join(self.index_dir, 'documents.pkl')
        
        if os.path.exists(index_path) and os.path.exists(docs_path):
            self.index = faiss.read_index(index_path)
            with open(docs_path, 'rb') as f:
                self.documents = pickle.load(f)
        else:
            raise FileNotFoundError("Index not found. Run build_index.py first.")
    
    def set_openai_client(self, api_key: str):
        """Set OpenAI client."""
        self.client = OpenAI(api_key=api_key)
    
    def retrieve(self, query: str, top_k: int = 5) -> List[Dict]:
        """Retrieve top-k relevant documents."""
        query_embedding = self.model.encode([query])
        faiss.normalize_L2(query_embedding)
        distances, indices = self.index.search(query_embedding, top_k)
        
        results = []
        for dist, idx in zip(distances[0], indices[0]):
            if idx != -1:
                results.append({
                    'text': self.documents[idx]['text'],
                    'source': self.documents[idx]['source'],
                    'chunk_id': self.documents[idx]['chunk_id'],
                    'score': float(dist)
                })
        return results
    
    def generate_itinerary(self, destination: str, days: int, budget: float, preferences: str = "") -> str:
        """Generate itinerary using RAG."""
        query = f"Travel guide for {destination}: attractions, food, activities, budget around ${budget} for {days} days."
        retrieved = self.retrieve(query, top_k=10)
        
        context = "\n\n".join([doc['text'] for doc in retrieved])
        
        prompt = f"""
You are a travel assistant. Based on the following information about {destination}, create a {days}-day itinerary for a budget of approximately ${budget}.

Retrieved information:
{context}

Preferences: {preferences}

Please structure the itinerary day by day, including:
- Morning activities
- Afternoon activities
- Evening activities
- Estimated costs
- Transportation tips

Keep it realistic and balanced.
"""
        
        if not self.client:
            return "OpenAI client not set. Please provide API key."
        
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1500,
            temperature=0.7
        )
        
        return response.choices[0].message.content.strip()

def generate_itinerary(destination: str, days: int, budget: float, preferences: str = "", api_key: str = None) -> str:
    """Convenience function."""
    assistant = TravelAssistant()
    if api_key:
        assistant.set_openai_client(api_key)
    return assistant.generate_itinerary(destination, days, budget, preferences)