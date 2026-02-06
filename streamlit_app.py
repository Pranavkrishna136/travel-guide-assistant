"""Streamlit Travel Guide using Keyword-Based RAG (no heavy ML libraries)"""
import streamlit as st
from keyword_rag import get_rag_backend
import folium
from streamlit_folium import st_folium
import pandas as pd

st.set_page_config(
    page_title="🌍 Travel Guide RAG",
    page_icon="✈️",
    layout="wide"
)

st.title("🌍 World Travel Guide Assistant")
st.subheader("Powered by Keyword-Based Retrieval")

# Load RAG
@st.cache_resource
def load_rag():
    return get_rag_backend()

rag = load_rag()

# Initialize session state
if 'favorites' not in st.session_state:
    st.session_state.favorites = []

# Create tabs
tab1, tab2, tab3, tab4 = st.tabs(["🔍 Search", "💬 Q&A", "🗺️ Map", "❤️ Favorites"])

# ===== TAB 1: SEARCH =====
with tab1:
    st.markdown("### 🔍 Search Destinations")
    
    col1, col2 = st.columns([3, 1])
    with col1:
        search_query = st.text_input("Search:", placeholder="beach, temple, monument...")
    with col2:
        search_btn = st.button("🔍 Search")
    
    # Filters
    col1, col2, col3 = st.columns(3)
    with col1:
        budget_filter = st.multiselect(
            "💰 Budget",
            ["budget", "mid_range"],
            key="budget_filter"
        )
    with col2:
        all_categories = set()
        for dest in rag.destinations:
            all_categories.update([cat.strip() for cat in dest['category'].split(',')])
        
        category_filter = st.multiselect(
            "🎯 Category",
            sorted(list(all_categories)),
            key="category_filter"
        )
    with col3:
        top_k = st.slider("Results", 1, 10, 5)
    
    if search_btn and search_query:
        st.divider()
        
        # Build filters
        filters = {}
        if budget_filter:
            filters['budget'] = budget_filter
        if category_filter:
            filters['category'] = category_filter
        
        # Search
        results = rag.semantic_search(
            search_query,
            top_k=top_k,
            filters=filters if filters else None
        )
        
        if results:
            st.success(f"✅ Found {len(results)} destination(s)")
            
            for i, result in enumerate(results, 1):
                dest = result['destination']
                score = result['score']
                
                col1, col2 = st.columns([3, 1])
                
                with col1:
                    st.markdown(f"**{i}. {dest['name']}** - {dest['city']}, {dest['country']}")
                    st.write(f"📊 Relevance: {score:.0%}")
                    st.write(f"💰 {dest['budget']} | 🎯 {dest['category']}")
                    st.write(f"📝 {dest['description'][:100]}...")
                    
                    if st.button("❤️ Add to Favorites", key=f"fav_{dest['id']}"):
                        if dest not in st.session_state.favorites:
                            st.session_state.favorites.append(dest)
                            st.success(f"Added {dest['name']}!")
                
                with col2:
                    # Mini map
                    m = folium.Map(
                        location=[dest['lat'], dest['lon']],
                        zoom_start=10
                    )
                    folium.Marker(
                        [dest['lat'], dest['lon']],
                        popup=dest['name']
                    ).add_to(m)
                    st_folium(m, width=250, height=250)
                
                st.divider()
        else:
            st.warning("❌ No destinations found")

# ===== TAB 2: Q&A =====
with tab2:
    st.markdown("### 💬 Travel Q&A")
    
    question = st.text_input("Ask:", placeholder="Best beaches? Where can I find temples?")
    
    if st.button("Answer"):
        if question:
            result = rag.travel_qna(question)
            st.info(result['answer'])
            
            if result['sources']:
                st.markdown("**Related Destinations:**")
                for source in result['sources']:
                    st.write(f"🎯 {source['name']} - {source['city']}")

# ===== TAB 3: MAP =====
with tab3:
    st.markdown("### 🗺️ All Destinations")
    
    # World map
    m = folium.Map(
        location=[20, 0],
        zoom_start=2
    )
    
    for dest in rag.destinations:
        folium.Marker(
            location=[dest['lat'], dest['lon']],
            popup=f"{dest['name']}<br>{dest['city']}, {dest['country']}",
            tooltip=dest['name']
        ).add_to(m)
    
    st_folium(m, width=1300, height=600)
    
    # Table
    st.markdown("### Destinations List")
    import pandas as pd
    
    data = []
    for dest in rag.destinations:
        data.append({
            'Name': dest['name'],
            'City': dest['city'],
            'Country': dest['country'],
            'Budget': dest['budget'],
            'Category': dest['category'],
            'Duration': f"{dest['duration_hours']}h"
        })
    
    st.dataframe(pd.DataFrame(data))

# ===== TAB 4: FAVORITES =====
with tab4:
    st.markdown("### ❤️ My Favorites")
    
    if st.session_state.favorites:
        for i, fav in enumerate(st.session_state.favorites, 1):
            col1, col2 = st.columns([4, 1])
            
            with col1:
                st.markdown(f"**{i}. {fav['name']}** - {fav['city']}, {fav['country']}")
                st.write(f"💰 {fav['budget']} | 🎯 {fav['category']}")
            
            with col2:
                if st.button("❌", key=f"remove_{i}"):
                    st.session_state.favorites.pop(i-1)
                    st.rerun()
            
            st.divider()
    else:
        st.info("No favorites yet! Add destinations from the search tab.")

# Footer
st.markdown("---")
st.markdown("*🌍 World Travel Guide RAG | Powered by Streamlit & Keyword Search*")
