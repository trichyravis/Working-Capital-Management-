

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

    tab1, tab2, tab3 = st.tabs([
        "📊 Balance Sheet",
        "📈 Liquidity Metrics",
        "🔄 Cash Conversion Cycle"
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

        with col1:
            metric_card("Net Working Capital", f"{net_wc:,.0f}")

        with col2:
            metric_card("Current Ratio", f"{current_ratio:.2f}")

        with col3:
            metric_card("Quick Ratio", f"{quick_ratio:.2f}")

    # -------- CCC --------
        # -------- CCC --------
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

        st.markdown("<br>", unsafe_allow_html=True)

        # ===== CCC INTERPRETATION (unchanged logic) =====
        if ccc < 0:
            st.success("Negative CCC — strong working capital efficiency.")
        elif ccc < 60:
            st.info("Moderate CCC — manageable cycle.")
        else:
            st.warning("High CCC — working capital tied up for long duration.")

        # ==========================================================
        # NEW: CCC WATERFALL (non-intrusive)
        # ==========================================================
        st.markdown("### 📊 CCC Decomposition")
        
        # Create waterfall dataframe
        waterfall = pd.DataFrame({
            "Component": ["DSO", "DIO", "-DPO"],
            "Days": [dso, dio, -dpo]
        }).set_index("Component")
        
        # Wrap chart in light container for visibility
        st.markdown("""
        <div style="
            background:white;
            padding:20px;
            border-radius:12px;
        ">
        """, unsafe_allow_html=True)
        
        st.bar_chart(waterfall)
        
        st.markdown("</div>", unsafe_allow_html=True)


        # ==========================================================
        # NEW: Working Capital Release Simulation
        # ==========================================================
        st.markdown("### 💰 Working Capital Release Simulation")

        reduce_days = st.slider("Reduce CCC by (Days)", 0, 60, 10)

        cash_release = (reduce_days / 365) * revenue

        st.success(f"Estimated Cash Release: ₹ {cash_release:,.0f}")

        # ==========================================================
        # NEW: AI Recommendation Engine (Light-touch addition)
        # ==========================================================
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



if __name__ == "__main__":
    main()
