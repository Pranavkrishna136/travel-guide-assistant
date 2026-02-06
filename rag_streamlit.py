"""Streamlit Travel Guide with RAG"""
import streamlit as st
import folium
from streamlit_folium import st_folium
from rag_backend import get_rag_backend
import pandas as pd

# Configure page
st.set_page_config(
    page_title="🌍 World Travel Guide Assistant",
    page_icon="✈️",
    layout="wide"
)

# Initialize RAG backend
@st.cache_resource
def load_rag():
    return get_rag_backend()

rag = load_rag()

# Initialize session state
if 'favorites' not in st.session_state:
    st.session_state.favorites = []
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'user_preferences' not in st.session_state:
    st.session_state.user_preferences = {'budget': 'budget', 'interests': [], 'duration': 3}

# Header
st.markdown("# 🌍 World Travel Guide Assistant")
st.markdown("*Powered by RAG (Retrieval-Augmented Generation) with AI-driven recommendations*")

# Create tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🔍 Semantic Search",
    "💬 Travel Q&A",
    "📋 Itinerary Generator",
    "🗺️ Interactive Map",
    "❤️ My Favorites"
])

# ==================== TAB 1: SEMANTIC SEARCH ====================
with tab1:
    st.markdown("### 🔍 Semantic Destination Search")
    st.markdown("Search destinations using natural language")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        search_query = st.text_input(
            "Search destinations:",
            placeholder="Try: 'beach', 'temple', 'monument', 'budget trip'...",
            key="search_input"
        )
    
    with col2:
        search_clicked = st.button("🔍 Search", use_container_width=True, key="search_btn")
    
    # Filters
    col1, col2, col3 = st.columns(3)
    
    with col1:
        budget_filter = st.multiselect(
            "💰 Budget",
            ["budget", "mid_range"],
            default=[],
            key="budget_filter"
        )
    
    with col2:
        all_categories = set()
        for dest in rag.destinations:
            all_categories.update([cat.strip() for cat in dest['category'].split(',')])
        
        category_filter = st.multiselect(
            "🎯 Interest Category",
            sorted(list(all_categories)),
            default=[],
            key="category_filter"
        )
    
    with col3:
        top_k = st.slider("📊 Results", 1, 10, 5, key="top_k_slider")
    
    # Check if should search
    should_search = search_clicked or (search_query and len(search_query) > 1)
    
    if should_search and search_query:
        st.markdown("---")
        st.markdown("#### 🎯 Search Results")
        
        # Build filters dict
        filters = None
        if budget_filter or category_filter:
            filters = {}
            if budget_filter:
                filters['budget'] = budget_filter
            if category_filter:
                filters['category'] = category_filter
        
        try:
            results = rag.semantic_search(
                search_query,
                top_k=top_k,
                filters=filters
            )
            
            if results:
                st.success(f"✅ Found {len(results)} destination(s)")
                
                for i, result in enumerate(results, 1):
                    dest = result['destination']
                    score = result['score']
                    
                    with st.container():
                        col1, col2 = st.columns([3, 1])
                        
                        with col1:
                            st.markdown(f"**{i}. {dest['name']}** - {dest['city']}, {dest['country']}")
                            st.write(f"📊 Relevance Score: {score:.2%}")
                            st.write(f"💰 Budget: {dest['budget']} | ⏱️ {dest['duration_hours']} hours")
                            st.write(f"🎯 Categories: {dest['category']}")
                            
                            if st.button(f"❤️ Add to Favorites", key=f"fav_{dest['id']}"):
                                if dest['id'] not in [f['id'] for f in st.session_state.favorites]:
                                    st.session_state.favorites.append(dest)
                                    st.success(f"✅ {dest['name']} added to favorites!")
                        
                        with col2:
                            # Mini map
                            mini_map = folium.Map(
                                location=[dest['lat'], dest['lon']],
                                zoom_start=10,
                                tiles="OpenStreetMap"
                            )
                            folium.Marker(
                                [dest['lat'], dest['lon']],
                                popup=dest['name']
                            ).add_to(mini_map)
                            st_folium(mini_map, width=250, height=250)
                        
                        st.markdown("---")
            else:
                st.warning("❌ No destinations found. Try different search terms!")
        except Exception as e:
            st.error(f"❌ Search error: {str(e)}")
            import traceback
            st.error(traceback.format_exc())

