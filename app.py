
"""
Working Capital AI Agent - Mountain Path Edition
Enhanced Version (Contrast Fixed + CCC Enhancements)
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
        background-color: white !important;
        color: black !important;
    }}

    /* ===== MAIN CONTENT CONTRAST FIX ===== */

    .main * {{
        color: {COLORS['text_primary']} !important;
    }}

    h1, h2, h3, h4, h5, h6 {{
        color: {COLORS['accent_gold']} !important;
    }}

    div[data-testid="stMarkdownContainer"] p {{
        color: {COLORS['text_primary']} !important;
    }}

    div[data-testid="stSlider"] label {{
        color: {COLORS['text_primary']} !important;
    }}

    div[data-testid="stAlert"] * {{
        color: white !important;
        font-weight: 500;
    }}

    /* Header */

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

    /* Tabs */

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

# ==========================================================
# METRIC CARD
# ==========================================================

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

# ==========================================================
# MAIN
# ==========================================================

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

    # SIDEBAR INPUTS
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

    # CALCULATIONS
    total_ca = cash + receivables + inventory + other_ca
    total_cl = payables + short_debt + other_cl

    net_wc = total_ca - total_cl
    current_ratio = total_ca / total_cl if total_cl else 0
    quick_ratio = (cash + receivables) / total_cl if total_cl else 0

    dso = (receivables / revenue) * 365 if revenue else 0
    dio = (inventory / cogs) * 365 if cogs else 0
    dpo = (payables / cogs) * 365 if cogs else 0
    ccc = dso + dio - dpo

    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs([
        "📊 Balance Sheet",
        "📈 Liquidity Metrics",
        "🔄 Cash Conversion Cycle",
        "📈 3-Year Forecast",
        "🏦 Covenant & Stress Test",
        "📊 Multi-Year Trend",
        "🏦 DSCR & EBITDA Covenants",
        "💼 Credit Memo",
        "📈 WC Sensitivity Grid"
    ])



    # BALANCE SHEET
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

    # LIQUIDITY
    with tab2:
        col1, col2, col3 = st.columns(3)

        with col1:
            metric_card("Net Working Capital", f"{net_wc:,.0f}")

        with col2:
            metric_card("Current Ratio", f"{current_ratio:.2f}")

        with col3:
            metric_card("Quick Ratio", f"{quick_ratio:.2f}")

    # CCC
    with tab3:
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            metric_card("DSO (Days)", f"{dso:.1f}")

        with col2:
            metric_card("DIO (Days)", f"{dio:.1f}")

        with col3:
            metric_card("DPO (Days)", f"{dpo:.1f}")

        with col4:
            metric_card("CCC (Days)", f"{ccc:.1f}")

        st.markdown("### 📊 CCC Decomposition")

        waterfall = pd.DataFrame({
            "Component": ["DSO", "DIO", "-DPO"],
            "Days": [dso, dio, -dpo]
        }).set_index("Component")

        st.bar_chart(waterfall)

        st.markdown("### 💰 Working Capital Release Simulation")

        reduce_days = st.slider("Reduce CCC by (Days)", 0, 60, 10)
        cash_release = (reduce_days / 365) * revenue

        st.success(f"Estimated Cash Release: ₹ {cash_release:,.0f}")

        st.markdown("### 🤖 AI Working Capital Suggestions")

        suggestions = []

        if dso > 90:
            suggestions.append("Tighten credit control policies.")
        if dio > 90:
            suggestions.append("Optimize inventory procurement cycle.")
        if dpo < 45:
            suggestions.append("Negotiate extended supplier terms.")
        if ccc > 60:
            suggestions.append("Launch structured working capital optimization program.")

        if suggestions:
            for s in suggestions:
                st.warning(s)
        else:
            st.success("Working capital structure appears efficient.")

    # ==========================================================
    # 3-YEAR WORKING CAPITAL FORECAST
    # ==========================================================
    with tab4:

        st.markdown("### 📈 3-Year Working Capital Forecast")

        growth_rate = st.slider("Annual Revenue Growth (%)", 0, 30, 10) / 100

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
                "Working Capital Required": round(wc),
                "Projected CCC": round(dso + dio - dpo, 1)
            })

        forecast_df = pd.DataFrame(forecast_data)

        st.dataframe(forecast_df, use_container_width=True, hide_index=True)

        incremental_wc = forecast_df["Working Capital Required"].iloc[-1] - net_wc

        st.info(f"Additional Working Capital Needed in 3 Years: ₹ {incremental_wc:,.0f}")
    # ==========================================================
    # BANK COVENANT & STRESS TEST
    # ==========================================================
    with tab5:

        st.markdown("### 🏦 Bank Covenant & Liquidity Stress Panel")

        min_current_ratio = st.number_input("Minimum Required Current Ratio (Bank)", value=1.25)
        max_ccc_allowed = st.number_input("Maximum CCC Allowed (Days)", value=90)

        stress_revenue_drop = st.slider("Revenue Stress Scenario (%)", 0, 50, 20) / 100

        stressed_revenue = revenue * (1 - stress_revenue_drop)

        stressed_receivables = (dso / 365) * stressed_revenue
        stressed_wc = stressed_receivables + inventory - payables

        stressed_current_ratio = (cash + stressed_receivables + inventory + other_ca) / total_cl if total_cl else 0

        col1, col2 = st.columns(2)

        with col1:
            metric_card("Stressed Current Ratio", f"{stressed_current_ratio:.2f}")

        with col2:
            metric_card("Stressed Working Capital", f"{stressed_wc:,.0f}")

        st.markdown("### Covenant Status")

        if stressed_current_ratio < min_current_ratio:
            st.error("⚠️ Current Ratio Covenant Breach Under Stress Scenario.")
        else:
            st.success("Current Ratio Covenant Maintained.")

        if ccc > max_ccc_allowed:
            st.error("⚠️ CCC Covenant Breach.")
        else:
            st.success("CCC Within Acceptable Bank Limits.")

    # ==========================================================
    # MULTI-YEAR TREND VIEW
    # ==========================================================
    with tab6:

        st.markdown("### 📊 Historical + Forecast Trend")

        history_years = 3
        growth = 0.08

        trend_data = []

        rev_hist = revenue

        # Simulated historical backward
        for i in range(history_years, 0, -1):
            rev_hist = rev_hist / (1 + growth)
            trend_data.append({
                "Year": f"Hist -{i}",
                "Revenue": round(rev_hist),
                "Working Capital": round((dso/365)*rev_hist + (dio/365)*cogs - (dpo/365)*cogs)
            })

        # Current
        trend_data.append({
            "Year": "Current",
            "Revenue": revenue,
            "Working Capital": net_wc
        })

        # Forecast forward
        rev_fwd = revenue
        for i in range(1, 4):
            rev_fwd *= (1 + growth)
            trend_data.append({
                "Year": f"Fwd +{i}",
                "Revenue": round(rev_fwd),
                "Working Capital": round((dso/365)*rev_fwd + (dio/365)*cogs - (dpo/365)*cogs)
            })

        trend_df = pd.DataFrame(trend_data).set_index("Year")

        st.line_chart(trend_df)

        # ==========================================================
    # DSCR & EBITDA COVENANT TEST
    # ==========================================================
    with tab7:

        st.markdown("### 🏦 Debt Service Coverage & EBITDA Covenants")

        debt_outstanding = st.number_input("Total Debt", value=5000000)
        interest_rate = st.number_input("Interest Rate (%)", value=10) / 100
        principal_payment = st.number_input("Annual Principal Payment", value=1000000)
        ebitda_margin = st.number_input("EBITDA Margin (%)", value=25) / 100

        ebitda = revenue * ebitda_margin
        interest = debt_outstanding * interest_rate
        debt_service = interest + principal_payment

        dscr = ebitda / debt_service if debt_service else 0

        col1, col2 = st.columns(2)

        with col1:
            metric_card("EBITDA", f"{ebitda:,.0f}")

        with col2:
            metric_card("DSCR", f"{dscr:.2f}")

        covenant_dscr_min = 1.25
        covenant_ebitda_min = 3000000

        if dscr < covenant_dscr_min:
            st.error("⚠️ DSCR Covenant Breach")
        else:
            st.success("DSCR Covenant Maintained")

        if ebitda < covenant_ebitda_min:
            st.error("⚠️ EBITDA Covenant Breach")
        else:
            st.success("EBITDA Covenant Maintained")

        # ==========================================================
    # CREDIT MEMO GENERATOR
    # ==========================================================
    with tab8:

        st.markdown("### 💼 Automated Credit Memo Summary")

        memo = f"""
