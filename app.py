
"""
Working Capital AI Engine - Mountain Path Edition
CFO Decision System

Includes:
- Traffic Light Risk Coding
- CCC Waterfall
- Working Capital Release Simulation
- Scenario Analysis
- AI Advisory Engine

ZERO external chart libraries
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
# STYLING
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
    section[data-testid="stSidebar"] input {{
        background-color:white !important;
        color:black !important;
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
    st.set_page_config(page_title="WC AI Engine", layout="wide")
    apply_styles()

    st.markdown(f"""
    <h1 style="color:{COLORS['accent_gold']}">
    {BRANDING['icon']} Working Capital AI Engine
    </h1>
    """, unsafe_allow_html=True)

    # ================= INPUTS =================
    st.sidebar.header("Financial Inputs")

    revenue = st.sidebar.number_input("Annual Revenue", 20000000)
    cogs = st.sidebar.number_input("Annual COGS", 14000000)
    receivables = st.sidebar.number_input("Accounts Receivable", 5000000)
    inventory = st.sidebar.number_input("Inventory", 3000000)
    payables = st.sidebar.number_input("Accounts Payable", 3500000)

    # ================= CALCULATIONS =================
    dso = (receivables / revenue) * 365 if revenue else 0
    dio = (inventory / cogs) * 365 if cogs else 0
    dpo = (payables / cogs) * 365 if cogs else 0
    ccc = dso + dio - dpo

    working_capital = receivables + inventory - payables

    # ================= TABS =================
    tab1, tab2, tab3, tab4 = st.tabs([
        "📊 Traffic Dashboard",
        "🔄 CCC Waterfall",
        "💰 WC Release Simulation",
        "🤖 AI Advisory"
    ])

    # ==========================================================
    # 1️⃣ TRAFFIC LIGHT DASHBOARD
    # ==========================================================
    with tab1:
        col1, col2, col3, col4 = st.columns(4)

        dso_status = "good" if dso < 60 else "moderate" if dso < 90 else "bad"
        dio_status = "good" if dio < 60 else "moderate" if dio < 90 else "bad"
        dpo_status = "good" if dpo > 60 else "moderate"
        ccc_status = "good" if ccc < 0 else "moderate" if ccc < 60 else "bad"

        with col1:
            metric_card("DSO (Days)", f"{dso:.1f}", dso_status)
        with col2:
            metric_card("DIO (Days)", f"{dio:.1f}", dio_status)
        with col3:
            metric_card("DPO (Days)", f"{dpo:.1f}", dpo_status)
        with col4:
            metric_card("CCC (Days)", f"{ccc:.1f}", ccc_status)

    # ==========================================================
    # 2️⃣ CCC WATERFALL
    # ==========================================================
    with tab2:
        st.subheader("CCC Decomposition")

        waterfall_df = pd.DataFrame({
            "Component": ["DSO", "DIO", "-DPO"],
            "Days": [dso, dio, -dpo]
        }).set_index("Component")

        st.bar_chart(waterfall_df)

    # ==========================================================
    # 3️⃣ WORKING CAPITAL RELEASE SIMULATION
    # ==========================================================
    with tab3:
        st.subheader("Cash Release from CCC Improvement")

        target_dso = st.slider("Reduce DSO by (days)", 0, 60, 10)
        target_dio = st.slider("Reduce DIO by (days)", 0, 60, 10)

        cash_release_dso = (target_dso / 365) * revenue
        cash_release_dio = (target_dio / 365) * cogs

        total_release = cash_release_dso + cash_release_dio

        st.markdown(f"""
        **Estimated Cash Release:**  
        ₹ {total_release:,.0f}
        """)

    # ==========================================================
    # 4️⃣ AI RECOMMENDATION ENGINE
    # ==========================================================
    with tab4:
        st.subheader("AI Working Capital Recommendations")

        recommendations = []

        if dso > 90:
            recommendations.append("Implement stricter credit policy.")
        if dio > 90:
            recommendations.append("Optimize inventory procurement cycles.")
        if dpo < 45:
            recommendations.append("Negotiate better supplier credit terms.")
        if ccc > 60:
            recommendations.append("Launch working capital optimization program.")

        if not recommendations:
            st.success("Working capital structure is efficient.")
        else:
            for r in recommendations:
                st.warning(r)


if __name__ == "__main__":
    main()
