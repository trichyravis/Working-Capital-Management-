
"""
Working Capital AI Agent - Mountain Path Edition
Restored Original Design + Advanced Analytics
"""

import streamlit as st
import pandas as pd

# ==========================================================
# BRANDING
# ==========================================================

COLORS = {
    'dark_blue': '#003366',
    'medium_blue': '#004d80',
    'accent_gold': '#FFD700',
    'bg_dark': '#0a1628',
    'card_bg': '#112240',
    'text_primary': '#e6f1ff',
    'text_secondary': '#8892b0',
    'success': '#2ecc71',
    'warning': '#f39c12',
    'danger': '#e74c3c'
}

BRANDING = {
    'name': 'The Mountain Path - World of Finance',
    'instructor': 'Prof. V. Ravichandran',
    'credentials': '28+ Years Corporate Finance & Banking | 10+ Years Academic Excellence',
    'icon': '🏔️',
}

# ==========================================================
# STYLING (YOUR ORIGINAL STYLE RESTORED)
# ==========================================================

def apply_styles():
    st.markdown(f"""
    <style>
    .stApp {{
        background: linear-gradient(135deg, {COLORS['bg_dark']} 0%, {COLORS['dark_blue']} 50%, #0d2137 100%);
    }}

    section[data-testid="stSidebar"] {{
        background: linear-gradient(180deg, {COLORS['bg_dark']} 0%, {COLORS['dark_blue']} 100%);
    }}

    section[data-testid="stSidebar"] * {{
        color: {COLORS['text_primary']} !important;
    }}

    .header-container {{
        background: linear-gradient(135deg, {COLORS['dark_blue']}, {COLORS['medium_blue']});
        border: 2px solid {COLORS['accent_gold']};
        border-radius: 12px;
        padding: 2rem;
        margin-bottom: 2rem;
        text-align: center;
    }}

    .header-container h1 {{
        color: {COLORS['accent_gold']} !important;
        font-size: 2.2rem;
    }}

    .header-container p {{
        color: {COLORS['text_primary']} !important;
    }}

    .stTabs [data-baseweb="tab"] {{
        background: {COLORS['card_bg']};
        border-radius: 8px;
        color: {COLORS['text_primary']} !important;
        font-weight: 600;
    }}

    .stTabs [aria-selected="true"] {{
        background: {COLORS['dark_blue']} !important;
        border: 2px solid {COLORS['accent_gold']} !important;
        color: {COLORS['accent_gold']} !important;
    }}

    footer {{visibility:hidden;}}
    </style>
    """, unsafe_allow_html=True)

# ==========================================================
# METRIC CARD WITH TRAFFIC LIGHT
# ==========================================================

def metric_card(label, value, status=None):
    color = COLORS['accent_gold']

    if status == "good":
        color = COLORS['success']
    elif status == "moderate":
        color = COLORS['warning']
    elif status == "bad":
        color = COLORS['danger']

    st.markdown(f"""
    <div style="
        background:{COLORS['card_bg']};
        padding:25px;
        border-radius:12px;
        border:1px solid rgba(255,215,0,0.3);
        text-align:center;
    ">
        <div style="color:{COLORS['text_secondary']}; font-size:0.9rem;">
            {label}
        </div>
        <div style="color:{color}; font-size:2rem; font-weight:700;">
            {value}
        </div>
    </div>
    """, unsafe_allow_html=True)

# ==========================================================
# MAIN
# ==========================================================

def main():
    st.set_page_config(page_title="Working Capital AI Agent", layout="wide")
    apply_styles()

    # HEADER
    st.markdown(f"""
    <div class="header-container">
        <h1>{BRANDING['icon']} Working Capital AI Agent</h1>
        <p>{BRANDING['name']}</p>
        <p>{BRANDING['instructor']} | {BRANDING['credentials']}</p>
    </div>
    """, unsafe_allow_html=True)

    # SIDEBAR INPUTS
    st.sidebar.header("Financial Inputs")

    revenue = st.sidebar.number_input("Annual Revenue", 20000000)
    cogs = st.sidebar.number_input("Annual COGS", 14000000)
    receivables = st.sidebar.number_input("Accounts Receivable", 5000000)
    inventory = st.sidebar.number_input("Inventory", 3000000)
    payables = st.sidebar.number_input("Accounts Payable", 3500000)

    # CALCULATIONS
    dso = (receivables / revenue) * 365 if revenue else 0
    dio = (inventory / cogs) * 365 if cogs else 0
    dpo = (payables / cogs) * 365 if cogs else 0
    ccc = dso + dio - dpo

    working_capital = receivables + inventory - payables

    tab1, tab2, tab3 = st.tabs([
        "📊 Balance Sheet",
        "📈 Liquidity Metrics",
        "🔄 Cash Conversion Cycle"
    ])

    # ================= BALANCE SHEET =================
    with tab1:
        col1, col2 = st.columns(2)

        with col1:
            st.dataframe(pd.DataFrame({
                "Current Assets": ["Receivables", "Inventory"],
                "Amount": [receivables, inventory]
            }), use_container_width=True, hide_index=True)

        with col2:
            st.dataframe(pd.DataFrame({
                "Current Liabilities": ["Payables"],
                "Amount": [payables]
            }), use_container_width=True, hide_index=True)

    # ================= LIQUIDITY =================
    with tab2:
        col1, col2 = st.columns(2)

        wc_status = "good" if working_capital > 0 else "bad"

        with col1:
            metric_card("Working Capital", f"{working_capital:,.0f}", wc_status)

        with col2:
            metric_card("CCC (Days)", f"{ccc:.1f}",
                        "good" if ccc < 0 else "moderate" if ccc < 60 else "bad")

    # ================= CCC ADVANCED =================
    with tab3:

        # Traffic Cards
        col1, col2, col3 = st.columns(3)

        with col1:
            metric_card("DSO", f"{dso:.1f}",
                        "good" if dso < 60 else "moderate" if dso < 90 else "bad")
        with col2:
            metric_card("DIO", f"{dio:.1f}",
                        "good" if dio < 60 else "moderate" if dio < 90 else "bad")
        with col3:
            metric_card("DPO", f"{dpo:.1f}", "good" if dpo > 60 else "moderate")

        st.markdown("### CCC Waterfall")
        waterfall = pd.DataFrame({
            "Component": ["DSO", "DIO", "-DPO"],
            "Days": [dso, dio, -dpo]
        }).set_index("Component")

        st.bar_chart(waterfall)

        st.markdown("### Working Capital Release Simulation")
        reduce_days = st.slider("Reduce CCC by (days)", 0, 60, 10)
        release = (reduce_days / 365) * revenue
        st.success(f"Estimated Cash Release: ₹ {release:,.0f}")

        st.markdown("### AI Recommendations")
        if ccc > 60:
            st.warning("High CCC — tighten receivables & inventory cycle.")
        elif ccc < 0:
            st.success("Excellent working capital efficiency.")
        else:
            st.info("Moderate cycle — incremental optimization possible.")

if __name__ == "__main__":
    main()
