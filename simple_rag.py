"""Simplified RAG backend that avoids sentence-transformers threading issues"""
import json
import logging
import os
from pathlib import Path
import numpy as np
import faiss

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SimpleRAGBackend:
    def __init__(self, data_path=None):
        """Initialize without loading sentence-transformers on init"""
        logger.info("🚀 Initializing RAG Backend (deferred embeddings)...")
        
        # Load data
        if data_path is None:
            data_path = self._find_data_path()
        
        logger.info(f"✓ Using data file: {data_path}")
        with open(data_path, 'r') as f:
            self.data = json.load(f)
        
        self.destinations = self.data.get('destinations', [])
        logger.info(f"✓ Loaded {len(self.destinations)} destinations")
        
        self.model = None
        self.embeddings = None
        self.index = None
        self.chunks = None
        self.chunk_to_destination = None
    
    def _ensure_embeddings_loaded(self):
        """Lazy load embeddings only when needed"""
        if self.model is not None:
            return
        
        logger.info("Loading embedding model (first time)...")
        from sentence_transformers import SentenceTransformer
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        
        logger.info("📝 Building knowledge chunks...")
        self._build_chunks_and_embeddings()
        
        logger.info("🔨 Building FAISS index...")
        self._create_faiss_index()
        
        logger.info("✅ Embeddings loaded!")
    
    def _find_data_path(self):
        """Find destinations.json"""
        strategies = [
            lambda: os.environ.get('RAG_DATA_PATH'),
            lambda: str(Path(__file__).parent / 'rag_data' / 'destinations.json'),
            lambda: str(Path.cwd() / 'rag_data' / 'destinations.json'),
            lambda: str(Path.cwd() / 'Travel guide' / 'rag_data' / 'destinations.json'),
        ]
        
        for strategy in strategies:
            try:
                path = strategy()
                if path and os.path.exists(path):
                    return path
            except:
                pass
        
        raise FileNotFoundError(f"Could not find destinations.json")
    
    def _build_chunks_and_embeddings(self):
        """Build document chunks and embeddings"""
        self.chunks = []
        self.chunk_to_destination = []
        
        for dest in self.destinations:
            if dest.get('description'):
                self.chunks.append(dest['description'])
                self.chunk_to_destination.append(dest)
            
            for guide in dest.get('guides', []):
                self.chunks.append(guide)
                self.chunk_to_destination.append(dest)
            
            reviews_text = ' '.join([r.get('text', '') for r in dest.get('reviews', [])])
            if reviews_text:
                self.chunks.append(reviews_text)
                self.chunk_to_destination.append(dest)
            
            food_text = ' '.join(dest.get('food_near', []))
            transport_text = dest.get('transport', '')
            combined = f"{food_text} {transport_text}"
            if combined.strip():
                self.chunks.append(combined)
                self.chunk_to_destination.append(dest)
        
        logger.info(f"✓ Encoding {len(self.chunks)} chunks...")
        self.embeddings = self.model.encode(self.chunks, show_progress_bar=True)
        logger.info(f"✅ Created {len(self.chunks)} chunks")
    
    def _create_faiss_index(self):
        """Create FAISS index"""
        dimension = self.embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(self.embeddings.astype(np.float32))
        logger.info(f"✅ FAISS index created with {len(self.embeddings)} vectors")
    
    def semantic_search(self, query, top_k=5, filters=None):
        """Search destinations"""
        self._ensure_embeddings_loaded()
        
        query_embedding = self.model.encode(query, show_progress_bar=False)
        query_embedding = query_embedding.astype(np.float32).reshape(1, -1)
        
        distances, indices = self.index.search(query_embedding, top_k * 3)
        
        results = []
        seen_destinations = set()
        
        for i, idx in enumerate(indices[0]):
            if len(results) >= top_k:
                break
            
            dest = self.chunk_to_destination[idx]
            dest_id = dest['id']
            
            if dest_id in seen_destinations:
                continue
            
            distance = distances[0][i]
            score = 1 / (1 + distance)
            
            if score < 0.1:
                continue
            
            if filters:
                skip = False
                if 'budget' in filters and filters['budget']:
                    budget_list = filters['budget'] if isinstance(filters['budget'], list) else [filters['budget']]
                    if dest.get('budget') not in budget_list:
                        skip = True
                if 'category' in filters and filters['category']:
                    cat_list = filters['category'] if isinstance(filters['category'], list) else [filters['category']]
                    dest_cats = [c.strip() for c in dest.get('category', '').split(',')]
                    if not any(c in dest_cats for c in cat_list):
                        skip = True
                if skip:
                    continue
            
            results.append({
                'destination': dest,
                'score': score,
            })
            seen_destinations.add(dest_id)
        
        return results
    
    def travel_qna(self, question, top_k=3):
        """Answer questions"""
        results = self.semantic_search(question, top_k=top_k)
        
        if not results:
            return {
                'answer': "I don't have information about this topic.",
                'sources': []
            }
        
        destinations = [r['destination'] for r in results]
        dest_names = ', '.join([d['name'] for d in destinations])
        
        answer = f"Related destinations: {dest_names}."
        sources = [{'name': d['name'], 'city': d['city']} for d in destinations]
        
        return {'answer': answer, 'sources': sources}

# Global instance
_instance = None

def get_rag_backend():
    """Get RAG backend"""
    global _instance
    if _instance is None:
        _instance = SimpleRAGBackend()
    return _instance
