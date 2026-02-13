
"""
Working Capital AI Agent - Mountain Path Edition
The Mountain Path - World of Finance
Prof. V. Ravichandran

AI Agent for:
- Receivables Risk Detection
- Cash Flow Forecast
- Inventory Reorder Optimization

ZERO external chart libraries - uses only Streamlit native components
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
            border-right: 1px solid rgba(255,215,0,0.2);
        }}

        /* FORCE ALL SIDEBAR TEXT TO BE LIGHT */
        section[data-testid="stSidebar"] label,
        section[data-testid="stSidebar"] .stMarkdown,
        section[data-testid="stSidebar"] p,
        section[data-testid="stSidebar"] span,
        section[data-testid="stSidebar"] div,
        section[data-testid="stSidebar"] [data-testid="stWidgetLabel"] p,
        section[data-testid="stSidebar"] [data-testid="stWidgetLabel"] label {{
            color: {COLORS['text_primary']} !important;
        }}

        /* Slider current value */
        section[data-testid="stSidebar"] [data-testid="stThumbValue"] {{
            color: {COLORS['accent_gold']} !important;
            font-weight: bold;
        }}

        /* Input fields */
        section[data-testid="stSidebar"] input {{
            background-color: #ffffff !important;
            color: #000000 !important;
        }}

        /* Selectbox text */
        section[data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] span {{
            color: {COLORS['text_primary']} !important;
        }}

        .header-container {{
            background: linear-gradient(135deg, {COLORS['dark_blue']}, {COLORS['medium_blue']});
            border: 2px solid {COLORS['accent_gold']};
            border-radius: 12px;
            padding: 1.5rem 2rem;
            margin-bottom: 1.5rem;
            text-align: center;
        }}

        .header-container h1 {{
            color: {COLORS['accent_gold']};
            margin: 0;
        }}

        .header-container p {{
            color: {COLORS['text_primary']};
            margin: 0.3rem 0 0;
            font-size: 0.9rem;
        }}

        .metric-card {{
            background: {COLORS['card_bg']};
            border: 1px solid rgba(255,215,0,0.3);
            border-radius: 10px;
            padding: 1.2rem;
            text-align: center;
        }}

        .metric-card .label {{
            color: {COLORS['text_secondary']};
            font-size: 0.8rem;
            text-transform: uppercase;
        }}

        .metric-card .value {{
            color: {COLORS['accent_gold']};
            font-size: 1.6rem;
            font-weight: 700;
        }}

        .section-title {{
            color: {COLORS['accent_gold']};
            font-size: 1.3rem;
            border-bottom: 2px solid rgba(255,215,0,0.3);
            padding-bottom: 0.5rem;
            margin: 1.5rem 0 1rem;
        }}

        footer {{visibility: hidden;}}
    </style>
    """, unsafe_allow_html=True)


# ============================================================================
# WORKING CAPITAL AI ENGINE
# ============================================================================

class WorkingCapitalAgent:

    def __init__(self, params):
        self.p = params
        self.receivables = None
        self.cash_history = None

    def generate_data(self):
        np.random.seed(42)

        self.receivables = pd.DataFrame({
            "customer_id": np.arange(1, 201),
            "invoice_amount": np.random.randint(10000, 200000, 200),
            "days_outstanding": np.random.randint(5, 90, 200),
            "past_delay_flag": np.random.randint(0, 2, 200)
        })

        self.receivables["delayed"] = (
            0.02 * self.receivables["days_outstanding"]
            + 0.5 * self.receivables["past_delay_flag"]
            + np.random.normal(0, 0.5, 200)
        ) > 1.5

        self.receivables["delayed"] = self.receivables["delayed"].astype(int)

        self.cash_history = pd.DataFrame({
            "day_index": np.arange(180),
            "net_cash_flow": np.random.normal(
                self.p["avg_cash_flow"],
                self.p["cash_volatility"],
                180
            )
        })

        self.cash_history["cumulative_cash"] = \
            self.cash_history["net_cash_flow"].cumsum()

    def receivables_risk(self):
        X = self.receivables[[
            "invoice_amount",
            "days_outstanding",
            "past_delay_flag"
        ]]
        y = self.receivables["delayed"]

        model = LogisticRegression()
        model.fit(X, y)

        self.receivables["delay_probability"] = \
            model.predict_proba(X)[:, 1]

        high_risk = self.receivables[
            (self.receivables["delay_probability"] > 0.7) &
            (self.receivables["days_outstanding"] > 45)
        ]

        return high_risk

    def cash_forecast(self):
        X = self.cash_history[["day_index"]]
        y = self.cash_history["cumulative_cash"]

        model = LinearRegression()
        model.fit(X, y)

        future_index = np.arange(180, 180 + self.p["forecast_days"])
        forecast = model.predict(
            pd.DataFrame({"day_index": future_index})
        )

        return forecast

    def inventory_analysis(self):
        reorder_point = (
            self.p["avg_daily_demand"]
            * self.p["lead_time_days"]
        )

        stockout = self.p["current_stock"] < reorder_point

        return reorder_point, stockout


