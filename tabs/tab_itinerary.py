"""
tabs/tab_itinerary.py — Tab 2: Day-by-Day Optimized Itinerary Generator.
Geographic clustering, itemized costs, and cumulative budget tracking.
"""

import streamlit as st
from llm_client import LLMClient


# Period → CSS class mapping
PERIOD_CLASSES = {
    "Morning Sightseeing": "period-morning",
    "Lunch": "period-lunch",
    "Afternoon Leisure": "period-afternoon",
    "Evening Dining & Entertainment": "period-evening",
}

# Category emoji mapping
CATEGORY_EMOJI = {
    "attraction": "🏛️",
    "dining": "🍽️",
    "exploration": "🚶",
    "entertainment": "🎭",
    "shopping": "🛍️",
    "transport": "🚃",
}


def render_itinerary():
    """Render the Day-by-Day Itinerary Generator tab."""
    st.markdown('<div class="section-title">📅 Day-by-Day Optimized Itinerary</div>', unsafe_allow_html=True)

    prefs = st.session_state.preferences
    destination = prefs.get("destination", "").strip()

    if not destination:
        st.warning(
            "⚠️ Please set a destination first! Either enter one in the sidebar, "
            "or use **Tab 1** to find the perfect city."
        )
        return

    st.markdown(
        f"Generate a **{prefs['duration']}-day** itinerary for **{destination}** "
        f"with {prefs['pace'].lower()} pace, {prefs['budget_level'].lower()} budget, "
        f"optimized for geographic clustering."
    )

    col1, col2 = st.columns([1, 3])
    with col1:
        generate_btn = st.button(
            "🗺️ Generate Itinerary",
            type="primary",
            use_container_width=True,
        )

    if generate_btn:
        with st.spinner(f"✨ Crafting your perfect {destination} itinerary..."):
            client = LLMClient(
                provider=st.session_state.api_provider,
                api_key=st.session_state.api_key,
                demo_mode=st.session_state.demo_mode,
            )
            itinerary = client.generate_itinerary(prefs)
            st.session_state.itinerary = itinerary
            st.session_state.swap_history = []

    # Display itinerary
    itinerary = st.session_state.get("itinerary")
    if not itinerary:
        st.info("👆 Click **Generate Itinerary** to create your personalized travel plan.")
        return

    _render_budget_overview(itinerary, prefs)
    st.markdown("---")
    _render_day_cards(itinerary)
    _render_budget_summary_table(itinerary)


def _render_budget_overview(itinerary: dict, prefs: dict):
    """Render the budget overview metrics and progress bar."""
    total_usd = itinerary.get("trip_total_usd", 0)
    total_inr = itinerary.get("trip_total_inr", 0)
    total_local = itinerary.get("trip_total_local", 0)
    currency = itinerary.get("currency", "USD")
    currency_symbol = itinerary.get("currency_symbol", "$")
    days_count = len(itinerary.get("days", []))

    # Budget thresholds
    budget_limits = {"Budget": 50, "Moderate": 120, "Luxury": 300}
    daily_limit = budget_limits.get(prefs.get("budget_level", "Moderate"), 120)
    total_limit = daily_limit * days_count
    avg_daily = total_usd / days_count if days_count else 0
    pct = min((total_usd / total_limit) * 100, 100) if total_limit else 0
    over_budget = total_usd > total_limit

    # Metrics row
    metrics_html = f"""
    <div class="metric-row">
        <div class="metric-card">
            <div class="metric-value">{currency_symbol}{total_local}</div>
            <div class="metric-label">Total ({currency})</div>
        </div>
        <div class="metric-card">
            <div class="metric-value">${total_usd:.0f}</div>
            <div class="metric-label">Total (USD)</div>
        </div>
        <div class="metric-card">
            <div class="metric-value">₹{total_inr:.0f}</div>
            <div class="metric-label">Total (INR)</div>
        </div>
        <div class="metric-card">
            <div class="metric-value">${avg_daily:.0f}</div>
            <div class="metric-label">Avg per Day</div>
        </div>
    </div>
    """
    st.markdown(metrics_html, unsafe_allow_html=True)

    # Budget progress bar
    bar_class = "over-budget" if over_budget else ""
    budget_html = f"""
    <div class="budget-tracker">
        <div style="display: flex; justify-content: space-between; font-size: 0.85rem;">
            <span><strong>Budget Tracker</strong></span>
            <span>${total_usd:.0f} / ${total_limit:.0f} ({prefs.get('budget_level', 'Moderate')})</span>
        </div>
        <div class="budget-bar-container">
            <div class="budget-bar-fill {bar_class}" style="width: {pct:.0f}%;">
                {pct:.0f}%
            </div>
        </div>
        {'<span style="color: #FF4444; font-size: 0.8rem;">⚠️ Over budget!</span>' if over_budget else ''}
    </div>
    """
    st.markdown(budget_html, unsafe_allow_html=True)


