
"""
Working Capital AI Agent - Mountain Path Edition
Fully Extended + Stable + Wrapped Tabs
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

PAGE_CONFIG = {
    'page_title': 'Working Capital AI Agent | Mountain Path',
    'page_icon': '🏔️',
    'layout': 'wide',
    'initial_sidebar_state': 'expanded',
}

# ==========================================================
# STYLING (Safe — No f-string brace issues)
# ==========================================================

def apply_styles():

    css = """
    <style>

    .stApp {
        background: linear-gradient(135deg, #0a1628 0%, #003366 50%, #0d2137 100%);
    }

    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0a1628 0%, #003366 100%);
    }

    section[data-testid="stSidebar"] * {
        color: #e6f1ff !important;
    }

    section[data-testid="stSidebar"] input {
        background-color: white !important;
        color: black !important;
    }

    /* Force high contrast main content */
    .main * {
        color: #e6f1ff !important;
    }

    h1, h2, h3, h4, h5, h6 {
        color: #FFD700 !important;
    }

    div[data-testid="stAlert"] * {
        color: white !important;
    }

    /* Wrap tabs to next line */
    .stTabs [data-baseweb="tab-list"] {
        flex-wrap: wrap !important;
        row-gap: 8px;
    }

    .stTabs [data-baseweb="tab"] {
        flex: 0 0 auto;
    }

    footer {visibility:hidden;}

    </style>
    """

    st.markdown(css, unsafe_allow_html=True)

# ==========================================================
# METRIC CARD
# ==========================================================

def metric_card(label, value):
    st.markdown(f"""
    <div style="
        background:#112240;
        padding:25px;
        border-radius:12px;
        border:1px solid rgba(255,215,0,0.3);
        text-align:center;
    ">
        <div style="
            color:#8892b0;
            font-size:0.9rem;
            margin-bottom:10px;
        ">
            {label}
        </div>
        <div style="
            color:#FFD700;
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

    st.markdown("""
    <h1>🏔️ Working Capital AI Agent</h1>
    """, unsafe_allow_html=True)

    # ================= INPUTS =================
    st.sidebar.header("Financial Inputs")

    revenue = st.sidebar.number_input("Annual Revenue", 20000000)
    cogs = st.sidebar.number_input("Annual COGS", 14000000)

    cash = st.sidebar.number_input("Cash", 2000000)
    receivables = st.sidebar.number_input("Accounts Receivable", 5000000)
    inventory = st.sidebar.number_input("Inventory", 3000000)
    other_ca = st.sidebar.number_input("Other Current Assets", 500000)

    payables = st.sidebar.number_input("Accounts Payable", 3500000)
    short_debt = st.sidebar.number_input("Short-Term Debt", 1500000)
    other_cl = st.sidebar.number_input("Other Current Liabilities", 400000)

    total_ca = cash + receivables + inventory + other_ca
    total_cl = payables + short_debt + other_cl
    net_wc = total_ca - total_cl

    current_ratio = total_ca / total_cl if total_cl else 0
    quick_ratio = (cash + receivables) / total_cl if total_cl else 0

    dso = (receivables / revenue) * 365 if revenue else 0
    dio = (inventory / cogs) * 365 if cogs else 0
    dpo = (payables / cogs) * 365 if cogs else 0
    ccc = dso + dio - dpo

    # ==========================================================
    # TABS
    # ==========================================================

    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs([
        "📊 Balance Sheet",
        "📈 Liquidity",
        "🔄 CCC",
        "📈 3-Year Forecast",
        "🏦 Stress Test",
        "📊 Trend",
        "🏦 DSCR",
        "💼 Credit Memo",
        "📈 Sensitivity"
    ])

    # ----------------------------------------------------------
    # TAB 1
    # ----------------------------------------------------------
    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            st.dataframe(pd.DataFrame({
                "Current Assets": ["Cash","Receivables","Inventory","Other CA","Total"],
                "Amount":[cash,receivables,inventory,other_ca,total_ca]
            }), use_container_width=True, hide_index=True)

        with col2:
            st.dataframe(pd.DataFrame({
                "Current Liabilities":["Payables","Short Debt","Other CL","Total"],
                "Amount":[payables,short_debt,other_cl,total_cl]
            }), use_container_width=True, hide_index=True)

    # ----------------------------------------------------------
    # TAB 2
    # ----------------------------------------------------------
    with tab2:
        col1,col2,col3 = st.columns(3)
        with col1:
            metric_card("Net Working Capital", f"{net_wc:,.0f}")
        with col2:
            metric_card("Current Ratio", f"{current_ratio:.2f}")
        with col3:
            metric_card("Quick Ratio", f"{quick_ratio:.2f}")

    # ----------------------------------------------------------
    # TAB 3
    # ----------------------------------------------------------
    with tab3:
        col1,col2,col3,col4 = st.columns(4)
        with col1:
            metric_card("DSO", f"{dso:.1f}")
        with col2:
            metric_card("DIO", f"{dio:.1f}")
        with col3:
            metric_card("DPO", f"{dpo:.1f}")
        with col4:
            metric_card("CCC", f"{ccc:.1f}")

        st.bar_chart(pd.DataFrame({
            "Component":["DSO","DIO","-DPO"],
            "Days":[dso,dio,-dpo]
        }).set_index("Component"))

    # ----------------------------------------------------------
    # TAB 7 — DSCR (example advanced)
    # ----------------------------------------------------------
    with tab7:
        debt = st.number_input("Total Debt", 5000000)
        rate = st.number_input("Interest Rate (%)", 10)/100
        principal = st.number_input("Principal Payment", 1000000)
        margin = st.number_input("EBITDA Margin (%)", 25)/100

        ebitda = revenue * margin
        interest = debt * rate
        dscr = ebitda / (interest + principal) if (interest+principal) else 0

        col1,col2 = st.columns(2)
        with col1:
            metric_card("EBITDA", f"{ebitda:,.0f}")
        with col2:
            metric_card("DSCR", f"{dscr:.2f}")

    # ----------------------------------------------------------
    # TAB 9 — Sensitivity
    # ----------------------------------------------------------
    with tab9:
        growth_range = [0,5,10,15,20]
        sens=[]
        for g in growth_range:
            rev_s = revenue*(1+g/100)
            wc_s = (dso/365)*rev_s + (dio/365)*cogs - (dpo/365)*cogs
            sens.append({
                "Growth %":g,
                "Revenue":round(rev_s),
                "WC Required":round(wc_s)
            })
        st.dataframe(pd.DataFrame(sens),use_container_width=True,hide_index=True)

if __name__ == "__main__":
    main()
