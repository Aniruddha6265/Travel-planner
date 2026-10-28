"""
tabs/tab_preferences.py — Sidebar trip preference form.
"""

import streamlit as st
from datetime import date, timedelta


def render_preferences():
    """Render the comprehensive trip preference form in the sidebar."""
    st.sidebar.markdown("### 🌍 Trip Preferences")

    prefs = st.session_state.preferences

    # Destination input
    destination = st.sidebar.text_input(
        "📍 Destination",
        value=prefs.get("destination", ""),
        placeholder="e.g., Paris, Tokyo, or leave blank for recommendations",
        help="Leave blank to get AI-powered destination recommendations in Tab 1.",
    )
    prefs["destination"] = destination

    # Vibe / Travel Mood
    vibe_options = ["Beach", "Mountains", "Cultural", "Urban"]
    vibe = st.sidebar.selectbox(
        "✨ Travel Vibe",
        vibe_options,
        index=vibe_options.index(prefs.get("vibe", "Cultural")),
        help="What mood are you going for?",
    )
    prefs["vibe"] = vibe

    # Trip Duration
    duration = st.sidebar.slider(
        "📅 Trip Duration (days)",
        min_value=1,
        max_value=14,
        value=prefs.get("duration", 3),
        help="Number of full days at your destination.",
    )
    prefs["duration"] = duration

    # Travel Dates
    start_date = st.sidebar.date_input(
        "🗓️ Travel Start Date",
        value=prefs.get("start_date", date.today() + timedelta(days=30)),
        min_value=date.today(),
        help="When do you plan to start your trip?",
    )
    prefs["start_date"] = start_date

    # Budget Level
    budget_options = ["Budget", "Moderate", "Luxury"]
    budget = st.sidebar.selectbox(
        "💰 Budget Level",
        budget_options,
        index=budget_options.index(prefs.get("budget_level", "Moderate")),
    )
    prefs["budget_level"] = budget

    # Travel Party
    party_options = ["Solo", "Couple", "Family", "Friends"]
    party = st.sidebar.selectbox(
        "👥 Travel Party",
        party_options,
        index=party_options.index(prefs.get("travel_party", "Solo")),
    )
    prefs["travel_party"] = party

    # Pace
    pace_options = ["Relaxed", "Moderate", "Fast-Paced"]
    pace = st.sidebar.selectbox(
        "🚶 Travel Pace",
        pace_options,
        index=pace_options.index(prefs.get("pace", "Moderate")),
    )
    prefs["pace"] = pace

    # Interests (multi-select)
    interest_options = [
        "Food", "Adventure", "History", "Nightlife",
        "Art & Museums", "Nature", "Shopping", "Photography",
        "Wellness & Spa", "Architecture",
    ]
    interests = st.sidebar.multiselect(
        "❤️ Interests",
        interest_options,
        default=prefs.get("interests", ["Food", "History"]),
        help="Select all interests that apply to your trip.",
    )
    prefs["interests"] = interests

    st.session_state.preferences = prefs

    # Summary card
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📋 Trip Summary")

    summary_parts = [
        f"**Destination:** {destination or 'TBD (see Tab 1)'}",
        f"**Vibe:** {vibe} | **Duration:** {duration} days",
        f"**Budget:** {budget} | **Party:** {party}",
        f"**Pace:** {pace}",
        f"**Interests:** {', '.join(interests) if interests else 'None selected'}",
    ]
    st.sidebar.markdown("\n\n".join(summary_parts))
