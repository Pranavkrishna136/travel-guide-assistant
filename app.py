"""
Travel Guide Assistant - Streamlit Web Dashboard with Location & Maps Integration
"""

import streamlit as st
import os
import folium
from streamlit_folium import st_folium
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
    **Now with Live Location Tracking & Google Maps Integration**
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
st.subheader("🗺️ Interactive Map View")

# Create two columns for map and destination info
map_col, dest_col = st.columns([2, 1])

with map_col:
    # Create folium map
    available_cities = sorted(list(st.session_state.assistant.documents.keys()))
    
    # Map center (user location or default)
    if st.session_state.user_location:
        center_lat = st.session_state.user_location['lat']
        center_lng = st.session_state.user_location['lng']
        center_name = st.session_state.user_location['city']
    else:
        center_lat, center_lng, center_name = 40.7128, -74.0060, "New York"
    
    m = folium.Map(
        location=[center_lat, center_lng],
        zoom_start=4,
        tiles='OpenStreetMap'
    )
    
    # Add user location marker
    folium.Marker(
        location=[center_lat, center_lng],
        popup=f"<b>📍 Your Location</b><br>{center_name}",
        tooltip="Your Current Location",
        icon=folium.Icon(color='blue', icon='info-sign', prefix='glyphicon')
    ).add_to(m)
    
    # Add destination cities markers (all available cities)
    all_cities_coords = {
        'Amsterdam': (52.3676, 4.9041),
        'Athens': (37.9838, 23.7275),
        'Auckland': (-37.7870, 174.7765),
        'Bali': (-8.6705, 115.2126),
        'Bangkok': (13.7563, 100.5018),
        'Bangkok_Extended': (13.7563, 100.5018),
        'Barcelona': (41.3874, 2.1686),
        'Barcelona_Extended': (41.3874, 2.1686),
        'Beijing': (39.9042, 116.4074),
        'Berlin': (52.5200, 13.4050),
        'Bogota': (4.7110, -74.0721),
        'Boracay': (11.9674, 121.9248),
        'Budapest': (47.4979, 19.0402),
        'Buenos Aires': (-34.6037, -58.3816),
        'Cairo': (30.0444, 31.2357),
        'Cape Town': (-33.9249, 18.4241),
        'Chiang Mai': (18.7883, 98.9853),
        'Delhi': (28.7041, 77.1025),
        'Dubai': (25.2048, 55.2708),
        'Dubai_Culture': (25.2048, 55.2708),
        'Dubai_Extended': (25.2048, 55.2708),
        'Goa': (15.4909, 73.8278),
        'Hanoi': (21.0285, 105.8542),
        'Ho Chi Minh': (10.8231, 106.6297),
        'Hong Kong': (22.3193, 114.1694),
        'Istanbul': (41.0082, 28.9784),
        'Jaipur': (26.9124, 75.7873),
        'Jerusalem': (31.7683, 35.2137),
        'Kuala Lumpur': (3.1390, 101.6869),
        'Kyoto': (35.0116, 135.7681),
        'Lagos': (6.5244, 3.3792),
        'Lima': (-12.0464, -77.0428),
        'Lisbon': (38.7223, -9.1393),
        'London': (51.5074, -0.1278),
        'Los Angeles': (34.0522, -118.2437),
        'Madrid': (40.4168, -3.7038),
        'Manila': (14.5994, 120.9842),
        'Marrakech': (31.6295, -8.0088),
        'Mexico City': (19.4326, -99.1332),
        'Moscow': (55.7558, 37.6173),
        'Mumbai': (19.0760, 72.8777),
        'Nairobi': (-1.2870, 36.8172),
        'New York': (40.7128, -74.0060),
        'Paris': (48.8566, 2.3522),
        'Paris_Culture': (48.8566, 2.3522),
        'Paris_Extended': (48.8566, 2.3522),
        'Phuket': (7.8804, 98.3923),
        'Prague': (50.0755, 14.4378),
        'Rio de Janeiro': (-22.9068, -43.1729),
        'Rome': (41.9028, 12.4964),
        'Rome_Culture': (41.9028, 12.4964),
        'San Francisco': (37.7749, -122.4194),
        'Santiago': (-33.8688, -151.2093),
        'Seoul': (37.5665, 126.9780),
        'Shanghai': (31.2304, 121.4737),
        'Singapore': (1.3521, 103.8198),
        'Sydney': (-33.8688, 151.2093),
        'Taipei': (25.0330, 121.5654),
        'Tokyo': (35.6762, 139.6503),
        'Tokyo_Extended': (35.6762, 139.6503),
        'Toronto': (43.6532, -79.3832),
        'Venice': (45.4408, 12.3155),
        'Vienna': (48.2082, 16.3738),
        'Xian': (34.3416, 108.9398),
    }
    
    for city, coords in all_cities_coords.items():
        city_key = city.lower()
        if city_key in available_cities or city_key.replace('_', '') in [c.replace('_', '') for c in available_cities]:
            folium.Marker(
                location=coords,
                popup=f"<b>📍 {city.replace('_', ' ')}</b><br><i>Click to select</i>",
                tooltip=city.replace('_', ' '),
                icon=folium.Icon(color='red', icon='map-pin', prefix='fa')
            ).add_to(m)
    
    # Display map
    map_data = st_folium(m, width=700, height=500)

with dest_col:
    st.markdown("### 📍 Destination Info")
    if st.session_state.user_location:
        st.success(f"✅ Current: **{st.session_state.user_location['city']}**")
    else:
        st.info("👈 Click on map or set location")

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