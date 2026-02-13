
"""
Working Capital CFO Dashboard
Mountain Path Edition
"""

import streamlit as st
import pandas as pd

# ==========================================================
# STYLING
# ==========================================================

def apply_styles():
    st.markdown("""
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

    .main * {
        color: #e6f1ff !important;
    }

    h1, h2, h3 {
        color: #FFD700 !important;
    }

    footer {visibility:hidden;}
    </style>
    """, unsafe_allow_html=True)

# ==========================================================
# METRIC CARD
# ==========================================================

def metric_card(label, value, color="#FFD700"):
    st.markdown(f"""
    <div style="
        background:#112240;
        padding:22px;
        border-radius:12px;
        border:1px solid rgba(255,215,0,0.3);
        text-align:center;
    ">
        <div style="color:#8892b0;font-size:0.85rem;margin-bottom:8px;">
            {label}
        </div>
        <div style="color:{color};font-size:1.8rem;font-weight:700;">
            {value}
        </div>
    </div>
    """, unsafe_allow_html=True)

# ==========================================================
# MAIN
# ==========================================================

def main():

    st.set_page_config(layout="wide")
    apply_styles()

    st.markdown("<h1>🏔️ CFO Liquidity Dashboard</h1>", unsafe_allow_html=True)

    # ================= INPUTS =================
    st.sidebar.header("Financial Inputs")

    revenue = st.sidebar.number_input("Annual Revenue", 20000000)
    cogs = st.sidebar.number_input("Annual COGS", 14000000)

    cash = st.sidebar.number_input("Cash", 2000000)
    receivables = st.sidebar.number_input("Accounts Receivable", 5000000)
    inventory = st.sidebar.number_input("Inventory", 3000000)
    payables = st.sidebar.number_input("Accounts Payable", 3500000)

    debt = st.sidebar.number_input("Total Debt", 5000000)
    interest_rate = st.sidebar.number_input("Interest Rate (%)", 10)/100
    principal = st.sidebar.number_input("Annual Principal Payment", 1000000)
    ebitda_margin = st.sidebar.number_input("EBITDA Margin (%)", 25)/100

    # ================= CALCULATIONS =================
    total_ca = cash + receivables + inventory
    total_cl = payables

    net_wc = total_ca - total_cl
    current_ratio = total_ca / total_cl if total_cl else 0
    quick_ratio = (cash + receivables) / total_cl if total_cl else 0

    dso = (receivables / revenue) * 365 if revenue else 0
    dio = (inventory / cogs) * 365 if cogs else 0
    dpo = (payables / cogs) * 365 if cogs else 0
    ccc = dso + dio - dpo

    ebitda = revenue * ebitda_margin
    interest = debt * interest_rate
    debt_service = interest + principal
    dscr = ebitda / debt_service if debt_service else 0

    # ==========================================================
    # TABS
    # ==========================================================

    tab1, tab2, tab3 = st.tabs([
        "🏔 Executive Snapshot",
        "📈 Forward Outlook",
        "🏦 Capital & Covenants"
    ])

    # ==========================================================
    # TAB 1 — EXECUTIVE SNAPSHOT
    # ==========================================================

    with tab1:

        col1,col2,col3,col4 = st.columns(4)

        col1.metric("Net Working Capital", f"{net_wc:,.0f}")
        col2.metric("Current Ratio", f"{current_ratio:.2f}")
        col3.metric("Quick Ratio", f"{quick_ratio:.2f}")
        col4.metric("CCC (Days)", f"{ccc:.1f}")

        st.divider()

        col1,col2,col3 = st.columns(3)

        col1.metric("DSO", f"{dso:.1f}")
        col2.metric("DIO", f"{dio:.1f}")
        col3.metric("DPO", f"{dpo:.1f}")

        st.divider()

        if current_ratio < 1.2:
            st.error("⚠️ Liquidity Risk Elevated")
        elif ccc > 60:
            st.warning("⚠️ Working Capital Cycle Extended")
        else:
            st.success("Liquidity Position Stable")

    # ==========================================================
    # TAB 2 — FORWARD OUTLOOK
    # ==========================================================

    with tab2:

        growth = st.slider("Revenue Growth (%)", 0, 25, 10)/100

        rev_forecast = revenue * (1 + growth)
        wc_forecast = (dso/365)*rev_forecast + (dio/365)*cogs - (dpo/365)*cogs

        metric_card("Projected Revenue", f"{rev_forecast:,.0f}")
        metric_card("Projected WC Requirement", f"{wc_forecast:,.0f}")

        st.divider()

        reduce_days = st.slider("Improve CCC by (Days)", 0, 60, 10)
        cash_release = (reduce_days/365)*revenue

        st.info(f"Potential Cash Release: {cash_release:,.0f}")

    # ==========================================================
    # TAB 3 — CAPITAL & COVENANTS
    # ==========================================================

    with tab3:

        col1,col2 = st.columns(2)

        with col1:
            metric_card("EBITDA", f"{ebitda:,.0f}")

        with col2:
            metric_card("DSCR", f"{dscr:.2f}")

        st.divider()

        if dscr < 1.25:
            st.error("⚠️ DSCR Covenant Breach")
        else:
            st.success("DSCR Covenant Maintained")

if __name__ == "__main__":
    main()
