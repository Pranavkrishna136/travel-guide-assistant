"""
Travel Guide Assistant - RAG-based itinerary generator with Global Coverage.
Supports all countries and states/regions worldwide.
"""

import os
import glob
from typing import List, Dict, Tuple
from global_destinations import (
    GLOBAL_DESTINATIONS, 
    get_all_countries, 
    get_states,
    search_destination,
    get_country_info
)
from state_attractions import (
    get_state_attractions,
    get_must_visit_spots,
    get_local_cuisine,
    get_accommodation_prices,
    get_activities,
    get_best_time,
    get_how_to_reach,
    get_culture_info
)

class TravelAssistant:
    def __init__(self, data_dir: str = 'data/raw'):
        self.data_dir = data_dir
        self.documents = {}
        self.client = None
        self.global_destinations = GLOBAL_DESTINATIONS
        self.load_documents()
        self.load_global_coverage()
    
    def load_documents(self):
        """Load travel guide documents from files."""
        for filepath in glob.glob(os.path.join(self.data_dir, '*.txt')):
            city_name = os.path.basename(filepath).replace('.txt', '').lower()
            
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                self.documents[city_name] = content
        
        # Sort for consistent ordering
        self.documents = dict(sorted(self.documents.items()))
        print(f"Loaded {len(self.documents)} local city guides")
    
    def load_global_coverage(self):
        """Load all countries and states from global database."""
        self.all_countries = get_all_countries()
        print(f"Loaded comprehensive global coverage: {len(self.all_countries)} countries with states/regions")
    
    def set_openai_client(self, api_key: str):
        """Set OpenAI client."""
        from openai import OpenAI
        self.client = OpenAI(api_key=api_key)
    
    def get_available_countries(self) -> List[str]:
        """Get all available countries."""
        return self.all_countries
    
    def get_available_states(self, country: str) -> List[str]:
        """Get all available states/regions for a country."""
        return get_states(country)
    
    def search_destination(self, query: str) -> List[Dict]:
        """Search for destinations by name."""
        return search_destination(query)
    
    def find_matching_destination(self, destination: str) -> Tuple[str, str]:
        """
        Find the best matching destination from global database.
        Returns (country, state/city) tuple.
        """
        destination_lower = destination.lower()
        
        # First check if it's in local documents
        if destination_lower in self.documents:
            return (destination, "")
        
        # Search global database
        search_results = self.search_destination(destination)
        if search_results:
            result = search_results[0]
            if result["type"] == "country":
                return (result["name"], "")
            else:  # state
                parts = result["name"].rsplit(", ", 1)
                return (parts[1], parts[0])
        
        # Partial match in documents
        for city in self.documents.keys():
            if city in destination_lower or destination_lower in city:
                return (city, "")
        
        # Default to first country if no match
        return (self.all_countries[0], "") if self.all_countries else (None, None)
    
    def retrieve(self, destination: str, state: str = "") -> str:
        """Retrieve travel guide for destination."""
        # First check local documents
        destination_lower = destination.lower()
        if destination_lower in self.documents:
            return self.documents[destination_lower]
        
        # Check global database
        country_info = get_country_info(destination)
        if country_info:
            description = country_info.get("description", "")
            region = country_info.get("region", "")
            states = country_info.get("states", [])
            
            content = f"""
# {destination} - Travel Guide

**Region:** {region}

## Overview
{description}

## Popular Destinations
{chr(10).join([f"- {state}" for state in states])}

## Travel Information
This comprehensive guide covers {destination} and includes information about its major destinations and attractions.

### Getting There
{destination} is accessible by air, rail, and road depending on its location and neighboring countries.

### Best Time to Visit
Most regions offer different seasonal attractions. Check specific state/city guides for detailed seasonal information.

### Culture & Local Customs
Each region in {destination} has unique cultural practices. Respect local traditions and customs.

### Food & Dining
From street food to fine dining, {destination} offers diverse culinary experiences reflecting its rich heritage.

### Accommodation
Various options available from budget hostels to luxury resorts in major cities and tourist destinations.

### Safety & Practical Information
Standard travel precautions apply. Check current travel advisories and local conditions before visiting.
"""
            return content
        
        return f"No travel data available for {destination}. Available countries: {', '.join(self.get_available_countries()[:20])}"
    
    def parse_preferences(self, preferences: str) -> Dict:
        """Parse preferences string into structured data."""
        prefs = {
            'activities': [],
            'travel_style': 'Moderate',
            'pace': 'Moderate'
        }
        
        if not preferences:
            return prefs
        
        lines = preferences.split('\n')
        for line in lines:
            if 'Travel Style:' in line:
                prefs['travel_style'] = line.split('Travel Style:')[1].strip()
            elif 'Pace:' in line:
                prefs['pace'] = line.split('Pace:')[1].strip()
            elif 'Activities:' in line:
                activities_str = line.split('Activities:')[1].strip()
                if activities_str and activities_str != 'Any':
                    prefs['activities'] = [a.strip() for a in activities_str.split(',')]
        
        return prefs
    
    def filter_attractions_by_preference(self, attractions: List[str], preferences: Dict) -> List[str]:
        """Filter attractions based on user preferences - always show all attractions, highlight matching ones."""
        # Always return ALL attractions - preferences don't filter, they just help curate
        # The must-visit spots should ALWAYS be shown regardless of preferences
        return attractions if attractions else []
    
    def filter_activities_by_preference(self, activities_list: List[str], preferences: Dict) -> List[str]:
        """Filter activities - always show all activities regardless of preferences."""
        # Always show all activities available at the destination
        return activities_list if activities_list else []
    
    def filter_cuisine_by_preference(self, cuisine_list: List[str], preferences: Dict) -> List[str]:
        """Filter cuisine based on user preferences."""
        if 'Food & Cuisine' not in preferences['activities']:
            # If food not selected, return 3-4 basic items
            return cuisine_list[:4] if cuisine_list else []
        # Return all if food is selected
        return cuisine_list
    
    def adjust_budget_by_style(self, travel_style: str, base_budget: float) -> Dict[str, float]:
        """Adjust budget allocation based on travel style."""
        budgets = {
            'Budget': {
                'accommodation': 0.30,  # 30% for budget travel
                'food': 0.25,
                'activities': 0.20,
                'transport': 0.15,
                'misc': 0.10
            },
            'Moderate': {
                'accommodation': 0.40,  # 40% standard
                'food': 0.25,
                'activities': 0.20,
                'transport': 0.10,
                'misc': 0.05
            },
            'Luxury': {
                'accommodation': 0.50,  # 50% for luxury
                'food': 0.25,
                'activities': 0.15,
                'transport': 0.05,
                'misc': 0.05
            }
        }
        
        style = travel_style if travel_style in budgets else 'Moderate'
        allocations = budgets[style]
        
        return {
            'accommodation': base_budget * allocations['accommodation'],
            'food': base_budget * allocations['food'],
            'activities': base_budget * allocations['activities'],
            'transport': base_budget * allocations['transport'],
            'misc': base_budget * allocations['misc']
        }
    
    def generate_demo_itinerary(self, destination: str, state: str, days: int, budget: float, preferences: str = "") -> str:
        """Generate a comprehensive itinerary with state-specific information and preference customization."""
        destination_display = f"{state}, {destination}" if state else destination
        
        # Parse preferences
        parsed_prefs = self.parse_preferences(preferences)
        travel_style = parsed_prefs['travel_style']
        pace = parsed_prefs['pace']
        activities_selected = parsed_prefs['activities']
        
        # Get state-specific attractions and information
        state_info = get_state_attractions(destination, state)
        must_visit = get_must_visit_spots(destination, state)
        cuisine = get_local_cuisine(destination, state)
        accommodation_prices = get_accommodation_prices(destination, state)
        activities = get_activities(destination, state)
        best_time = get_best_time(destination, state)
        how_to_reach = get_how_to_reach(destination, state)
        culture = get_culture_info(destination, state)
        
        # Filter based on preferences
        must_visit_filtered = self.filter_attractions_by_preference(must_visit, parsed_prefs)
        activities_filtered = self.filter_activities_by_preference(activities, parsed_prefs)
        cuisine_filtered = self.filter_cuisine_by_preference(cuisine, parsed_prefs)
        
        # Adjust budget based on travel style
        budget_breakdown = self.adjust_budget_by_style(travel_style, budget)
        accommodation_budget = budget_breakdown['accommodation']
        food_budget = budget_breakdown['food']
        activities_budget = budget_breakdown['activities']
        transport_budget = budget_breakdown['transport']
        misc_budget = budget_breakdown['misc']
        
        budget_per_day = budget / days
        accommodation_per_day = accommodation_budget / days
        food_per_day = food_budget / days
        activities_per_day = activities_budget / days
        transport_per_day = transport_budget / days
        misc_per_day = misc_budget / days
        
        # Start building the itinerary
        itinerary = f"""
# 🗺️ {destination_display} - {days} Day Itinerary

**Duration:** {days} days  
**Total Budget:** ₹{budget:,.0f}  
**Budget per Day:** ₹{budget_per_day:,.0f}  
**Travel Style:** {travel_style}  
**Pace:** {pace}  

---

## 📊 Budget Breakdown (Based on {travel_style} Travel)

| Category | Amount | Per Day |
|----------|--------|---------|
| 🏨 Accommodation | ₹{accommodation_budget:,.0f} ({int(budget_breakdown['accommodation']/budget*100)}%) | ₹{accommodation_per_day:,.0f} |
| 🍽️ Food & Dining | ₹{food_budget:,.0f} ({int(budget_breakdown['food']/budget*100)}%) | ₹{food_per_day:,.0f} |
| 🎫 Activities & Tickets | ₹{activities_budget:,.0f} ({int(budget_breakdown['activities']/budget*100)}%) | ₹{activities_per_day:,.0f} |
| 🚕 Transport & Travel | ₹{transport_budget:,.0f} ({int(budget_breakdown['transport']/budget*100)}%) | ₹{transport_per_day:,.0f} |
| 📱 Miscellaneous | ₹{misc_budget:,.0f} ({int(budget_breakdown['misc']/budget*100)}%) | ₹{misc_per_day:,.0f} |
| **TOTAL** | **₹{budget:,.0f}** | **₹{budget_per_day:,.0f}** |

---

## 🌟 About {destination_display}

### Best Time to Visit
{best_time}

### Culture & Heritage
{culture if culture else f"{destination} is a wonderful destination with rich cultural heritage and diverse attractions."}

### How to Reach
"""
        
        if how_to_reach:
            for transport_type, details in how_to_reach.items():
                itinerary += f"- **{transport_type.replace('_', ' ').title()}:** {details}\n"
        else:
            itinerary += "- Contact travel agent for detailed transportation information\n"
        
        itinerary += f"""
---

## 🎯 Must-Visit Spots

{chr(10).join([f"✓ {spot}" for spot in must_visit_filtered]) if must_visit_filtered else "Popular attractions in the area"}

---

## 🍜 Local Cuisine to Try"""
        
        if activities_selected and 'Food & Cuisine' in activities_selected:
            itinerary += f"\n\n{chr(10).join([f'• {dish}' for dish in cuisine_filtered]) if cuisine_filtered else 'Explore local food specialties'}"
        else:
            itinerary += "\n\n" + (f"{chr(10).join([f'• {dish}' for dish in cuisine_filtered[:3]])}" if cuisine_filtered else "Explore local food specialties")
        
        itinerary += f"""

---

## 🏨 Accommodation Options (Based on {travel_style} Budget)

"""
        
        # Recommend accommodation type based on travel style
        if travel_style == "Budget":
            itinerary += "| Type | Price Range | Recommendation |\n|------|-------------|----------------|\n"
            if accommodation_prices:
                itinerary += f"| Budget Hotels/Hostels | ₹{accommodation_per_day:,.0f}/night | Recommended for your budget |\n"
                if 'mid_range' in accommodation_prices:
                    itinerary += f"| Mid-range Guesthouses | {accommodation_prices.get('mid_range', 'Available')} | Optional upgrades |\n"
            else:
                itinerary += f"| Budget Accommodation | ₹{accommodation_per_day:,.0f}/night | Recommended |\n"
        elif travel_style == "Luxury":
            itinerary += "| Type | Price Range | Recommendation |\n|------|-------------|----------------|\n"
            if accommodation_prices:
                itinerary += f"| Luxury Hotels | {accommodation_prices.get('luxury', f'₹{accommodation_per_day:,.0f}+/night')} | Recommended for your budget |\n"
                itinerary += f"| Mid-range Options | {accommodation_prices.get('mid_range', 'Available')} | Budget-friendly alternative |\n"
            else:
                itinerary += f"| Premium Accommodation | ₹{accommodation_per_day:,.0f}+/night | Recommended |\n"
        else:
            itinerary += "| Type | Price Range | Examples |\n|------|-------------|----------|\n"
            if accommodation_prices:
                for acc_type, price in accommodation_prices.items():
                    acc_type_clean = acc_type.replace('_', ' ').title()
                    itinerary += f"| {acc_type_clean} | {price} | Hotels, Resorts, Guesthouses |\n"
            else:
                itinerary += "| Mid-range Hotels | Comfortable options | 3-4 star establishments |\n"
        
        itinerary += f"""
---

## 🎭 Popular Activities

{chr(10).join([f"• {activity}" for activity in activities_filtered]) if activities_filtered else "Various activities available"}

---

## 📅 {days}-Day Itinerary ({pace} Pace)

"""
        
        # Determine activities per day based on pace
        if pace == "Relaxed":
            activities_per_day_count = max(2, days // 3)  # Fewer activities
        elif pace == "Fast-paced":
            activities_per_day_count = days + 2  # More activities
        else:
            activities_per_day_count = days  # Moderate activities
        
        # Generate day-by-day detailed itinerary
        activities_list = activities_filtered if activities_filtered else ["Local exploration", "Monument visit", "Market visit", "Temple/cultural site"]
        must_visit_list = must_visit_filtered if must_visit_filtered else ["Main attraction"]
        
        for day in range(1, days + 1):
            # Select activities based on pace and day
            if pace == "Relaxed":
                day_activities = activities_list[day % len(activities_list):day % len(activities_list) + 1]
                morning_time = "8:00 AM - 11:00 AM (Slow start)"
                afternoon_time = "2:00 PM - 5:00 PM (Leisurely)"
                evening_time = "7:00 PM onwards (Evening at leisure)"
            elif pace == "Fast-paced":
                day_activities = activities_list[day % len(activities_list):min(day % len(activities_list) + 2, len(activities_list))]
                morning_time = "6:00 AM - 10:00 AM (Early start)"
                afternoon_time = "11:00 AM - 5:00 PM (Packed)"
                evening_time = "6:00 PM - 10:00 PM (Late evening activities)"
            else:  # Moderate
                day_activities = [activities_list[day % len(activities_list)]]
                morning_time = "7:00 AM - 11:00 AM"
                afternoon_time = "1:00 PM - 5:00 PM"
                evening_time = "6:00 PM - 9:00 PM"
            
            itinerary += f"""
### Day {day}

**Daily Budget:** ₹{budget_per_day:,.0f}

**Budget Allocation:**
- 🏨 Accommodation: ₹{accommodation_per_day:,.0f}
- 🍽️ Food: ₹{food_per_day:,.0f}
- 🎫 Activities: ₹{activities_per_day:,.0f}
- 🚕 Transport: ₹{transport_per_day:,.0f}
- 📱 Miscellaneous: ₹{misc_per_day:,.0f}

#### 🌅 Morning - {morning_time} (₹{budget_per_day * 0.25:,.0f})
"""
            
            if day == 1:
                itinerary += f"""- Arrive at {destination_display} & settle into accommodation
- Breakfast at {"budget-friendly local café" if travel_style == "Budget" else "hotel restaurant"} (₹{"200-400" if travel_style == "Budget" else "400-600"})
- Visit {must_visit_list[0] if must_visit_list else "main attraction"} or explore local area
- Estimated activity cost: ₹{activities_per_day * 0.3:,.0f}
"""
            else:
                main_activity = day_activities[0] if day_activities else "Local exploration"
                itinerary += f"""- {main_activity}
- Breakfast at {"budget café" if travel_style == "Budget" else "good restaurant"} (₹{"200-400" if travel_style == "Budget" else "500-700"})
- Start with {"nearby" if pace == "Relaxed" else ""} attraction or activity
- Estimated cost: ₹{activities_per_day * 0.3:,.0f}
"""
            
            itinerary += f"""
#### 🌤️ Afternoon - {afternoon_time} (₹{budget_per_day * 0.35:,.0f})
"""
            
            if day == 1:
                itinerary += f"""- Explore local market or shopping area
- Lunch at restaurant (₹{"400-700" if travel_style == "Budget" else "700-1200"})
- {"Visit additional major attraction" if pace == "Fast-paced" else "Rest and explore nearby"}
- Estimated activity cost: ₹{activities_per_day * 0.35:,.0f}
"""
            else:
                next_activity = day_activities[-1] if day_activities else "Cultural site"
                itinerary += f"""- {next_activity}
- Lunch at {"local eatery" if travel_style == "Budget" else "good restaurant"} (₹{"400-800" if travel_style == "Budget" else "800-1500"})
- {"Visit 2nd attraction" if pace == "Fast-paced" else "Rest at hotel or café"}
- Estimated cost: ₹{activities_per_day * 0.35:,.0f}
"""
            
            itinerary += f"""
#### 🌆 Evening - {evening_time} (₹{budget_per_day * 0.40:,.0f})
"""
            
            if pace == "Fast-paced":
                itinerary += f"""- {"Visit night market or local entertainment" if day < days else "Evening walk and reflection"}
- Dinner at {"budget restaurant" if travel_style == "Budget" else "nice restaurant"} (₹{"500-800" if travel_style == "Budget" else "900-1500"})
- {"Nightlife or evening activity" if "Nightlife" in activities_selected else "Evening exploration"}
- Snacks & beverages (₹{"150-300" if travel_style == "Budget" else "300-500"})
- Estimated cost: ₹{misc_per_day + food_per_day * 0.35:,.0f}
"""
            else:
                itinerary += f"""- Relax at accommodation or explore nearby areas
- Dinner at restaurant (₹{"400-700" if travel_style == "Budget" else "800-1300"})
- Evening walk or {"local entertainment" if "Nightlife" in activities_selected else "quiet exploration"}
- Snacks & beverages (₹{"100-200" if travel_style == "Budget" else "200-400"})
- Estimated cost: ₹{misc_per_day + food_per_day * 0.35:,.0f}
"""
            
            itinerary += "\n---\n"
        
        itinerary += f"""
## 💡 Travel Tips for {destination_display}

1. **Best Transportation:** Use local taxis, auto-rickshaws, or buses
2. **Money Matters:** ATMs widely available. Carry {"small cash for small purchases" if travel_style == "Budget" else "mix of cash and cards"}
3. **Packing:** Check weather; carry sunscreen, water bottle, comfortable shoes
4. **Language:** English spoken in tourist areas. Learn basic local greetings
5. **Safety:** Keep valuables safe, {"travel in groups at night" if "Nightlife" in activities_selected else "stay in well-lit areas"}
6. **Photography:** Ask permission before photographing people, especially at religious sites
7. **Dining:** Try {"street food for authentic taste" if "Food & Cuisine" in activities_selected else "local restaurants"}, visit local eateries
8. **Timing:** Check opening hours of attractions before visiting
9. **Pace:** {"Take it slow, enjoy local life at own pace" if pace == "Relaxed" else "Packed schedule, move quickly between attractions" if pace == "Fast-paced" else "Moderate pace, enjoy without rushing"}

## 📝 Important Notes

- This itinerary is customized based on your preferences: {", ".join(activities_selected) if activities_selected else "General"} activities, {travel_style} travel style, {pace} pace
- Prices are approximate in INR and may vary with season
- Book accommodations in advance during peak season
- Check weather conditions and local festivals before planning
- Keep emergency contact numbers handy
- Consider travel insurance for your trip
- Respect local customs and traditions
- Adjust itinerary based on weather and personal interests

## 🗺️ Quick Reference

**State:** {state}  
**Country:** {destination}  
**Duration:** {days} days  
**Total Budget:** ₹{budget:,.0f}  
**Travel Style:** {travel_style}  
**Pace:** {pace}  
**Interests:** {", ".join(activities_selected) if activities_selected else "General"}  
**Best Time:** {best_time}  

---

✨ **Have a wonderful {pace.lower()} trip to {destination_display}!** ✨

For more details, visit local tourism websites or contact local travel agencies.

"""
        
        return itinerary
    
    def generate_itinerary(self, destination: str, state: str = "", days: int = 3, budget: float = 50000, preferences: str = "", use_demo: bool = False) -> Tuple[str, bool]:
        """Generate itinerary using RAG. Returns (itinerary, is_demo)."""
        context = self.retrieve(destination, state)
        
        destination_display = f"{state}, {destination}" if state else destination
        
        prompt = f"""
You are a travel assistant. Based on the following information about {destination_display}, create a {days}-day itinerary for a budget of approximately ₹{budget:,.0f}.

Retrieved information:
{context}

Preferences: {preferences}

Please structure the itinerary day by day, including:
- Morning activities
- Afternoon activities
- Evening activities
- Estimated costs in INR
- Transportation tips

Keep it realistic and balanced.
"""
        
        if not self.client or use_demo:
            # Use demo mode if no client or explicitly requested
            demo_itinerary = self.generate_demo_itinerary(destination, state, days, budget, preferences)
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
                demo_itinerary = self.generate_demo_itinerary(destination, state, days, budget, preferences)
                return demo_itinerary, True
            else:
                raise

def generate_itinerary(destination: str, state: str = "", days: int = 3, budget: float = 50000, preferences: str = "", api_key: str = None, use_demo: bool = False) -> Tuple[str, bool]:
    """Convenience function. Returns (itinerary, is_demo)."""
    assistant = TravelAssistant()
    if api_key:
        assistant.set_openai_client(api_key)
    return assistant.generate_itinerary(destination, state, days, budget, preferences, use_demo)