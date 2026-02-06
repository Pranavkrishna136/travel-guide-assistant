# API Usage Examples - Global Travel Guide Assistant

This document demonstrates how to use the Travel Guide Assistant API programmatically.

## Quick Start

```python
from travel_assistant import TravelAssistant
from global_destinations import get_all_countries, get_states, search_destination

# Initialize
assistant = TravelAssistant()

# Get list of countries
countries = assistant.get_available_countries()
print(f"Total countries: {len(countries)}")

# Get states for a country
states = assistant.get_available_states('India')
print(f"States in India: {states}")

# Generate itinerary
destination = "India"
state = "Mumbai"
itinerary, is_demo = assistant.generate_itinerary(
    destination=destination,
    state=state,
    days=5,
    budget=50000,
    preferences="Activities: Food & Cuisine, Shopping"
)
print(itinerary)
```

## Core Functions

### 1. Get All Countries

```python
from global_destinations import get_all_countries

countries = get_all_countries()
print(countries[:10])
# Output: ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', ...]
print(f"Total: {len(countries)}")
# Output: Total: 193
```

### 2. Get States/Regions for a Country

```python
from global_destinations import get_states

# Get states for different countries
usa_states = get_states('United States')
print(f"USA states: {usa_states}")
# Output: USA states: ['New York', 'Los Angeles', 'Chicago', ...]

india_states = get_states('India')
print(f"India states: {india_states}")
# Output: India states: ['Delhi', 'Mumbai', 'Bangalore', 'Kolkata', 'Chennai', ...]

france_states = get_states('France')
print(f"France cities: {france_states}")
# Output: France cities: ['Paris', 'Lyon', 'Marseille', 'Toulouse', 'Nice', ...]
```

### 3. Get Country Information

```python
from global_destinations import get_country_info

japan_info = get_country_info('Japan')
print(f"Region: {japan_info['region']}")
print(f"Description: {japan_info['description']}")
print(f"States/Cities: {japan_info['states']}")
# Output:
# Region: Asia
# Description: East Asian island nation with ancient temples and modern technology
# States/Cities: ['Tokyo', 'Osaka', 'Kyoto', 'Hiroshima', 'Yokohama', 'Hokkaido', 'Mount Fuji']
```

### 4. Search Destinations

```python
from global_destinations import search_destination

# Search by city
results = search_destination('Paris')
for result in results:
    print(f"Type: {result['type']}, Name: {result['name']}")
# Output:
# Type: state, Name: Paris, France

# Search by country
results = search_destination('Japan')
for result in results:
    print(f"Type: {result['type']}, Name: {result['name']}")
# Output:
# Type: country, Name: Japan

# Partial search
results = search_destination('New')
for result in results:
    print(f"{result['name']}")
# Output:
# New York, United States
# New Zealand
# New Delhi, India
```

### 5. Get Destinations by Region

```python
from global_destinations import get_destinations_by_region, get_all_regions

# Get all regions
regions = get_all_regions()
print(f"Regions: {regions}")
# Output: Regions: ['Africa', 'Asia', 'Europe', 'North America', 'Oceania', 'South America']

# Get all countries in a region
asia_countries = get_destinations_by_region('Europe')
print(f"European countries: {list(asia_countries.keys())}")
# Output: European countries: ['Albania', 'Andorra', 'Austria', 'Belarus', ...]
```

## TravelAssistant Class

### Initialize Assistant

```python
from travel_assistant import TravelAssistant

# Basic initialization
assistant = TravelAssistant()

# With custom data directory
assistant = TravelAssistant(data_dir='custom_data/raw')

# Set OpenAI API key
assistant.set_openai_client('your-api-key-here')
```

### Get Available Destinations

```python
# Get all countries
countries = assistant.get_available_countries()
print(f"Available countries: {len(countries)}")

# Get states for specific country
states = assistant.get_available_states('Thailand')
print(f"Thailand destinations: {states}")
# Output: Thailand destinations: ['Bangkok', 'Chiang Mai', 'Phuket', 'Krabi', 'Pattaya']
```

### Search Destinations

```python
# Search for destinations
results = assistant.search_destination('Barcelona')
if results:
    for result in results:
        if result['type'] == 'state':
            print(f"Found: {result['name']}")
        # Output: Found: Barcelona, Spain
```

