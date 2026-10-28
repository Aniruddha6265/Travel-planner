"""
app.py — Personalized Travel Itinerary Planner
Skill Wallet Capstone Project 4

A production-ready Streamlit application that recommends destinations,
generates optimized day-by-day itineraries with geographic clustering
and budget tracking, supports dynamic activity swaps, and exports
beautiful offline PDFs.

Run: streamlit run app.py
"""

import streamlit as st

# ── Page Config (must be first Streamlit call) ──
st.set_page_config(
    page_title="✈️ Travel Itinerary Planner",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Initialize ──
from config import init_session_state, render_api_config
from ui_styles import inject_css

init_session_state()
inject_css()

# ── Hero Header ──
st.markdown(
    """
    <div class="hero-header">
        <h1>✈️ Personalized Travel Itinerary Planner</h1>
        <p>AI-powered destination recommendations • Optimized day-by-day plans • Beautiful PDF exports</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ── Sidebar ──
render_api_config()

from tabs.tab_preferences import render_preferences
render_preferences()

# ── Main Tabs ──
tab1, tab2, tab3, tab4 = st.tabs([
    "🧭 Destination Recommender",
    "📅 Itinerary Generator",
    "🎨 Vibe Customizer",
    "💼 Trip Manager & PDF",
])

from tabs.tab_recommender import render_recommender
from tabs.tab_itinerary import render_itinerary
from tabs.tab_customizer import render_customizer
from tabs.tab_manager import render_manager

with tab1:
    render_recommender()

with tab2:
    render_itinerary()

with tab3:
    render_customizer()

with tab4:
    render_manager()

# ── Footer ──
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; padding: 1rem; color: #888; font-size: 0.8rem;">
        <p>Built with ❤️ using Streamlit & AI · Skill Wallet Capstone Project 4</p>
        <p>
            <span class="tag-pill interest">Gemini</span>
            <span class="tag-pill interest">Groq</span>
            <span class="tag-pill interest">Streamlit</span>
            <span class="tag-pill interest">FPDF2</span>
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)
