"""
tabs/tab_recommender.py — Tab 1: Smart Destination Recommender.
Recommends top 3 cities based on user preferences using LLM.
"""

import streamlit as st
from llm_client import LLMClient


def render_recommender():
    """Render the Smart Destination Recommender tab."""
    st.markdown('<div class="section-title">🧭 Smart Destination Recommender</div>', unsafe_allow_html=True)

    prefs = st.session_state.preferences
    has_destination = bool(prefs.get("destination", "").strip())

    if has_destination:
        st.info(
            f"🎯 You've already set **{prefs['destination']}** as your destination. "
            "This tab is for when you're undecided! Clear the destination in the sidebar to use recommendations."
        )

    st.markdown(
        "Not sure where to go? Tell us your **vibe**, **budget**, and **interests** in the sidebar, "
        "and we'll recommend the perfect destinations for you!"
    )

    col1, col2 = st.columns([1, 3])
    with col1:
        generate_btn = st.button(
            "🔮 Find My Destinations",
            type="primary",
            use_container_width=True,
        )

    if generate_btn:
        with st.spinner("🌍 Analyzing your travel personality..."):
            client = LLMClient(
                provider=st.session_state.api_provider,
                api_key=st.session_state.api_key,
                demo_mode=st.session_state.demo_mode,
            )
            result = client.get_recommendations(prefs)
            st.session_state.recommendations = result

    # Display recommendations
    recommendations = st.session_state.get("recommendations")
    if recommendations and "recommendations" in recommendations:
        recs = recommendations["recommendations"]
        st.markdown("---")
        st.markdown(f"### ✨ Top {len(recs)} Destinations For You")

        cols = st.columns(len(recs))
        for idx, (col, rec) in enumerate(zip(cols, recs)):
            with col:
                _render_destination_card(rec, idx)


def _render_destination_card(rec: dict, index: int):
    """Render a single destination recommendation card."""
    city = rec.get("city", "Unknown")
    country = rec.get("country", "")
    score = rec.get("match_score", 0)
    tags = rec.get("highlight_tags", [])
    cost = rec.get("avg_daily_cost_usd", 0)
    season = rec.get("best_season", "Year-round")
    description = rec.get("description", "")

    # Build tag HTML
    tags_html = "".join(
        f'<span class="tag-pill interest">{tag}</span>' for tag in tags
    )

    card_html = f"""
    <div class="dest-card">
        <div class="match-score">🎯 {score}% Match</div>
        <h3>{city}</h3>
        <div class="country">📍 {country}</div>
        <div class="description">{description}</div>
        <div class="tag-container">{tags_html}</div>
        <div style="margin-top: 0.8rem; display: flex; justify-content: space-between; align-items: center;">
            <span class="tag-pill budget">💰 ~${cost}/day</span>
            <span style="font-size: 0.8rem; color: #888;">📅 {season}</span>
        </div>
    </div>
    """
    st.markdown(card_html, unsafe_allow_html=True)

    # "Use this destination" button
    if st.button(f"✅ Choose {city}", key=f"choose_{index}", use_container_width=True):
        st.session_state.preferences["destination"] = city
        st.success(f"🎉 **{city}** set as your destination! Head to Tab 2 to generate your itinerary.")
        st.rerun()
