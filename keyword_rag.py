"""Ultra-lightweight RAG using keyword matching only - no embeddings"""
import json
import logging
import os
from pathlib import Path
import re

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class KeywordRAGBackend:
    """RAG backend using keyword matching instead of embeddings"""
    
    def __init__(self, data_path=None):
        logger.info("🚀 Initializing Keyword-Based RAG Backend...")
        
        if data_path is None:
            data_path = self._find_data_path()
        
        logger.info(f"✓ Using data file: {data_path}")
        with open(data_path, 'r') as f:
            self.data = json.load(f)
        
        self.destinations = self.data.get('destinations', [])
        logger.info(f"✓ Loaded {len(self.destinations)} destinations")
        
        # Pre-build searchable content
        self._build_search_index()
        logger.info("✅ RAG Backend initialized!")
    
    def _find_data_path(self):
        strategies = [
            lambda: os.environ.get('RAG_DATA_PATH'),
            lambda: str(Path(__file__).parent / 'rag_data' / 'destinations.json'),
            lambda: str(Path.cwd() / 'rag_data' / 'destinations.json'),
        ]
        
        for strategy in strategies:
            try:
                path = strategy()
                if path and os.path.exists(path):
                    return path
            except:
                pass
        
        raise FileNotFoundError("Could not find destinations.json")
    
    def _build_search_index(self):
        """Create searchable text for each destination"""
        self.search_index = []
        
        for dest in self.destinations:
            # Combine all searchable text
            searchable = []
            searchable.append(dest.get('name', '').lower())
            searchable.append(dest.get('city', '').lower())
            searchable.append(dest.get('country', '').lower())
            searchable.append(dest.get('category', '').lower())
            searchable.append(dest.get('description', '').lower())
            searchable.extend([g.lower() for g in dest.get('guides', [])])
            searchable.extend([r.get('text', '').lower() for r in dest.get('reviews', [])])
            searchable.extend([f.lower() for f in dest.get('food_near', [])])
            searchable.append(dest.get('transport', '').lower())
            
            combined_text = ' '.join(searchable)
            self.search_index.append(combined_text)
    
    def _keyword_similarity(self, query, text):
        """Calculate keyword-based similarity score"""
        query_words = set(query.lower().split())
        text_words = set(text.split())
        
        if not query_words:
            return 0
        
        matches = query_words & text_words
        score = len(matches) / len(query_words)
        return score
    
    def semantic_search(self, query, top_k=5, filters=None):
        """Search using keyword matching"""
        if not query:
            return []
        
        # Calculate scores for each destination
        scores = []
        for i, dest in enumerate(self.destinations):
            text = self.search_index[i]
            score = self._keyword_similarity(query, text)
            scores.append((i, dest, score))
        
        # Sort by score
        scores.sort(key=lambda x: x[2], reverse=True)
        
        # Apply filters and collect results
        results = []
        seen = set()
        
        for i, dest, score in scores:
            if len(results) >= top_k:
                break
            
            dest_id = dest['id']
            if dest_id in seen:
                continue
            
            if score < 0.1:  # Skip very low scores
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
            })
            seen.add(dest_id)
        
        return results
    
    def travel_qna(self, question, top_k=3):
        """Answer questions"""
        results = self.semantic_search(question, top_k=top_k)
        
        if not results:
            return {
                'answer': "I don't have information about this topic. Try searching for specific destinations.",
                'sources': []
            }
        
        destinations = [r['destination'] for r in results]
        dest_names = ', '.join([d['name'] for d in destinations])
        
        answer = f"Based on our travel guide, I found these relevant destinations: {dest_names}. "
        answer += "Feel free to explore them using the search feature for more details!"
        
        sources = [{'name': d['name'], 'city': d['city']} for d in destinations]
        
        return {'answer': answer, 'sources': sources}

# Global instance
_instance = None

def get_rag_backend():
    global _instance
    if _instance is None:
        _instance = KeywordRAGBackend()
    return _instance