### Retrieve Travel Information

```python
# Get travel information for a destination
info = assistant.retrieve(destination='Thailand', state='Bangkok')
print(info)
# Output: Comprehensive travel guide for Bangkok, Thailand

# Get info for country only
info = assistant.retrieve(destination='France')
print(info)
# Output: Comprehensive travel guide for France
```

### Generate Itineraries

```python
# Generate demo itinerary (no API needed)
itinerary, is_demo = assistant.generate_itinerary(
    destination='Japan',
    state='Tokyo',
    days=5,
    budget=100000,
    preferences='Activities: Culture, Food & Cuisine\nTravel Style: Moderate'
)
print(itinerary)
print(f"Demo mode: {is_demo}")

# Generate with OpenAI API (requires valid API key and credits)
assistant.set_openai_client('sk-...')
itinerary, is_demo = assistant.generate_itinerary(
    destination='Italy',
    state='Rome',
    days=3,
    budget=50000,
    preferences='Activities: Historical Sites, Food & Cuisine'
)
print(itinerary)
```

## Practical Examples

### Example 1: Plan a Multi-Destination Trip

```python
from travel_assistant import TravelAssistant

assistant = TravelAssistant()

# Plan trips to multiple destinations
destinations = [
    ('Thailand', 'Bangkok', 3),
    ('Vietnam', 'Hanoi', 3),
    ('Cambodia', 'Siem Reap', 2)
]

for country, state, days in destinations:
    itinerary, _ = assistant.generate_itinerary(
        destination=country,
        state=state,
        days=days,
        budget=30000
    )
    with open(f'{state}_itinerary.txt', 'w') as f:
        f.write(itinerary)
    print(f"✅ Generated {state} itinerary")
```

### Example 2: Explore All Regions of a Country

```python
from travel_assistant import TravelAssistant

assistant = TravelAssistant()
country = 'India'

# Get all states in India
states = assistant.get_available_states(country)

# Generate quick info for each
for state in states:
    info = assistant.retrieve(country, state)
    print(f"\n--- {state} ---")
    print(info[:200] + "...")  # First 200 chars
```

### Example 3: Budget Travel Planning

```python
from travel_assistant import TravelAssistant

assistant = TravelAssistant()

# Search for budget destinations
budget = 25000

# Different regions
regions = {
    'Southeast Asia': [('Thailand', 'Bangkok'), ('Vietnam', 'Hanoi')],
    'South Asia': [('India', 'Delhi'), ('Nepal', 'Kathmandu')],
    'Europe': [('Hungary', 'Budapest'), ('Poland', 'Warsaw')]
}

for region_name, destinations in regions.items():
    print(f"\n### {region_name} ###")
    for country, state in destinations:
        itinerary, _ = assistant.generate_itinerary(
            destination=country,
            state=state,
            days=5,
            budget=budget
        )
        # Extract first day from itinerary for preview
        first_day = itinerary.split('### Day 2')[0]
        print(f"{state}: Estimated within ₹{budget}")
```

### Example 4: Activity-Based Travel Search

```python
from travel_assistant import TravelAssistant

assistant = TravelAssistant()

# Adventure destinations
adventure_destinations = [
    ('Nepal', 'Everest Region'),
    ('Peru', 'Cusco'),
    ('New Zealand', 'Queenstown'),
    ('Switzerland', 'Interlaken')
]

preferences = "Activities: Adventure Sports, Outdoor & Nature"

for country, state in adventure_destinations:
    itinerary, _ = assistant.generate_itinerary(
        destination=country,
        state=state,
        days=7,
        budget=100000,
        preferences=preferences
    )
    print(f"✅ {state}, {country} - Adventure itinerary ready")
```

### Example 5: Food Tourism Planner

```python
from travel_assistant import TravelAssistant

assistant = TravelAssistant()

# Food tourism destinations
food_destinations = [
    ('France', 'Paris'),
    ('Italy', 'Rome'),
    ('Thailand', 'Bangkok'),
    ('India', 'Delhi'),
    ('Japan', 'Tokyo')
]

preferences = "Activities: Food & Cuisine, Photography"

for country, state in food_destinations:
    itinerary, _ = assistant.generate_itinerary(
        destination=country,
        state=state,
        days=4,
        budget=60000,
        preferences=preferences
    )
    # Process itinerary (save, display, etc.)
    print(f"📍 {state}: Food tour ready")
```