# ============================================================================
# MAIN APPLICATION
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

    # SIDEBAR INPUTS
    st.sidebar.markdown("### 📊 Working Capital Assumptions")

    current_stock = st.sidebar.number_input("Current Inventory", 1200)
    avg_daily_demand = st.sidebar.number_input("Avg Daily Demand", 50)
    lead_time_days = st.sidebar.number_input("Lead Time (Days)", 10)

    avg_cash_flow = st.sidebar.number_input("Avg Daily Cash Flow", 50000)
    cash_volatility = st.sidebar.number_input("Cash Flow Volatility", 20000)
    forecast_days = st.sidebar.selectbox("Forecast Horizon", [30, 60, 90], index=2)

    params = {
        "current_stock": current_stock,
        "avg_daily_demand": avg_daily_demand,
        "lead_time_days": lead_time_days,
        "avg_cash_flow": avg_cash_flow,
        "cash_volatility": cash_volatility,
        "forecast_days": forecast_days
    }

    agent = WorkingCapitalAgent(params)
    agent.generate_data()

    high_risk = agent.receivables_risk()
    forecast = agent.cash_forecast()
    reorder_point, stockout = agent.inventory_analysis()

    tab1, tab2, tab3, tab4 = st.tabs([
        "📋 WC Summary",
        "💰 Receivables Risk",
        "📈 Cash Forecast",
        "📦 Inventory"
    ])

    with tab1:
        st.markdown('<div class="section-title">📊 Key Metrics</div>', unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown(f'<div class="metric-card"><div class="label">High Risk Customers</div><div class="value">{len(high_risk)}</div></div>', unsafe_allow_html=True)

        with col2:
            st.markdown(f'<div class="metric-card"><div class="label">Reorder Point</div><div class="value">{reorder_point}</div></div>', unsafe_allow_html=True)

        with col3:
            status = "⚠️ STOCKOUT RISK" if stockout else "✅ HEALTHY"
            st.markdown(f'<div class="metric-card"><div class="label">Inventory Status</div><div class="value">{status}</div></div>', unsafe_allow_html=True)

    with tab2:
        st.markdown('<div class="section-title">⚠️ High Risk Receivables</div>', unsafe_allow_html=True)
        st.dataframe(high_risk, use_container_width=True)

    with tab3:
        st.markdown('<div class="section-title">📈 Cash Position Forecast</div>', unsafe_allow_html=True)
        forecast_df = pd.DataFrame({
            "Forecast Day": np.arange(1, forecast_days + 1),
            "Projected Cash": forecast
        }).set_index("Forecast Day")
        st.line_chart(forecast_df)

    with tab4:
        st.markdown('<div class="section-title">📦 Inventory Analysis</div>', unsafe_allow_html=True)
        st.write(f"Reorder Point: {reorder_point}")
        if stockout:
            st.error("Inventory below reorder level. Place order immediately.")
        else:
            st.success("Inventory within safe limits.")

    st.divider()
    st.markdown(f"""
    <div style="text-align:center; padding:1rem;">
        <p style="color:{COLORS['accent_gold']}; font-weight:700;">
            {BRANDING['icon']} {BRANDING['name']}</p>
        <p style="color:{COLORS['text_secondary']}; font-size:0.8rem;">
            {BRANDING['instructor']} | {BRANDING['credentials']}</p>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