def _render_day_cards(itinerary: dict):
    """Render expandable day cards with activity timelines."""
    currency_symbol = itinerary.get("currency_symbol", "$")
    days = itinerary.get("days", [])

    cumulative = 0
    for day_data in days:
        day_num = day_data.get("day", 0)
        theme = day_data.get("theme", "")
        cluster = day_data.get("neighborhood_cluster", "")
        day_total = day_data.get("day_total_usd", 0)
        cumulative += day_total

        with st.expander(f"📍 Day {day_num} — {theme}", expanded=(day_num <= 2)):
            # Cluster badge
            if cluster:
                st.markdown(
                    f'<span class="cluster-badge" style="display:inline-block;background:#E8F4F2;color:#1A6B6B;'
                    f'padding:3px 12px;border-radius:12px;font-size:0.8rem;margin-bottom:10px;">'
                    f'📌 {cluster}</span>',
                    unsafe_allow_html=True,
                )

            # Activities
            for slot in day_data.get("slots", []):
                _render_activity_slot(slot, currency_symbol)

            # Day summary
            st.markdown(
                f'<div style="text-align:right;margin-top:8px;padding-top:8px;border-top:2px solid #F4A261;">'
                f'<strong>Day Total: {currency_symbol}{day_data.get("day_total_local", 0)} '
                f'(${day_total:.0f} USD)</strong> &nbsp;|&nbsp; '
                f'Running Total: <strong>${cumulative:.0f} USD</strong></div>',
                unsafe_allow_html=True,
            )


def _render_activity_slot(slot: dict, currency_symbol: str):
    """Render a single activity slot in the timeline."""
    time = slot.get("time", "")
    period = slot.get("period", "")
    activity = slot.get("activity", "")
    description = slot.get("description", "")
    cost_local = slot.get("cost_local", 0)
    cost_usd = slot.get("cost_usd", 0)
    category = slot.get("category", "")

    period_class = PERIOD_CLASSES.get(period, "period-morning")
    emoji = CATEGORY_EMOJI.get(category, "📍")

    html = f"""
    <div class="activity-item">
        <div class="activity-time">{time}</div>
        <div class="activity-content">
            <span class="period-label {period_class}">{period}</span>
            <div class="activity-name">{emoji} {activity}</div>
            <div class="activity-desc">{description}</div>
        </div>
        <div class="activity-cost">
            {currency_symbol}{cost_local}
            <div style="font-size:0.7rem;color:#888;">${cost_usd:.0f}</div>
        </div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)


def _render_budget_summary_table(itinerary: dict):
    """Render the final budget summary table."""
    st.markdown("---")
    st.markdown('<div class="section-title">💰 Budget Summary</div>', unsafe_allow_html=True)

    currency = itinerary.get("currency", "USD")
    currency_symbol = itinerary.get("currency_symbol", "$")
    rate_to_inr = itinerary.get("exchange_rate_to_inr", 83.5)
    rate_to_usd = itinerary.get("exchange_rate_to_usd", 1.0)

    import pandas as pd

    rows = []
    for day in itinerary.get("days", []):
        day_usd = day.get("day_total_usd", 0)
        day_local = day.get("day_total_local", 0)
        day_inr = day_usd * (rate_to_inr / rate_to_usd) if rate_to_usd else 0
        rows.append({
            "Day": f"Day {day['day']}",
            "Theme": day.get("theme", ""),
            f"Cost ({currency})": f"{currency_symbol}{day_local}",
            "Cost (USD)": f"${day_usd:.2f}",
            "Cost (INR)": f"₹{day_inr:.0f}",
        })

    # Totals row
    total_usd = itinerary.get("trip_total_usd", 0)
    total_local = itinerary.get("trip_total_local", 0)
    total_inr = itinerary.get("trip_total_inr", 0)
    rows.append({
        "Day": "**TOTAL**",
        "Theme": "",
        f"Cost ({currency})": f"**{currency_symbol}{total_local}**",
        "Cost (USD)": f"**${total_usd:.2f}**",
        "Cost (INR)": f"**₹{total_inr:.0f}**",
    })

    df = pd.DataFrame(rows)
    st.dataframe(df, use_container_width=True, hide_index=True)

    st.caption(
        "💡 *All costs are estimates based on average prices. Actual costs may vary. "
        f"Exchange rates: 1 {currency} ≈ ${rate_to_usd} USD ≈ ₹{rate_to_inr} INR.*"
    )
