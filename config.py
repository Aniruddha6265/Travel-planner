"""
config.py — Session state initialization and API key management.
"""

import streamlit as st
from datetime import date, timedelta


def init_session_state():
    """Initialize all session state keys with sensible defaults."""
    defaults = {
        # API configuration
        "api_key": "",
        "api_provider": "Gemini",
        "demo_mode": True,
        # Trip preferences
        "preferences": {
            "destination": "",
            "vibe": "Cultural",
            "duration": 3,
            "start_date": date.today() + timedelta(days=30),
            "budget_level": "Moderate",
            "travel_party": "Solo",
            "pace": "Moderate",
            "interests": ["Food", "History"],
        },
        # Generated data
        "recommendations": None,
        "itinerary": None,
        "swap_history": [],
        # Trip persistence
        "saved_trips": {},
        # UI state
        "active_tab": 0,
        "generating": False,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def render_api_config():
    """Render API key configuration in the sidebar."""
    st.sidebar.markdown("### 🔑 API Configuration")

    provider = st.sidebar.selectbox(
        "LLM Provider",
        ["Gemini", "Groq"],
        index=0 if st.session_state.api_provider == "Gemini" else 1,
        help="Choose your LLM provider. Both offer free tiers.",
    )
    st.session_state.api_provider = provider

    api_key = st.sidebar.text_input(
        f"{provider} API Key",
        type="password",
        value=st.session_state.api_key,
        placeholder=f"Enter your {provider} API key...",
        help=f"Get a free key from {'aistudio.google.com' if provider == 'Gemini' else 'console.groq.com'}",
    )
    st.session_state.api_key = api_key

    demo_mode = st.sidebar.toggle(
        "🎭 Demo Mode",
        value=st.session_state.demo_mode if not api_key else False,
        help="Use pre-built demo data — no API key needed!",
        disabled=False,
    )
    st.session_state.demo_mode = demo_mode or (not api_key)

    if st.session_state.demo_mode:
        st.sidebar.info("✨ **Demo Mode active** — using sample data. Add an API key for live generation.")
    else:
        st.sidebar.success(f"✅ Connected to **{provider}**")

    st.sidebar.markdown("---")
