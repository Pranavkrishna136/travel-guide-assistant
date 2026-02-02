# Usage

This page shows common usage flows and examples for the Travel Guide Assistant.

Example: generate a 3-day itinerary for Paris, budget $700

1. Open the app (Streamlit):

   streamlit run app.py

2. Enter values:
- Destination: Paris
- Duration: 3 days
- Budget: 700

3. Click "Generate Itinerary" and review the returned plan. Use follow-up prompts to adjust preferences (more museums, less walking, family-friendly, etc.).

Programmatic usage (script)

If the project exposes a Python function or CLI for generating itineraries, call it like:

```py
# pseudocode — adapt to actual function names
from travel_assistant import generate_itinerary

plan = generate_itinerary(destination='Paris', days=3, budget=700)
print(plan)
```

Notes
- Prompts and model choices impact cost/latency. Use smaller models for fast feedback and larger ones for final outputs.