Company Revenue: ₹ {revenue:,.0f}

Net Working Capital: ₹ {net_wc:,.0f}
Current Ratio: {current_ratio:.2f}
Cash Conversion Cycle: {ccc:.1f} days

EBITDA: ₹ {ebitda:,.0f}
DSCR: {dscr:.2f}

Assessment:
"""

        if current_ratio < 1.25:
            memo += "\n- Liquidity risk elevated."
        else:
            memo += "\n- Liquidity position acceptable."

        if dscr < 1.25:
            memo += "\n- Debt servicing risk observed."
        else:
            memo += "\n- Debt servicing adequate."

        if ccc > 60:
            memo += "\n- Working capital cycle extended."
        else:
            memo += "\n- Working capital cycle efficient."

        st.text_area("Credit Committee Note", memo, height=300)

        # ==========================================================
    # REVENUE-LINKED WC SENSITIVITY GRID
    # ==========================================================
    with tab9:

        st.markdown("### 📈 Revenue vs Working Capital Sensitivity")

        growth_range = [0, 5, 10, 15, 20]
        sensitivity = []

        for g in growth_range:
            rev_s = revenue * (1 + g/100)
            wc_s = (dso/365)*rev_s + (dio/365)*cogs - (dpo/365)*cogs

            sensitivity.append({
                "Revenue Growth %": g,
                "Projected Revenue": round(rev_s),
                "Working Capital Required": round(wc_s)
            })

        sens_df = pd.DataFrame(sensitivity)

        st.dataframe(sens_df, use_container_width=True, hide_index=True)


    
    st.divider()
    st.markdown(f"""
    <div style="text-align:center; color:{COLORS['accent_gold']}; font-weight:bold;">
        {BRANDING['icon']} {BRANDING['name']}
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
