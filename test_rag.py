#!/usr/bin/env python
"""Test the RAG backend without Streamlit"""
import sys
sys.path.insert(0, 'c:\\Users\\prana\\Downloads\\Travel guide')

from rag_backend import get_rag_backend

print("\n" + "="*60)
print("TESTING RAG BACKEND")
print("="*60)

# Initialize
print("\nInitializing RAG backend...")
rag = get_rag_backend()
print("✅ Backend initialized\n")

# Test 1: Semantic Search
print("TEST 1: Semantic Search")
print("-" * 40)
results = rag.semantic_search("beach", top_k=3)
print(f"Query: 'beach'")
print(f"Results found: {len(results)}")
for r in results:
    print(f"  - {r['destination']['name']}: {r['score']:.2%}")

# Test 2: Different query
print("\n\nTEST 2: Semantic Search - 'temple'")
print("-" * 40)
results = rag.semantic_search("temple", top_k=3)
print(f"Results found: {len(results)}")
for r in results:
    print(f"  - {r['destination']['name']}: {r['score']:.2%}")

# Test 3: Q&A
print("\n\nTEST 3: Travel Q&A")
print("-" * 40)
qa_result = rag.travel_qna("Best beaches in Asia?")
print("Question: Best beaches in Asia?")
print(f"Answer: {qa_result['answer'][:100]}...")
print("Sources:")
for source in qa_result['sources']:
    print(f"  - {source['name']}")

# Test 4: Itinerary
print("\n\nTEST 4: Itinerary Generation")
print("-" * 40)
itinerary = rag.personalized_itinerary({
    'budget': 'budget',
    'duration': 3,
    'interests': ['beach', 'temple']
})
print(f"Title: {itinerary['title']}")
print(f"Days: {itinerary['duration_days']}")
for day in itinerary['days']:
    print(f"  Day {day['day']}: {day['destination']}")

# Test 5: Recommendations
print("\n\nTEST 5: Review-Aware Recommendations")
print("-" * 40)
rec = rag.review_aware_recommendations('goa_beaches')
print(f"Destination: {rec['destination']}")
print(f"Rating: {rec['average_rating']:.1f}/5")
print(f"Reviews: {len(rec['reviews'])}")

print("\n" + "="*60)
print("ALL TESTS PASSED! ✅")
print("="*60 + "\n")
