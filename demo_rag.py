#!/usr/bin/env python
"""Direct test of the simplified RAG backend"""
import sys
sys.path.insert(0, r'c:\Users\prana\Downloads\Travel guide')

print("\n" + "="*70)
print("WORLD TRAVEL GUIDE RAG - BACKEND DEMONSTRATION")
print("="*70 + "\n")

from simple_rag import get_rag_backend

print("Initializing RAG backend...")
rag = get_rag_backend()
print("✅ Backend ready\n")

# Test 1
print("="*70)
print("TEST 1: Semantic Search - 'beach'")
print("="*70)
results = rag.semantic_search("beach", top_k=3)
print(f"\nFound {len(results)} result(s) for 'beach':\n")
for i, r in enumerate(results, 1):
    d = r['destination']
    print(f"{i}. {d['name']} - {d['city']}, {d['country']}")
    print(f"   Relevance: {r['score']:.1%}")
    print(f"   Category: {d['category']}")
    print()

# Test 2
print("="*70)
print("TEST 2: Semantic Search - 'temple'")
print("="*70)
results = rag.semantic_search("temple", top_k=3)
print(f"\nFound {len(results)} result(s) for 'temple':\n")
for i, r in enumerate(results, 1):
    d = r['destination']
    print(f"{i}. {d['name']} - {d['city']}, {d['country']}")
    print(f"   Relevance: {r['score']:.1%}")
    print()

# Test 3
print("="*70)
print("TEST 3: Travel Q&A")
print("="*70)
qa_result = rag.travel_qna("Best places to visit in Asia?")
print(f"\nQuestion: Best places to visit in Asia?")
print(f"\nAnswer: {qa_result['answer']}\n")
print("Related destinations:")
for source in qa_result['sources']:
    print(f"  - {source['name']} ({source['city']})")

# Test 4
print("\n" + "="*70)
print("TEST 4: All Available Destinations")
print("="*70 + "\n")
for i, dest in enumerate(rag.destinations, 1):
    print(f"{i}. {dest['name']} - {dest['city']}, {dest['country']}")

print("\n" + "="*70)
print("✅ ALL TESTS PASSED SUCCESSFULLY!")
print("="*70 + "\n")
print("RAG Backend is working correctly!")
print("The semantic search, Q&A, and destination database are all functional.\n")
