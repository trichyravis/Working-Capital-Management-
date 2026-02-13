
"""
Working Capital AI Agent - Mountain Path Edition
Now with Current Assets & Current Liabilities Structure

The Mountain Path - World of Finance
Prof. V. Ravichandran
"""

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression, LinearRegression

# ============================================================================
# BRANDING & STYLING
# ============================================================================

COLORS = {
    'dark_blue': '#003366',
    'medium_blue': '#004d80',
    'light_blue': '#ADD8E6',
    'accent_gold': '#FFD700',
    'bg_dark': '#0a1628',
    'card_bg': '#112240',
    'text_primary': '#e6f1ff',
    'text_secondary': '#8892b0',
    'success': '#28a745',
    'danger': '#dc3545',
}

BRANDING = {
    'name': 'The Mountain Path - World of Finance',
    'instructor': 'Prof. V. Ravichandran',
    'credentials': '28+ Years Corporate Finance & Banking | 10+ Years Academic Excellence',
    'icon': '🏔️',
}

PAGE_CONFIG = {
    'page_title': 'Working Capital AI Agent | Mountain Path',
    'page_icon': '🏔️',
    'layout': 'wide',
    'initial_sidebar_state': 'expanded',
}


def apply_styles():
    st.markdown(f"""
    <style>
        .stApp {{
            background: linear-gradient(135deg, {COLORS['bg_dark']} 0%, {COLORS['dark_blue']} 50%, #0d2137 100%);
        }}

        section[data-testid="stSidebar"] {{
            background: linear-gradient(180deg, {COLORS['bg_dark']} 0%, {COLORS['dark_blue']} 100%);
        }}

        /* Sidebar text */
        section[data-testid="stSidebar"] label,
        section[data-testid="stSidebar"] p,
        section[data-testid="stSidebar"] span {{
            color: {COLORS['text_primary']} !important;
        }}

        section[data-testid="stSidebar"] input {{
            background-color: white !important;
            color: black !important;
        }}

        /* ===== TAB FIX ===== */

        .stTabs [data-baseweb="tab-list"] {{
            gap: 8px;
        }}

        .stTabs [data-baseweb="tab"] {{
            background: {COLORS['card_bg']};
            border: 1px solid rgba(255,215,0,0.3);
            border-radius: 8px;
            color: {COLORS['text_primary']} !important;
            font-weight: 600;
            padding: 8px 16px;
        }}

        .stTabs [aria-selected="true"] {{
            background: {COLORS['dark_blue']} !important;
            border: 2px solid {COLORS['accent_gold']} !important;
            color: {COLORS['accent_gold']} !important;
        }}

        /* Header */
        .header-container {{
    background: linear-gradient(135deg, {COLORS['dark_blue']}, {COLORS['medium_blue']});
    border: 2px solid {COLORS['accent_gold']};
    border-radius: 12px;
    padding: 1.8rem;
    margin-bottom: 1.5rem;
    text-align: center;
}}

.header-container h1 {{
    color: {COLORS['accent_gold']} !important;
    font-size: 2.2rem;
    font-weight: 700;
    margin-bottom: 0.5rem;
}}

.header-container p {{
    color: {COLORS['text_primary']} !important;
    font-size: 0.95rem;
    opacity: 0.9;
}}




# ============================================================================
# MAIN
# ============================================================================

def main():
    st.set_page_config(**PAGE_CONFIG)
    apply_styles()

    st.markdown(f"""
    <div class="header-container">
        <h1>{BRANDING['icon']} Working Capital AI Agent</h1>
        <p>{BRANDING['name']}</p>
        <p>{BRANDING['instructor']} | {BRANDING['credentials']}</p>
    </div>
    """, unsafe_allow_html=True)

    # ================= SIDEBAR =================

    st.sidebar.markdown("### 🧾 Current Assets")

    cash = st.sidebar.number_input("Cash", 2000000)
    receivables = st.sidebar.number_input("Accounts Receivable", 5000000)
    inventory = st.sidebar.number_input("Inventory", 3000000)
    other_ca = st.sidebar.number_input("Other Current Assets", 500000)

    st.sidebar.markdown("### 💳 Current Liabilities")

    payables = st.sidebar.number_input("Accounts Payable", 3500000)
    short_debt = st.sidebar.number_input("Short-Term Debt", 1500000)
    other_cl = st.sidebar.number_input("Other Current Liabilities", 400000)

    # ================= CALCULATIONS =================

    total_ca = cash + receivables + inventory + other_ca
    total_cl = payables + short_debt + other_cl

    net_working_capital = total_ca - total_cl
    current_ratio = total_ca / total_cl if total_cl != 0 else 0
    quick_ratio = (cash + receivables) / total_cl if total_cl != 0 else 0

    # ================= TABS =================

    tab1, tab2 = st.tabs(["📊 Balance Sheet View", "📈 Working Capital Metrics"])

    with tab1:
        st.markdown('<div class="section-title">Balance Sheet Snapshot</div>', unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("#### Current Assets")
            st.dataframe(pd.DataFrame({
                "Component": ["Cash", "Receivables", "Inventory", "Other CA", "Total CA"],
                "Amount": [cash, receivables, inventory, other_ca, total_ca]
            }), use_container_width=True, hide_index=True)

        with col2:
            st.markdown("#### Current Liabilities")
            st.dataframe(pd.DataFrame({
                "Component": ["Payables", "Short-Term Debt", "Other CL", "Total CL"],
                "Amount": [payables, short_debt, other_cl, total_cl]
            }), use_container_width=True, hide_index=True)

    with tab2:
        st.markdown('<div class="section-title">Working Capital Analytics</div>', unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown(f'<div class="metric-card"><div class="label">Net Working Capital</div><div class="value">{net_working_capital:,.0f}</div></div>', unsafe_allow_html=True)

        with col2:
            st.markdown(f'<div class="metric-card"><div class="label">Current Ratio</div><div class="value">{current_ratio:.2f}</div></div>', unsafe_allow_html=True)

        with col3:
            st.markdown(f'<div class="metric-card"><div class="label">Quick Ratio</div><div class="value">{quick_ratio:.2f}</div></div>', unsafe_allow_html=True)

        st.markdown("### Liquidity Status")

        if current_ratio >= 1.5:
            st.success("Strong liquidity position.")
        elif current_ratio >= 1:
            st.warning("Moderate liquidity. Monitor closely.")
        else:
            st.error("Liquidity risk detected.")


    st.divider()
    st.markdown(f"""
    <div style="text-align:center;">
        <p style="color:{COLORS['accent_gold']}; font-weight:bold;">
        {BRANDING['icon']} {BRANDING['name']}</p>
        <p style="color:{COLORS['text_secondary']}; font-size:0.8rem;">
        {BRANDING['instructor']} | {BRANDING['credentials']}</p>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
