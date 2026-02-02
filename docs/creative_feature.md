# Creative / Unique Feature — Itinerary Composer (proposal)

Proposed feature: an interactive "Itinerary Composer" that generates multi-day plans with constraints, optimization, and trade-offs.

Key capabilities
- Constraint input: must-see places, accessibility, max walking distance, start/end times
- Optimization: cluster points-of-interest by proximity, minimize transit time, balance activities (museums vs outdoor)
- Output: day-by-day schedule with approximate times and travel suggestions

Implementation approach (minimal viable)
1. When user asks for itinerary, allow checkboxes/fields for constraints.
2. Retrieved RAG context includes POIs and their locations.
3. Use a simple greedy scheduler: sort POIs by priority, then assign to day/time slots while checking travel-time heuristics.
4. For improved results add route optimization (TSP heuristics) and integrate a mapping API for accurate travel time.

Docs & demo
- Add a demo flow in the Streamlit UI to show the composer in action
- Provide an example dataset and screenshot in the README/docs
