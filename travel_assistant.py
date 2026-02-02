"""
Travel Guide Assistant - RAG-based itinerary generator (Simplified Version).
"""

import os
import glob
from typing import List, Dict, Tuple

class TravelAssistant:
    def __init__(self, data_dir: str = 'data/raw'):
        self.data_dir = data_dir
        self.documents = {}
        self.client = None
        self.load_documents()
    
    def load_documents(self):
        """Load all travel guide documents."""
        for filepath in glob.glob(os.path.join(self.data_dir, '*.txt')):
            city_name = os.path.basename(filepath).replace('.txt', '').lower()
            
            # Skip extended/culture/duplicates - keep main versions only
            if city_name.endswith(('_extended', '_culture')):
                continue
            
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                self.documents[city_name] = content
        
        # Sort for consistent ordering
        self.documents = dict(sorted(self.documents.items()))
        print(f"Loaded {len(self.documents)} unique city guides: {list(self.documents.keys())}")
    
    def set_openai_client(self, api_key: str):
        """Set OpenAI client."""
        from openai import OpenAI
        self.client = OpenAI(api_key=api_key)
    
    def find_matching_city(self, destination: str) -> str:
        """Find the best matching city from available documents."""
        destination_lower = destination.lower()
        
        # Exact match
        if destination_lower in self.documents:
            return destination_lower
        
        # Partial match
        for city in self.documents.keys():
            if city in destination_lower or destination_lower in city:
                return city
        
        # Return first available if no match
        return list(self.documents.keys())[0] if self.documents else None
    
    def retrieve(self, destination: str) -> str:
        """Retrieve travel guide for destination."""
        city = self.find_matching_city(destination)
        if not city:
            return f"No travel data available. Available cities: {', '.join(self.documents.keys())}"
        return self.documents[city]
    
    def generate_demo_itinerary(self, destination: str, days: int, budget: float, preferences: str = "") -> str:
        """Generate a demo itinerary from retrieved data without using API."""
        context = self.retrieve(destination)
        city = self.find_matching_city(destination)
        
        # Generate demo itinerary based on retrieved context
        demo_itinerary = f"""
# 🗺️ {destination} - {days} Day Itinerary (Demo Mode)

**Budget:** ${budget}  
**Travel Style:** {preferences.split('Travel Style: ')[1].split('\\n')[0] if 'Travel Style:' in preferences else 'Flexible'}  

---

## Travel Information

Based on available travel data:

{context}

---

## Daily Schedule

"""
        
        # Generate day-by-day structure
        budget_per_day = budget / days
        for day in range(1, days + 1):
            demo_itinerary += f"""
### Day {day}

**Budget for today:** ${budget_per_day:.2f}

#### Morning
- Start with a local breakfast or café
- Visit main attractions or museums in the area
- Estimated cost: ${budget_per_day * 0.3:.2f}

#### Afternoon  
- Continue exploring cultural sites or natural landmarks
- Lunch at a recommended local restaurant
- Estimated cost: ${budget_per_day * 0.35:.2f}

#### Evening
- Dinner at a local establishment
- Evening stroll or local entertainment
- Estimated cost: ${budget_per_day * 0.35:.2f}

---
"""
        
        demo_itinerary += """
## Notes

⚠️ **This is a DEMO itinerary** generated from available travel data.

**To generate AI-powered personalized itineraries:**
1. Ensure your OpenAI API key has active credits
2. Check your billing at https://platform.openai.com/account/billing/overview
3. If on free trial, you may need to add a payment method

**Demo mode sources:** Local travel guides in the database

---
"""
        return demo_itinerary
    
    def generate_itinerary(self, destination: str, days: int, budget: float, preferences: str = "", use_demo: bool = False) -> Tuple[str, bool]:
        """Generate itinerary using RAG. Returns (itinerary, is_demo)."""
        context = self.retrieve(destination)
        
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
        
        if not self.client or use_demo:
            # Use demo mode if no client or explicitly requested
            demo_itinerary = self.generate_demo_itinerary(destination, days, budget, preferences)
            return demo_itinerary, True
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=1500,
                temperature=0.7
            )
            return response.choices[0].message.content.strip(), False
        except Exception as e:
            # Fallback to demo mode on API error
            if "insufficient_quota" in str(e) or "429" in str(e):
                demo_itinerary = self.generate_demo_itinerary(destination, days, budget, preferences)
                return demo_itinerary, True
            else:
                raise

def generate_itinerary(destination: str, days: int, budget: float, preferences: str = "", api_key: str = None, use_demo: bool = False) -> Tuple[str, bool]:
    """Convenience function. Returns (itinerary, is_demo)."""
    assistant = TravelAssistant()
    if api_key:
        assistant.set_openai_client(api_key)
    return assistant.generate_itinerary(destination, days, budget, preferences, use_demo)