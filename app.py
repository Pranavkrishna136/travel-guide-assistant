"""
Streamlit app for Travel Guide Assistant.
"""

import streamlit as st
import os
from travel_assistant import TravelAssistant

st.set_page_config(page_title="Travel Guide Assistant", page_icon="🗺️")

st.title("🗺️ Travel Guide Assistant")
st.markdown("Generate personalized travel itineraries using AI and curated travel data.")

# Sidebar for inputs
st.sidebar.header("Trip Details")
destination = st.sidebar.text_input("Destination", "Paris")
days = st.sidebar.slider("Duration (days)", 1, 14, 3)
budget = st.sidebar.number_input("Budget ($)", 100, 10000, 700)
preferences = st.sidebar.text_area("Preferences (optional)", "Family-friendly, include museums")

# API Key
api_key = st.sidebar.text_input("OpenAI API Key", type="password")
if not api_key:
    st.sidebar.warning("Please enter your OpenAI API key to generate itineraries.")

# Main content
if st.button("Generate Itinerary"):
    if not api_key:
        st.error("Please provide an OpenAI API key.")
    else:
        with st.spinner("Generating your itinerary..."):
            try:
                assistant = TravelAssistant()
                assistant.set_openai_client(api_key)
                itinerary = assistant.generate_itinerary(destination, days, budget, preferences)
                st.success("Itinerary generated!")
                st.markdown(itinerary)
            except Exception as e:
                st.error(f"Error: {str(e)}")

st.markdown("---")
st.markdown("**Note:** This is a demo app. For production, ensure data privacy and API key security.")