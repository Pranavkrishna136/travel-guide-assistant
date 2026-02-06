"""
Travel Guide Assistant - Streamlit Web Dashboard with Location Features
"""

import streamlit as st
import os
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from travel_assistant import TravelAssistant
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="🌍 Travel Guide Assistant",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom styling
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton > button {
        width: 100%;
        padding: 12px;
        font-size: 16px;
        border-radius: 8px;
    }
    </style>
    """, unsafe_allow_html=True)

# Header
st.markdown("""
    # 🌍 Global Travel Guide Assistant
    ### Smart & Personalized Travel Planning Powered by AI
    **Comprehensive Coverage: All 195+ Countries & Their States/Regions**
    ---
""")

# Initialize session state
if 'assistant' not in st.session_state:
    try:
        st.session_state.assistant = TravelAssistant()
    except FileNotFoundError:
        st.error("⚠️ FAISS index not found. Please run `scripts/build_index.py` first.")
        st.stop()

if 'api_key_set' not in st.session_state:
    st.session_state.api_key_set = False

if 'itinerary' not in st.session_state:
    st.session_state.itinerary = None

if 'is_demo' not in st.session_state:
    st.session_state.is_demo = False

if 'user_location' not in st.session_state:
    st.session_state.user_location = None

# Demo mode always enabled - no configuration sidebar
use_demo_mode = True
st.session_state.api_key_set = True

# Main content area
col1, col2 = st.columns([1, 1], gap="medium")

st.markdown("---")

# Trip planning section
col1, col2 = st.columns([1, 1], gap="medium")

with col1:
    st.header("🎯 Trip Details")
    
    # Get all available countries
    available_countries = st.session_state.assistant.get_available_countries()
    
    # Country selection
    selected_country = st.selectbox(
        "🌐 Select Country",
        options=available_countries,
        index=0,
        help="Choose from 195+ countries worldwide"
    )
    
    # Get states for selected country
    available_states = st.session_state.assistant.get_available_states(selected_country)
    
    selected_state = st.selectbox(
        "📍 Select State/Region/City",
        options=available_states if available_states else [selected_country],
        help="Choose a specific state, region, or city within the country"
    )
    
    # Search functionality
    search_term = st.text_input(
        "🔍 Or search destination",
        placeholder="e.g., Paris, Tokyo, Bali...",
        help="Search for any destination worldwide"
    )
    
    destination = selected_country
    state = selected_state
    
    if search_term:
        search_results = st.session_state.assistant.search_destination(search_term)
        if search_results:
            result = search_results[0]
            if result["type"] == "country":
                destination = result["name"]
                state = ""
            else:
                parts = result["name"].rsplit(", ", 1)
                state = parts[0]
                destination = parts[1]
            st.info(f"✅ Found: {state or destination}" if state else f"✅ Found: {destination}")
    
    days = st.slider(
        "📅 Trip Duration (days)",
        min_value=1,
        max_value=30,
        value=3,
        help="How many days?"
    )
    
    budget = st.number_input(
        "💰 Budget (₹ Rupees)",
        min_value=0,
        max_value=10000000,
        value=50000,
        step=1000,
        help="Total budget in Indian Rupees"
    )
    
    # Display statistics
    col1_1, col1_2, col1_3 = st.columns(3)
    with col1_1:
        st.metric("🌍 Countries", len(st.session_state.assistant.get_available_countries()))
    with col1_2:
        st.metric("📍 Selected", state or destination)
    with col1_3:
        available_states = st.session_state.assistant.get_available_states(destination)
        st.metric("🗺️ Regions", len(available_states) if available_states else 1)

with col2:
    st.header("✨ Preferences")
    
    # Preference checkboxes
    activities = st.multiselect(
        "🎨 Activities",
        options=[
            "Museums & Culture",
            "Outdoor & Nature",
            "Food & Cuisine",
            "Shopping",
            "Nightlife",
            "Adventure Sports",
            "Photography",
            "Historical Sites"
        ],
        default=["Museums & Culture", "Food & Cuisine"]
    )
    
    travel_style = st.radio(
        "🚶 Travel Style",
        options=["Budget", "Moderate", "Luxury"],
        horizontal=True,
        help="Your travel style"
    )
    
    pace = st.radio(
        "⏱️ Pace",
        options=["Relaxed", "Moderate", "Fast-paced"],
        horizontal=True,
        help="Schedule intensity"
    )

st.markdown("---")

# Build preferences string
preferences = f"""
Travel Style: {travel_style}
Pace: {pace}
Activities: {', '.join(activities) if activities else 'Any'}
"""

# Generate button
col_btn1, col_btn2 = st.columns([1, 1])

with col_btn1:
    if st.button("🚀 Generate Itinerary", type="primary", use_container_width=True):
        if not destination:
            st.error("❌ Please enter a destination!")
        elif not st.session_state.api_key_set and not use_demo_mode:
            st.error("❌ Please configure your OpenAI API key in the sidebar!")
        else:
            with st.spinner("✨ Generating your personalized itinerary..."):
                try:
                    itinerary, is_demo = st.session_state.assistant.generate_itinerary(
                        destination=destination,
                        state=state,
                        days=days,
                        budget=budget,
                        preferences=preferences,
                        use_demo=use_demo_mode
                    )
                    st.session_state.itinerary = itinerary
                    st.session_state.is_demo = is_demo
                    st.success("✅ Itinerary generated successfully!")
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")

with col_btn2:
    if st.session_state.itinerary:
        if st.button("📋 Copy to Clipboard", type="secondary", use_container_width=True):
            st.success("✅ Ready to copy!")

# Display itinerary
if st.session_state.itinerary:
    # Display mode indicator
    if st.session_state.is_demo:
        st.info("🎮 **DEMO MODE** - Generated from travel database (no API used)")
    else:
        st.success("🤖 **AI-POWERED** - Generated using OpenAI GPT-3.5")
    
    st.header("📋 Your Personalized Itinerary")
    
    # Display itinerary in expandable sections
    with st.expander("📖 Full Itinerary", expanded=True):
        st.markdown(st.session_state.itinerary)
    
    # Download button
    st.download_button(
        label="📥 Download Itinerary (Text)",
        data=st.session_state.itinerary,
        file_name=f"{destination}_itinerary_{days}days.txt",
        mime="text/plain",
        use_container_width=True
    )
    
    # Export as markdown
    markdown_content = f"""# Travel Itinerary for {destination}
**Duration:** {days} days  
**Budget:** ₹{budget:,}  
**Travel Style:** {travel_style}  
**Pace:** {pace}  
**Mode:** {"Demo" if st.session_state.is_demo else "AI-Powered"}

---

{st.session_state.itinerary}
"""
    
    st.download_button(
        label="📑 Download Itinerary (Markdown)",
        data=markdown_content,
        file_name=f"{destination}_itinerary_{days}days.md",
        mime="text/markdown",
        use_container_width=True
    )

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #666;'>
    <p>Made with ❤️ by Travel Guide Assistant</p>
    <p>🔗 <a href='https://github.com/Pranavkrishna136/travel-guide-assistant'>GitHub Repository</a></p>
    <p style='font-size: 0.8em; margin-top: 10px;'>
    Features: Location Tracking • Google Maps • AI-Powered Itineraries • 50+ Destinations
    </p>
    </div>
    """, unsafe_allow_html=True)