## Advanced Usage

### Custom Destination Filtering

```python
from global_destinations import GLOBAL_DESTINATIONS

# Find all countries with more than 10 states
countries_with_many_states = {
    country: data for country, data in GLOBAL_DESTINATIONS.items()
    if len(data.get('states', [])) > 10
}

print(f"Countries with many states: {list(countries_with_many_states.keys())}")
```

### Regional Statistics

```python
from global_destinations import GLOBAL_DESTINATIONS, get_all_regions

# Count destinations by region
region_stats = {}
for region in get_all_regions():
    count = len([c for c, d in GLOBAL_DESTINATIONS.items() if d.get('region') == region])
    region_stats[region] = count

for region, count in sorted(region_stats.items(), key=lambda x: x[1], reverse=True):
    print(f"{region}: {count} countries")
```

### Batch Processing

```python
from travel_assistant import TravelAssistant
import json

assistant = TravelAssistant()

# Generate itineraries for top tourist destinations
top_destinations = [
    ('Thailand', 'Bangkok'),
    ('France', 'Paris'),
    ('Japan', 'Tokyo'),
    ('Italy', 'Rome'),
    ('Spain', 'Barcelona')
]

results = []
for country, state in top_destinations:
    itinerary, is_demo = assistant.generate_itinerary(
        destination=country,
        state=state,
        days=5,
        budget=100000
    )
    results.append({
        'destination': f"{state}, {country}",
        'itinerary': itinerary,
        'mode': 'demo' if is_demo else 'ai'
    })

# Save to JSON
with open('itineraries.json', 'w') as f:
    json.dump(results, f, indent=2)
```

## Error Handling

```python
from travel_assistant import TravelAssistant
from global_destinations import search_destination

assistant = TravelAssistant()

# Handle invalid country
try:
    states = assistant.get_available_states('InvalidCountry')
    if not states:
        print("No states found, checking if it's a valid country...")
        countries = assistant.get_available_countries()
        if 'InvalidCountry' not in countries:
            print("Country not found in database")
except Exception as e:
    print(f"Error: {e}")

# Handle search with no results
results = search_destination('XYZ')
if not results:
    print("No destinations found. Try a different search term.")
else:
    for result in results:
        print(f"Found: {result['name']}")
```

## Performance Tips

```python
from travel_assistant import TravelAssistant

# Initialize once and reuse
assistant = TravelAssistant()  # Load once

# Cache results
countries = assistant.get_available_countries()  # Fast (in-memory)
states = assistant.get_available_states('India')  # Fast (dictionary lookup)

# Batch operations are faster than individual calls
destinations = [
    ('India', 'Delhi'),
    ('India', 'Mumbai'),
    ('India', 'Bangalore')
]

# Better than calling separately
for country, state in destinations:
    itinerary, _ = assistant.generate_itinerary(country, state, 3, 30000)
```

## API Response Examples

### Country Info Response
```json
{
    "states": ["Tokyo", "Osaka", "Kyoto", "Hiroshima"],
    "region": "Asia",
    "description": "East Asian island nation with ancient temples..."
}
```

### Search Result Response
```json
{
    "type": "state",
    "name": "Paris, France",
    "data": {
        "states": ["Paris", "Lyon", "Marseille", ...],
        "region": "Europe",
        "description": "..."
    }
}
```

### Itinerary Response
```
(string) Full markdown-formatted itinerary with:
- Daily schedules
- Budget breakdowns
- Activity recommendations
- Travel tips
```

## Conclusion

The Global Travel Guide Assistant API provides comprehensive coverage of:
- ✅ 195+ countries
- ✅ 3,500+ states/regions
- ✅ Flexible search and retrieval
- ✅ Automatic itinerary generation
- ✅ Demo and AI modes

Use these examples as templates for your own travel planning applications!

---

**For more info**: Check GLOBAL_COVERAGE_DOCUMENTATION.md
**Quick start**: See QUICK_START.md
**Version**: 2.0