# ==================== TAB 2: TRAVEL Q&A ====================
with tab2:
    st.markdown("### 💬 Travel Q&A Chatbot")
    st.markdown("Ask questions about destinations and get answers with sources!")
    
    user_question = st.text_input(
        "Ask a travel question:",
        placeholder="E.g., 'Best time to visit Taj Mahal?', 'Where can I find beaches?'...",
        key="qa_input"
    )
    
    if st.button("🔍 Ask", key="qa_btn") and user_question:
        result = rag.travel_qna(user_question, top_k=3)
        
        st.markdown("---")
        st.markdown("#### Answer:")
        st.write(result['answer'])
        
        if result['sources']:
            st.markdown("#### Sources:")
            for source in result['sources']:
                st.write(f"📍 {source['name']} - {source['city']}")
    
    # Chat history
    if st.session_state.chat_history:
        st.markdown("#### Recent Questions:")
        for i, msg in enumerate(st.session_state.chat_history[-5:], 1):
            st.write(f"{i}. {msg}")

# ==================== TAB 3: ITINERARY GENERATOR ====================
with tab3:
    st.markdown("### 📋 Personalized Itinerary Generator")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        pref_budget = st.selectbox(
            "💰 Budget Level",
            ["budget", "mid_range"],
            key="itinerary_budget"
        )
    
    with col2:
        pref_duration = st.slider(
            "📅 Days",
            1, 14, 3,
            key="itinerary_duration"
        )
    
    with col3:
        pref_interests = st.multiselect(
            "🎯 Interests",
            ["temple", "beach", "monument", "culture", "nature", "adventure"],
            default=["culture"],
            key="itinerary_interests"
        )
    
    if st.button("✈️ Generate Itinerary", key="itinerary_btn"):
        itinerary = rag.personalized_itinerary({
            'budget': pref_budget,
            'duration': pref_duration,
            'interests': pref_interests
        })
        
        st.markdown(f"### {itinerary['title']}")
        
        for day_plan in itinerary['days']:
            col1, col2 = st.columns([2, 1])
            with col1:
                st.markdown(f"**Day {day_plan['day']}: {day_plan['destination']}**")
                st.write("Activities:")
                for act in day_plan['activities']:
                    st.write(f"  • {act}")
                st.write("Food:")
                for meal in day_plan['meals']:
                    st.write(f"  • {meal}")
            with col2:
                st.metric("Estimated Cost", day_plan['estimated_cost'])

# ==================== TAB 4: INTERACTIVE MAP ====================
with tab4:
    st.markdown("### 🗺️ Explore All Destinations")
    
    # Create world map with all destinations
    world_map = folium.Map(
        location=[20, 0],
        zoom_start=2,
        tiles="OpenStreetMap"
    )
    
    # Add markers for all destinations
    for dest in rag.destinations:
        folium.Marker(
            location=[dest['lat'], dest['lon']],
            popup=f"{dest['name']}<br>{dest['city']}, {dest['country']}",
            tooltip=dest['name'],
            icon=folium.Icon(color='blue', icon='info-sign')
        ).add_to(world_map)
    
    st_folium(world_map, width=1300, height=600)
    
    # Show destinations table
    st.markdown("### Destinations Overview")
    dest_data = []
    for dest in rag.destinations:
        dest_data.append({
            'Name': dest['name'],
            'City': dest['city'],
            'Country': dest['country'],
            'Budget': dest['budget'],
            'Categories': dest['category']
        })
    
    st.dataframe(pd.DataFrame(dest_data), use_container_width=True)

# ==================== TAB 5: FAVORITES ====================
with tab5:
    st.markdown("### ❤️ My Favorite Destinations")
    
    if st.session_state.favorites:
        for i, fav in enumerate(st.session_state.favorites, 1):
            col1, col2 = st.columns([4, 1])
            
            with col1:
                st.markdown(f"**{i}. {fav['name']}** - {fav['city']}, {fav['country']}")
                st.write(f"📊 {fav['category']} | 💰 {fav['budget']} | ⏱️ {fav['duration_hours']} hours")
                st.write(f"📍 Entry Fee: {fav['entry_fee']}")
            
            with col2:
                if st.button(f"❌ Remove", key=f"remove_{fav['id']}"):
                    st.session_state.favorites = [f for f in st.session_state.favorites if f['id'] != fav['id']]
                    st.rerun()
            
            st.markdown("---")
    else:
        st.info("No favorites yet! Add destinations from the search tab.")

# Footer
st.markdown("---")
st.markdown("*🌍 World Travel Guide Assistant - Powered by RAG & AI | Built with Streamlit*")
