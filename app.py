
"""
Working Capital AI Agent - Mountain Path Edition
With Solid Metric Cards (No st.metric transparency issues)

The Mountain Path - World of Finance
Prof. V. Ravichandran
"""

import streamlit as st
import pandas as pd

# ============================================================================
# BRANDING
# ============================================================================

COLORS = {
    'dark_blue': '#003366',
    'medium_blue': '#004d80',
    'accent_gold': '#FFD700',
    'bg_dark': '#0a1628',
    'card_bg': '#112240',
    'text_primary': '#e6f1ff',
    'text_secondary': '#8892b0',
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

# ============================================================================
# STYLING
# ============================================================================

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
        background-color: white !important;
        color: black !important;
    }}

    /* ===== FIX MAIN TEXT VISIBILITY (SAFE TARGETING) ===== */

    h1, h2, h3 {{
        color: {COLORS['accent_gold']} !important;
    }}

    label {{
        color: {COLORS['text_primary']} !important;
        font-weight: 600 !important;
    }}

    p {{
        color: {COLORS['text_primary']} !important;
    }}

    /* Improve DataFrame readability */
    div[data-testid="stDataFrame"] {{
        background-color: white !important;
        border-radius: 10px !important;
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

    footer {{visibility: hidden;}}

    </style>
    """, unsafe_allow_html=True)


# ============================================================================
# METRIC CARD FUNCTION
# ============================================================================

def metric_card(label, value):
    st.markdown(f"""
    <div style="
        background:{COLORS['card_bg']};
        padding:25px;
        border-radius:12px;
        border:1px solid rgba(255,215,0,0.3);
        text-align:center;
    ">
        <div style="
            color:{COLORS['text_secondary']};
            font-size:0.9rem;
            margin-bottom:10px;
        ">
            {label}
        </div>
        <div style="
            color:{COLORS['accent_gold']};
            font-size:2rem;
            font-weight:700;
        ">
            {value}
        </div>
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# MAIN APPLICATION
# ============================================================================

def main():
    st.set_page_config(**PAGE_CONFIG)
    apply_styles()

    # HEADER
    st.markdown(f"""
    <div class="header-container">
        <h1>{BRANDING['icon']} Working Capital AI Agent</h1>
        <p>{BRANDING['name']}</p>
        <p>{BRANDING['instructor']} | {BRANDING['credentials']}</p>
    </div>
    """, unsafe_allow_html=True)

    # ================= SIDEBAR =================

    st.sidebar.markdown("### 🧾 Income Statement Inputs")
    revenue = st.sidebar.number_input("Annual Revenue", 20000000)
    cogs = st.sidebar.number_input("Annual COGS", 14000000)

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

    net_wc = total_ca - total_cl
    current_ratio = total_ca / total_cl if total_cl else 0
    quick_ratio = (cash + receivables) / total_cl if total_cl else 0

    dso = (receivables / revenue) * 365 if revenue else 0
    dio = (inventory / cogs) * 365 if cogs else 0
    dpo = (payables / cogs) * 365 if cogs else 0
    ccc = dso + dio - dpo

    # ================= TABS =================

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📊 Balance Sheet",
        "📈 Liquidity Metrics",
        "🔄 Cash Conversion Cycle",
        "📊 Advanced CFO View",
        "📊 Visual Analytics"
    ])


    # -------- BALANCE SHEET --------
    with tab1:
        col1, col2 = st.columns(2)

        with col1:
            st.dataframe(pd.DataFrame({
                "Current Assets": ["Cash", "Receivables", "Inventory", "Other CA", "Total CA"],
                "Amount": [cash, receivables, inventory, other_ca, total_ca]
            }), use_container_width=True, hide_index=True)

        with col2:
            st.dataframe(pd.DataFrame({
                "Current Liabilities": ["Payables", "Short-Term Debt", "Other CL", "Total CL"],
                "Amount": [payables, short_debt, other_cl, total_cl]
            }), use_container_width=True, hide_index=True)

    # -------- LIQUIDITY --------
    with tab2:
        col1, col2, col3 = st.columns(3)

        col1.metric("Net Working Capital", f"{net_wc:,.0f}")
        col2.metric("Current Ratio", f"{current_ratio:.2f}")
        col3.metric("Quick Ratio", f"{quick_ratio:.2f}")

    # -------- CCC --------
    with tab3:
        col1, col2, col3, col4 = st.columns(4)

        col1.metric("DSO (Days)", f"{dso:.1f}")
        col2.metric("DIO (Days)", f"{dio:.1f}")
        col3.metric("DPO (Days)", f"{dpo:.1f}")
        col4.metric("CCC (Days)", f"{ccc:.1f}")

        st.markdown("<br>", unsafe_allow_html=True)

        if ccc < 0:
            st.success("Negative CCC — strong working capital efficiency.")
        elif ccc < 60:
            st.info("Moderate CCC — manageable cycle.")
        else:
            st.warning("High CCC — working capital tied up for long duration.")

    # -------- ADVANCED CFO VIEW --------
    with tab4:

        st.markdown("### 📈 3-Year Working Capital Forecast")

        growth_rate = st.slider("Revenue Growth (%)", 0, 30, 10) / 100

        forecast_data = []
        rev = revenue

        for year in range(1, 4):
            rev = rev * (1 + growth_rate)
            rec = (dso / 365) * rev
            inv = (dio / 365) * cogs * (1 + growth_rate) ** year
            pay = (dpo / 365) * cogs * (1 + growth_rate) ** year
            wc = rec + inv - pay

            forecast_data.append({
                "Year": f"Year {year}",
                "Revenue": round(rev),
                "Working Capital Required": round(wc)
            })

        st.dataframe(pd.DataFrame(forecast_data), use_container_width=True, hide_index=True)

        st.markdown("---")
        st.markdown("### 🏦 DSCR & Covenant Check")

        debt = st.number_input("Total Debt", 5000000)
        interest_rate = st.number_input("Interest Rate (%)", 10) / 100
        principal_payment = st.number_input("Annual Principal Payment", 1000000)
        ebitda_margin = st.number_input("EBITDA Margin (%)", 25) / 100

        ebitda = revenue * ebitda_margin
        interest = debt * interest_rate
        debt_service = interest + principal_payment
        dscr = ebitda / debt_service if debt_service else 0

        col1, col2 = st.columns(2)
        col1.metric("EBITDA", f"{ebitda:,.0f}")
        col2.metric("DSCR", f"{dscr:.2f}")

        if dscr < 1.25:
            st.warning("⚠️ DSCR Covenant Risk")
        else:
            st.success("DSCR Covenant Comfortable")
                # -------- VISUAL ANALYTICS --------
    with tab5:

        st.markdown("### 📈 CCC Decomposition")

        ccc_df = pd.DataFrame({
            "Component": ["DSO", "DIO", "-DPO"],
            "Days": [dso, dio, -dpo]
        })

        st.bar_chart(ccc_df.set_index("Component"))

        st.markdown("---")

        st.markdown("### 💰 Working Capital Composition")

        wc_comp = pd.DataFrame({
            "Component": ["Receivables", "Inventory", "Payables"],
            "Amount": [receivables, inventory, -payables]
        })

        st.bar_chart(wc_comp.set_index("Component"))

        st.markdown("---")

        st.markdown("### 📊 3-Year Working Capital Trend")

        growth = 0.10  # Default 10% for visual projection
        rev_temp = revenue

        trend_data = []

        for year in range(1, 4):
            rev_temp *= (1 + growth)

            rec = (dso / 365) * rev_temp
            inv = (dio / 365) * cogs * (1 + growth) ** year
            pay = (dpo / 365) * cogs * (1 + growth) ** year

            wc = rec + inv - pay

            trend_data.append({
                "Year": f"Year {year}",
                "Working Capital": wc
            })

        trend_df = pd.DataFrame(trend_data)
        st.line_chart(trend_df.set_index("Year"))


    st.divider()
    st.markdown(f"""
    <div style="text-align:center; color:{COLORS['accent_gold']}; font-weight:bold;">
        {BRANDING['icon']} {BRANDING['name']}
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
