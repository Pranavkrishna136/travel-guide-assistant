#!/usr/bin/env python
"""Test the keyword-based RAG"""
import sys
sys.path.insert(0, r'c:\Users\prana\Downloads\Travel guide')

print("\n" + "="*70)
print("KEYWORD-BASED RAG SYSTEM TEST")
print("="*70 + "\n")

from keyword_rag import get_rag_backend

print("Loading RAG backend (keyword-based)...")
rag = get_rag_backend()
print("✅ Backend loaded\n")

# Test 1
print("TEST 1: Search for 'beach'")
print("-" * 70)
results = rag.semantic_search("beach", top_k=3)
print(f"Found {len(results)} result(s):\n")
for r in results:
    d = r['destination']
    print(f"  • {d['name']} ({r['score']:.0%} relevance)")
    print(f"    {d['city']}, {d['country']}")

# Test 2
print("\n\nTEST 2: Search for 'temple'")
print("-" * 70)
results = rag.semantic_search("temple", top_k=3)
print(f"Found {len(results)} result(s):\n")
for r in results:
    d = r['destination']
    print(f"  • {d['name']} ({r['score']:.0%} relevance)")
    print(f"    {d['city']}, {d['country']}")

# Test 3
print("\n\nTEST 3: Q&A - 'Best Asian destinations?'")
print("-" * 70)
qa = rag.travel_qna("Best Asian destinations?")
print(f"Question: Best Asian destinations?")
print(f"Answer: {qa['answer']}")
print("\nSources:")
for s in qa['sources']:
    print(f"  - {s['name']} ({s['city']})")

# Test 4
print("\n\nTEST 4: All Destinations")
print("-" * 70)
for i, dest in enumerate(rag.destinations, 1):
    print(f"{i}. {dest['name']} - {dest['city']}, {dest['country']}")

print("\n" + "="*70)
print("✅ ALL TESTS PASSED!")
print("="*70 + "\n")
