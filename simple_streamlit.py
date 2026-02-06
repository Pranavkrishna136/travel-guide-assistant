"""Simple Streamlit Travel Guide RAG"""
import streamlit as st
from simple_rag import get_rag_backend

st.set_page_config(page_title="🌍 Travel Guide RAG", page_icon="✈️", layout="wide")

st.title("🌍 Travel Guide Assistant (RAG)")

# Initialize
@st.cache_resource
def load_rag():
    return get_rag_backend()

try:
    rag = load_rag()
    st.success("✅ RAG Backend loaded successfully!")
except Exception as e:
    st.error(f"❌ Error loading backend: {e}")
    st.stop()

# Tabs
tab1, tab2, tab3 = st.tabs(["🔍 Search", "💬 Q&A", "🗺️ Destinations"])

# TAB 1: Search
with tab1:
    st.header("Semantic Destination Search")
    
    col1, col2 = st.columns([3, 1])
    with col1:
        query = st.text_input("Search:", placeholder="beach, temple, monument...")
    with col2:
        search_btn = st.button("Search")
    
    if search_btn and query:
        st.write(f"Searching for: **{query}**")
        results = rag.semantic_search(query, top_k=5)
        
        if results:
            st.success(f"Found {len(results)} destinations")
            for r in results:
                d = r['destination']
                st.markdown(f"**{d['name']}** ({r['score']:.0%})")
                st.write(f"📍 {d['city']}, {d['country']} | 💰 {d['budget']}")
                st.divider()
        else:
            st.warning("No results found")

# TAB 2: Q&A
with tab2:
    st.header("Travel Q&A")
    
    question = st.text_input("Ask:", placeholder="Best beaches? Where are temples?")
    if st.button("Answer"):
        if question:
            result = rag.travel_qna(question)
            st.write(result['answer'])
            if result['sources']:
                st.write("**Sources:**")
                for s in result['sources']:
                    st.write(f"- {s['name']}")

# TAB 3: Destinations
with tab3:
    st.header("All Destinations")
    
    for dest in rag.destinations:
        st.markdown(f"**{dest['name']}**")
        st.write(f"{dest['city']}, {dest['country']} | {dest['category']}")
        st.divider()

st.markdown("---")
st.markdown("*RAG Travel Guide powered by Streamlit & FAISS*")
