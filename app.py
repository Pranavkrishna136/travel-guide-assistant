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
    # 🌍 Travel Guide Assistant
    ### Smart & Personalized Travel Planning Powered by AI
    **With Live Location Tracking & 65+ Global Destinations**
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

# Sidebar for configuration
with st.sidebar:
    st.header("⚙️ Configuration")
    
    st.subheader("📍 Your Current Location")
    
    location_option = st.radio(
        "Get Location By:",
        ["Manual Entry", "Browser Auto-Detect"],
        help="Choose how to set your current location"
    )
    
    current_lat = None
    current_lng = None
    current_city = None
    current_address = None
    
    if location_option == "Manual Entry":
        col1, col2 = st.columns(2)
        with col1:
            current_lat = st.number_input("Latitude", value=40.7128, format="%.4f")
        with col2:
            current_lng = st.number_input("Longitude", value=-74.0060, format="%.4f")
    else:
        st.info("📌 To use auto-detect, enable location in your browser settings")
        # Fallback to manual entry
        col1, col2 = st.columns(2)
        with col1:
            current_lat = st.number_input("Latitude (Fallback)", value=40.7128, format="%.4f", key="lat_fallback")
        with col2:
            current_lng = st.number_input("Longitude (Fallback)", value=-74.0060, format="%.4f", key="lng_fallback")
    
    # Update location if values changed
    if current_lat and current_lng:
        geolocator = Nominatim(user_agent="travel_guide_app", timeout=5)
        try:
            location_data = geolocator.reverse(f"{current_lat}, {current_lng}", language='en')
            address_parts = location_data.address.split(',')
            current_city = address_parts[0] if len(address_parts) > 0 else "Unknown"
            current_address = location_data.address
            
            st.session_state.user_location = {
                'lat': current_lat,
                'lng': current_lng,
                'city': current_city,
                'address': current_address
            }
            
            st.success(f"✅ Location Set: **{current_city}**")
            with st.expander("Full Address Details"):
                st.write(current_address)
        except (GeocoderTimedOut, Exception) as e:
            st.session_state.user_location = {
                'lat': current_lat,
                'lng': current_lng,
                'city': 'Location',
                'address': f'{current_lat}, {current_lng}'
            }
            st.warning(f"Coordinates set: ({current_lat}, {current_lng})")
    
    st.markdown("---")
    
    # Demo mode toggle
    use_demo_mode = st.checkbox(
        "🎮 Use Demo Mode (No API Key)",
        value=True,
        help="Generate itineraries from travel data without OpenAI API"
    )
    
    if not use_demo_mode:
        # API Key input
        api_key = st.text_input(
            "🔑 OpenAI API Key",
            type="password",
            help="Enter your OpenAI API key for AI-powered itinerary generation"
        )
        
        if api_key:
            try:
                st.session_state.assistant.set_openai_client(api_key)
                st.session_state.api_key_set = True
                st.success("✅ API Key Configured!")
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
                st.session_state.api_key_set = False
        else:
            st.session_state.api_key_set = False
    else:
        st.session_state.api_key_set = True
        st.info("🎮 Demo mode enabled - using travel database")
    
    st.markdown("---")
    
    # About section
    st.header("ℹ️ About")
    st.write("""
    🌍 **Travel Guide Assistant** uses:
    - **RAG**: Retrieval-Augmented Generation
    - **Geolocation**: Real-time location tracking
    - **AI**: OpenAI GPT-3.5 (optional)
    - **Maps**: Interactive Google Maps integration
    
    Create personalized itineraries based on your current location, preferences, and budget!
    """)
    
    st.markdown("---")
    st.header("💳 Need Help?")
    if not use_demo_mode:
        st.warning("""
        **API Issues?**
        1. Check balance: https://platform.openai.com/account
        2. Add payment method
        3. Use **Demo Mode** - no API needed!
        """)
    
    st.markdown("---")
    st.write("📚 [View Docs](https://pranavkrishna136.github.io/travel-guide-assistant/)")

# Main content area
col1, col2 = st.columns([1, 1], gap="medium")

st.markdown("---")

# Trip planning section
col1, col2 = st.columns([1, 1], gap="medium")

with col1:
    st.header("🎯 Trip Details")
    
    # Get available cities
    available_cities = sorted(list(st.session_state.assistant.documents.keys()))
    
    destination = st.selectbox(
        "📍 Select Destination",
        options=available_cities,
        index=0,
        help="Choose from available cities"
    )
    
    # Also allow custom input
    custom_dest = st.text_input(
        "Or enter custom destination",
        placeholder="e.g., Bangkok, Rome, Sydney",
        help="Enter any destination - we'll find the closest match"
    )
    
    if custom_dest:
        destination = custom_dest
    
    days = st.slider(
        "📅 Trip Duration (days)",
        min_value=1,
        max_value=30,
        value=3,
        help="How many days?"
    )
    
    budget = st.number_input(
        "💰 Budget (USD)",
        min_value=0,
        max_value=100000,
        value=700,
        step=100,
        help="Total budget"
    )
    
    # Display available cities count
    st.metric("🌍 Available Destinations", len(available_cities))

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
**Budget:** ${budget}  
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