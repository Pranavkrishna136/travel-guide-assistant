"""Travel Guide RAG Backend using FAISS and Sentence Transformers"""
import json
import logging
import os
from pathlib import Path
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(name)s:%(message)s')
logger = logging.getLogger(__name__)

class TravelRAGBackend:
    def __init__(self, data_path=None):
        """Initialize the Travel Guide RAG Backend"""
        logger.info("🚀 Initializing Travel Guide RAG Backend...")
        
        # Load data
        if data_path is None:
            data_path = self._find_data_path()
        
        logger.info(f"✓ Using data file: {data_path}")
        with open(data_path, 'r') as f:
            self.data = json.load(f)
        
        self.destinations = self.data.get('destinations', [])
        logger.info(f"✓ Loaded {len(self.destinations)} destinations")
        
        # Load embedding model
        logger.info("Loading embedding model: all-MiniLM-L6-v2")
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        
        # Build chunks and embeddings
        logger.info("📝 Building knowledge chunks from destinations...")
        self._build_chunks_and_embeddings()
        
        # Create FAISS index
        logger.info("🔨 Building FAISS index for fast retrieval...")
        self._create_faiss_index()
        
        logger.info("✅ RAG Backend initialized successfully!")
    
    def _find_data_path(self):
        """Find destinations.json with multiple fallback strategies"""
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
        """Build document chunks from destinations and generate embeddings"""
        self.chunks = []
        self.chunk_to_destination = []
        
        for dest in self.destinations:
            # Description chunk
            if dest.get('description'):
                self.chunks.append(dest['description'])
                self.chunk_to_destination.append(dest)
            
            # Guides chunks
            for guide in dest.get('guides', []):
                self.chunks.append(guide)
                self.chunk_to_destination.append(dest)
            
            # Review summary chunk
            reviews_text = ' '.join([r.get('text', '') for r in dest.get('reviews', [])])
            if reviews_text:
                self.chunks.append(reviews_text)
                self.chunk_to_destination.append(dest)
            
            # Food/transport chunk
            food_text = ' '.join(dest.get('food_near', []))
            transport_text = dest.get('transport', '')
            combined = f"{food_text} {transport_text}"
            if combined.strip():
                self.chunks.append(combined)
                self.chunk_to_destination.append(dest)
        
        logger.info(f"✓ Generated embeddings for {len(self.chunks)} chunks...")
        self.embeddings = self.model.encode(self.chunks, show_progress_bar=True)
        logger.info(f"✅ Created {len(self.chunks)} chunks with embeddings")
    
    def _create_faiss_index(self):
        """Create FAISS index for similarity search"""
        dimension = self.embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(self.embeddings.astype(np.float32))
        logger.info(f"✅ FAISS index created with {len(self.embeddings)} vectors")
    
    def semantic_search(self, query, top_k=5, filters=None):
        """Search destinations using semantic similarity"""
        # Encode query
        query_embedding = self.model.encode(query, show_progress_bar=True)
        query_embedding = query_embedding.astype(np.float32).reshape(1, -1)
        
        # Search
        distances, indices = self.index.search(query_embedding, top_k * 3)  # Get more, filter later
        
        results = []
        seen_destinations = set()
        
        for i, idx in enumerate(indices[0]):
            if len(results) >= top_k:
                break
            
            dest = self.chunk_to_destination[idx]
            dest_id = dest['id']
            
            # Skip if already added
            if dest_id in seen_destinations:
                continue
            
            # Calculate similarity score
            distance = distances[0][i]
            score = 1 / (1 + distance)  # Convert L2 distance to similarity
            
            # Skip low score results
            if score < 0.1:
                continue
            
            # Apply filters
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
                'chunk_index': idx
            })
            seen_destinations.add(dest_id)
        
        return results
    
    def travel_qna(self, question, top_k=3):
        """Answer travel questions with source citations"""
        results = self.semantic_search(question, top_k=top_k)
        
        if not results:
            return {
                'answer': "I don't have information about this topic. Try asking about specific destinations or features.",
                'sources': []
            }
        
        # Simple answer generation
        destinations = [r['destination'] for r in results]
        dest_names = ', '.join([d['name'] for d in destinations])
        
        answer = f"Based on the travel guide, here are relevant destinations: {dest_names}. "
        answer += f"You might also find helpful information in their reviews, guides, and nearby food options."
        
        sources = [{'name': d['name'], 'city': d['city']} for d in destinations]
        
        return {'answer': answer, 'sources': sources}
    
    def personalized_itinerary(self, preferences):
        """Generate personalized travel itineraries"""
        budget = preferences.get('budget', 'budget')
        interests = preferences.get('interests', [])
        duration = preferences.get('duration', 3)
        
        # Find matching destinations
        query = ' '.join(interests) if interests else "popular tourist destination"
        results = self.semantic_search(
            query, 
            top_k=10,
            filters={'budget': budget} if budget else None
        )
        
        itinerary = {
            'title': f"{duration}-Day {budget.title()} Travel Plan",
            'budget': budget,
            'duration_days': duration,
            'days': []
        }
        
        destinations = [r['destination'] for r in results[:max(1, duration // 2)]]
        
        for day in range(1, duration + 1):
            if day <= len(destinations):
                dest = destinations[day - 1]
                itinerary['days'].append({
                    'day': day,
                    'destination': dest['name'],
                    'activities': dest.get('guides', ['Visit main attractions'])[:2],
                    'meals': dest.get('food_near', ['Local cuisine'])[:2],
                    'estimated_cost': f"₹{500 * day}"
                })
            else:
                itinerary['days'].append({
                    'day': day,
                    'destination': 'Leisure day',
                    'activities': ['Rest and explore local markets'],
                    'meals': ['Local specialty'],
                    'estimated_cost': f"₹500"
                })
        
        return itinerary
    
    def review_aware_recommendations(self, destination_id):
        """Get recommendations based on destination reviews"""
        dest = next((d for d in self.destinations if d['id'] == destination_id), None)
        
        if not dest:
            return None
        
        reviews = dest.get('reviews', [])
        avg_rating = sum(r.get('rating', 0) for r in reviews) / len(reviews) if reviews else 0
        
        recommendations = {
            'destination': dest['name'],
            'average_rating': avg_rating,
            'reviews': reviews,
            'highlights': [g for g in dest.get('guides', [])[:3]],
            'nearby_food': dest.get('food_near', []),
            'transport': dest.get('transport', 'Not specified'),
        }
        
        return recommendations

# Global instance
_rag_instance = None

def get_rag_backend():
    """Get or create the RAG backend singleton"""
    global _rag_instance
    if _rag_instance is None:
        _rag_instance = TravelRAGBackend()
    return _rag_instance
