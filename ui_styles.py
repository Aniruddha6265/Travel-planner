"""
ui_styles.py — Wanderlust-inspired CSS theming for the Travel Planner.
"""

import streamlit as st


def inject_css():
    """Inject custom wanderlust CSS into the Streamlit app."""
    st.markdown(
        """
    <style>
    /* ── Import Google Fonts ── */
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Inter:wght@300;400;500;600&display=swap');

    /* ── Color Variables ── */
    :root {
        --teal-deep: #0B3D3D;
        --teal-medium: #1A6B6B;
        --teal-light: #2D9B9B;
        --coral: #FF6B6B;
        --coral-light: #FF8E8E;
        --gold: #F4A261;
        --gold-light: #F7C59F;
        --cream: #FFF8F0;
        --cream-dark: #F0E6D6;
        --forest: #2D6A4F;
        --purple-soft: #7B68AE;
    }

    /* ── Global Overrides ── */
    .stApp {
        font-family: 'Inter', sans-serif;
    }

    /* ── Hero Header ── */
    .hero-header {
        background: linear-gradient(135deg, var(--teal-deep) 0%, var(--teal-medium) 50%, var(--teal-light) 100%);
        padding: 2rem 2.5rem;
        border-radius: 16px;
        margin-bottom: 1.5rem;
        color: white;
        text-align: center;
        position: relative;
        overflow: hidden;
    }
    .hero-header::before {
        content: '';
        position: absolute;
        top: -50%;
        right: -20%;
        width: 300px;
        height: 300px;
        background: radial-gradient(circle, rgba(244,162,97,0.2) 0%, transparent 70%);
        border-radius: 50%;
    }
    .hero-header h1 {
        font-family: 'Playfair Display', serif;
        font-size: 2.2rem;
        font-weight: 700;
        margin: 0 0 0.3rem 0;
        color: white !important;
    }
    .hero-header p {
        font-size: 1.05rem;
        opacity: 0.9;
        margin: 0;
        font-weight: 300;
    }

    /* ── Destination Cards ── */
    .dest-card {
        background: white;
        border-radius: 14px;
        padding: 1.5rem;
        box-shadow: 0 4px 20px rgba(11, 61, 61, 0.08);
        border: 1px solid rgba(11, 61, 61, 0.06);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        height: 100%;
    }
    .dest-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 30px rgba(11, 61, 61, 0.15);
    }
    .dest-card h3 {
        font-family: 'Playfair Display', serif;
        color: var(--teal-deep);
        margin: 0 0 0.5rem 0;
        font-size: 1.3rem;
    }
    .dest-card .country {
        color: var(--teal-medium);
        font-size: 0.9rem;
        font-weight: 500;
        margin-bottom: 0.8rem;
    }
    .dest-card .description {
        color: #555;
        font-size: 0.92rem;
        line-height: 1.5;
        margin-bottom: 1rem;
    }

    /* ── Match Score Badge ── */
    .match-score {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: linear-gradient(135deg, var(--coral), var(--coral-light));
        color: white;
        padding: 4px 14px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        margin-bottom: 0.8rem;
    }

    /* ── Tag Pills ── */
    .tag-container {
        display: flex;
        flex-wrap: wrap;
        gap: 6px;
        margin: 0.8rem 0;
    }
    .tag-pill {
        background: var(--cream);
        color: var(--teal-deep);
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.78rem;
        font-weight: 500;
        border: 1px solid rgba(11, 61, 61, 0.1);
    }
    .tag-pill.interest {
        background: linear-gradient(135deg, #E8F4F2, #D0EBE7);
        border-color: var(--teal-light);
    }
    .tag-pill.budget {
        background: linear-gradient(135deg, #FFF3E8, #FFE8D0);
        border-color: var(--gold);
        color: #8B5E3C;
    }

    /* ── Day Card (Itinerary) ── */
    .day-card {
        background: white;
        border-radius: 14px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 2px 12px rgba(11, 61, 61, 0.06);
        border-left: 4px solid var(--teal-medium);
    }
    .day-card .day-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 1rem;
    }
    .day-card .day-number {
        font-family: 'Playfair Display', serif;
        font-size: 1.2rem;
        color: var(--teal-deep);
        font-weight: 700;
    }
    .day-card .day-theme {
        color: var(--coral);
        font-size: 0.9rem;
        font-weight: 500;
    }
    .day-card .cluster-badge {
        background: var(--cream);
        color: var(--teal-medium);
        padding: 3px 10px;
        border-radius: 12px;
        font-size: 0.75rem;
        font-weight: 500;
        border: 1px solid rgba(26, 107, 107, 0.15);
    }

    /* ── Activity Timeline ── */
    .activity-item {
        display: flex;
        gap: 1rem;
        padding: 0.8rem 0;
        border-bottom: 1px solid rgba(11, 61, 61, 0.06);
    }
    .activity-item:last-child {
        border-bottom: none;
    }
    .activity-time {
        min-width: 80px;
        color: var(--teal-medium);
        font-weight: 600;
        font-size: 0.85rem;
        padding-top: 2px;
    }
    .activity-content {
        flex: 1;
    }
    .activity-content .activity-name {
        font-weight: 600;
        color: var(--teal-deep);
        font-size: 0.95rem;
        margin-bottom: 3px;
    }
    .activity-content .activity-desc {
        color: #666;
        font-size: 0.85rem;
        line-height: 1.4;
    }
    .activity-cost {
        min-width: 70px;
        text-align: right;
        color: var(--forest);
        font-weight: 600;
        font-size: 0.9rem;
        padding-top: 2px;
    }

    /* ── Period Labels ── */
    .period-label {
        display: inline-block;
        padding: 3px 10px;
        border-radius: 8px;
        font-size: 0.72rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 4px;
    }
    .period-morning { background: #FFF3E0; color: #E65100; }
    .period-lunch { background: #E8F5E9; color: #2E7D32; }
    .period-afternoon { background: #E3F2FD; color: #1565C0; }
    .period-evening { background: #F3E5F5; color: #7B1FA2; }

    /* ── Budget Tracker ── */
    .budget-tracker {
        background: white;
        border-radius: 14px;
        padding: 1.2rem 1.5rem;
        box-shadow: 0 2px 12px rgba(11, 61, 61, 0.06);
        margin: 1rem 0;
    }
    .budget-bar-container {
        background: var(--cream-dark);
        border-radius: 10px;
        height: 24px;
        overflow: hidden;
        margin: 0.5rem 0;
    }
    .budget-bar-fill {
        height: 100%;
        border-radius: 10px;
        background: linear-gradient(90deg, var(--teal-medium), var(--teal-light));
        transition: width 0.5s ease;
        display: flex;
        align-items: center;
        justify-content: flex-end;
        padding-right: 8px;
        color: white;
        font-size: 0.75rem;
        font-weight: 600;
    }
    .budget-bar-fill.over-budget {
        background: linear-gradient(90deg, var(--coral), #FF4444);
    }

    /* ── Metric Cards ── */
    .metric-row {
        display: flex;
        gap: 1rem;
        margin: 1rem 0;
    }
    .metric-card {
        flex: 1;
        background: white;
        border-radius: 12px;
        padding: 1rem 1.2rem;
        text-align: center;
        box-shadow: 0 2px 10px rgba(11, 61, 61, 0.06);
        border: 1px solid rgba(11, 61, 61, 0.05);
    }
    .metric-card .metric-value {
        font-family: 'Playfair Display', serif;
        font-size: 1.5rem;
        color: var(--teal-deep);
        font-weight: 700;
    }
    .metric-card .metric-label {
        font-size: 0.8rem;
        color: #888;
        margin-top: 2px;
        font-weight: 500;
    }

    /* ── Swap Diff Styling ── */
    .swap-old {
        background: #FFEBEE;
        border-left: 3px solid var(--coral);
        padding: 0.6rem 1rem;
        border-radius: 6px;
        margin-bottom: 0.5rem;
        text-decoration: line-through;
        color: #999;
        font-size: 0.9rem;
    }
    .swap-new {
        background: #E8F5E9;
        border-left: 3px solid var(--forest);
        padding: 0.6rem 1rem;
        border-radius: 6px;
        font-size: 0.9rem;
        color: var(--teal-deep);
    }

    /* ── Trip History Table ── */
    .trip-history-card {
        background: white;
        border-radius: 12px;
        padding: 1rem 1.2rem;
        margin-bottom: 0.8rem;
        box-shadow: 0 2px 8px rgba(11, 61, 61, 0.05);
        border: 1px solid rgba(11, 61, 61, 0.06);
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    /* ── Section Titles ── */
    .section-title {
        font-family: 'Playfair Display', serif;
        color: var(--teal-deep);
        font-size: 1.4rem;
        margin: 1.5rem 0 0.8rem 0;
        padding-bottom: 0.3rem;
        border-bottom: 2px solid var(--gold);
        display: inline-block;
    }

    /* ── Streamlit Tab Overrides ── */
    .stTabs [data-baseweb="tab-list"] {
        gap: 4px;
    }
    .stTabs [data-baseweb="tab"] {
        border-radius: 10px 10px 0 0;
        padding: 10px 20px;
        font-weight: 500;
    }
    .stTabs [aria-selected="true"] {
        background: var(--teal-deep) !important;
        color: white !important;
    }

    /* ── Sidebar Styling ── */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0B3D3D 0%, #0F4F4F 100%);
    }
    [data-testid="stSidebar"] * {
        color: white !important;
    }
    [data-testid="stSidebar"] .stSelectbox label,
    [data-testid="stSidebar"] .stTextInput label,
    [data-testid="stSidebar"] .stMultiSelect label,
    [data-testid="stSidebar"] .stDateInput label,
    [data-testid="stSidebar"] .stSlider label,
    [data-testid="stSidebar"] .stNumberInput label {
        color: var(--gold-light) !important;
        font-weight: 500;
    }

    /* ── Smooth Transitions ── */
    * {
        transition: background-color 0.2s ease;
    }

    /* ── Scrollbar ── */
    ::-webkit-scrollbar {
        width: 6px;
    }
    ::-webkit-scrollbar-thumb {
        background: var(--teal-light);
        border-radius: 3px;
    }
    ::-webkit-scrollbar-track {
        background: var(--cream);
    }
    </style>
    """,
        unsafe_allow_html=True,
    )
