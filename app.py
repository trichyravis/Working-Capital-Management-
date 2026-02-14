"""
Enhanced Working Capital AI Agent - Mountain Path Edition
Advanced Analytics & CFO Decision Support

The Mountain Path - World of Finance
Prof. V. Ravichandran
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta

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
    'success': '#10b981',
    'warning': '#f59e0b',
    'danger': '#ef4444',
}

BRANDING = {
    'name': 'The Mountain Path - World of Finance',
    'instructor': 'Prof. V. Ravichandran',
    'credentials': '28+ Years Corporate Finance & Banking | 10+ Years Academic Excellence',
    'icon': '🏔️',
}

PAGE_CONFIG = {
    'page_title': 'Enhanced Working Capital AI Agent | Mountain Path',
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

    .insight-box {{
        background: {COLORS['card_bg']};
        border-left: 4px solid {COLORS['accent_gold']};
        border-radius: 8px;
        padding: 1.5rem;
        margin: 1rem 0;
    }}

    .insight-box h4 {{
        color: {COLORS['accent_gold']} !important;
        margin-top: 0;
    }}

    .metric-card {{
        background: {COLORS['card_bg']};
        padding: 20px;
        border-radius: 12px;
        border: 1px solid rgba(255,215,0,0.3);
        text-align: center;
        height: 100%;
    }}

    .metric-label {{
        color: {COLORS['text_secondary']};
        font-size: 0.85rem;
        margin-bottom: 8px;
    }}

    .metric-value {{
        color: {COLORS['accent_gold']};
        font-size: 1.8rem;
        font-weight: 700;
    }}

    .metric-delta {{
        font-size: 0.9rem;
        margin-top: 5px;
    }}

    footer {{visibility: hidden;}}

    </style>
    """, unsafe_allow_html=True)


# ============================================================================
# METRIC CARD FUNCTION
# ============================================================================

def metric_card(label, value, delta=None, delta_color=None):
    delta_html = ""
    if delta is not None:
        color = delta_color or (COLORS['success'] if delta > 0 else COLORS['danger'])
        arrow = "▲" if delta > 0 else "▼"
        delta_html = f"""
        <div class="metric-delta" style="color:{color};">
            {arrow} {abs(delta):.1f}%
        </div>
        """
    
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">{label}</div>
        <div class="metric-value">{value}</div>
        {delta_html}
    </div>
    """, unsafe_allow_html=True)


# ============================================================================
# ADVANCED CALCULATIONS
# ============================================================================

def calculate_working_capital_metrics(revenue, cogs, cash, receivables, inventory, 
                                     other_ca, payables, short_debt, other_cl):
    """Calculate comprehensive working capital metrics"""
    
    total_ca = cash + receivables + inventory + other_ca
    total_cl = payables + short_debt + other_cl
    
    net_wc = total_ca - total_cl
    current_ratio = total_ca / total_cl if total_cl else 0
    quick_ratio = (cash + receivables) / total_cl if total_cl else 0
    cash_ratio = cash / total_cl if total_cl else 0
    
    # Operating cycle metrics
    dso = (receivables / revenue) * 365 if revenue else 0
    dio = (inventory / cogs) * 365 if cogs else 0
    dpo = (payables / cogs) * 365 if cogs else 0
    ccc = dso + dio - dpo
    
    # Efficiency ratios
    receivables_turnover = revenue / receivables if receivables else 0
    inventory_turnover = cogs / inventory if inventory else 0
    payables_turnover = cogs / payables if payables else 0
    
    # Working capital ratios
    wc_to_sales = net_wc / revenue if revenue else 0
    wc_to_assets = net_wc / total_ca if total_ca else 0
    
    return {
        'total_ca': total_ca,
        'total_cl': total_cl,
        'net_wc': net_wc,
        'current_ratio': current_ratio,
        'quick_ratio': quick_ratio,
        'cash_ratio': cash_ratio,
        'dso': dso,
        'dio': dio,
        'dpo': dpo,
        'ccc': ccc,
        'receivables_turnover': receivables_turnover,
        'inventory_turnover': inventory_turnover,
        'payables_turnover': payables_turnover,
        'wc_to_sales': wc_to_sales,
        'wc_to_assets': wc_to_assets,
    }


def generate_scenario_analysis(base_metrics, revenue, cogs):
    """Generate best/worst case scenarios"""
    
    scenarios = {}
    
    # Base case
    scenarios['Base'] = base_metrics
    
    # Best case: 20% improvement in collection, 15% in inventory efficiency
    scenarios['Best'] = {
        'dso': base_metrics['dso'] * 0.80,
        'dio': base_metrics['dio'] * 0.85,
        'dpo': base_metrics['dpo'] * 1.10,
    }
    scenarios['Best']['ccc'] = scenarios['Best']['dso'] + scenarios['Best']['dio'] - scenarios['Best']['dpo']
    scenarios['Best']['impact'] = (base_metrics['ccc'] - scenarios['Best']['ccc']) / 365 * revenue * 0.08
    
    # Worst case: 20% deterioration
    scenarios['Worst'] = {
        'dso': base_metrics['dso'] * 1.20,
        'dio': base_metrics['dio'] * 1.20,
        'dpo': base_metrics['dpo'] * 0.90,
    }
    scenarios['Worst']['ccc'] = scenarios['Worst']['dso'] + scenarios['Worst']['dio'] - scenarios['Worst']['dpo']
    scenarios['Worst']['impact'] = (scenarios['Worst']['ccc'] - base_metrics['ccc']) / 365 * revenue * 0.08
    
    return scenarios


def calculate_cash_flow_impact(metrics, revenue, cogs):
    """Calculate cash flow impact of working capital changes"""
    
    # Calculate daily cash requirements
    daily_revenue = revenue / 365
    daily_cogs = cogs / 365
    
    # Cash tied up in operations
    cash_in_receivables = metrics['dso'] * daily_revenue
    cash_in_inventory = metrics['dio'] * daily_cogs
    cash_from_payables = metrics['dpo'] * daily_cogs
    
    net_cash_tied = cash_in_receivables + cash_in_inventory - cash_from_payables
    
    # Free cash flow impact
    operating_cash_flow = revenue * 0.15  # Assume 15% OCF margin
    fcf_impact_pct = (net_cash_tied / operating_cash_flow) * 100
    
    return {
        'cash_in_receivables': cash_in_receivables,
        'cash_in_inventory': cash_in_inventory,
        'cash_from_payables': cash_from_payables,
        'net_cash_tied': net_cash_tied,
        'fcf_impact_pct': fcf_impact_pct,
    }


# ============================================================================
# VISUALIZATION FUNCTIONS
# ============================================================================

def create_ccc_waterfall(dso, dio, dpo):
    """Create waterfall chart for Cash Conversion Cycle"""
    
    fig = go.Figure(go.Waterfall(
        orientation="v",
        measure=["relative", "relative", "relative", "total"],
        x=["DSO", "DIO", "DPO", "CCC"],
        y=[dso, dio, -dpo, None],
        text=[f"{dso:.1f}", f"{dio:.1f}", f"-{dpo:.1f}", f"{dso+dio-dpo:.1f}"],
        textposition="outside",
        connector={"line": {"color": COLORS['text_secondary']}},
        increasing={"marker": {"color": COLORS['danger']}},
        decreasing={"marker": {"color": COLORS['success']}},
        totals={"marker": {"color": COLORS['accent_gold']}},
    ))
    
    fig.update_layout(
        title="Cash Conversion Cycle Waterfall",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color=COLORS['text_primary']),
        showlegend=False,
        height=400,
    )
    
    return fig


def create_trend_forecast(revenue, cogs, metrics, years=5):
    """Create multi-year working capital forecast"""
    
    growth_scenarios = {
        'Conservative': 0.05,
        'Base': 0.10,
        'Aggressive': 0.15,
    }
    
    fig = go.Figure()
    
    for scenario, growth in growth_scenarios.items():
        wc_values = []
        years_list = []
        
        for year in range(years + 1):
            rev = revenue * (1 + growth) ** year
            rec = (metrics['dso'] / 365) * rev
            inv = (metrics['dio'] / 365) * cogs * (1 + growth) ** year
            pay = (metrics['dpo'] / 365) * cogs * (1 + growth) ** year
            wc = rec + inv - pay
            
            wc_values.append(wc)
            years_list.append(f"Year {year}")
        
        fig.add_trace(go.Scatter(
            x=years_list,
            y=wc_values,
            mode='lines+markers',
            name=f"{scenario} ({growth*100:.0f}%)",
            line=dict(width=3),
        ))
    
    fig.update_layout(
        title="Working Capital Forecast (5-Year)",
        xaxis_title="Year",
        yaxis_title="Working Capital (₹)",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color=COLORS['text_primary']),
        hovermode='x unified',
        height=450,
    )
    
    return fig


def create_sensitivity_analysis(base_ccc, revenue):
    """Create sensitivity analysis heatmap"""
    
    dso_range = np.linspace(-30, 30, 7)
    dio_range = np.linspace(-30, 30, 7)
    
    impact_matrix = []
    
    for dio_change in dio_range:
        row = []
        for dso_change in dso_range:
            ccc_change = dso_change + dio_change
            cash_impact = (ccc_change / 365) * revenue * 0.08
            row.append(cash_impact / 1_000_000)  # In millions
        impact_matrix.append(row)
    
    fig = go.Figure(data=go.Heatmap(
        z=impact_matrix,
        x=[f"{x:+.0f}" for x in dso_range],
        y=[f"{y:+.0f}" for y in dio_range],
        colorscale='RdYlGn_r',
        text=np.round(impact_matrix, 1),
        texttemplate='%{text}M',
        textfont={"size": 10},
        colorbar=dict(title="Cash Impact (₹M)"),
    ))
    
    fig.update_layout(
        title="Sensitivity Analysis: DSO vs DIO Impact on Cash",
        xaxis_title="DSO Change (days)",
        yaxis_title="DIO Change (days)",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color=COLORS['text_primary']),
        height=450,
    )
    
    return fig


def create_benchmark_comparison(metrics):
    """Create benchmark comparison radar chart"""
    
    # Industry benchmarks (example values)
    categories = ['Current Ratio', 'Quick Ratio', 'DSO Efficiency', 'DIO Efficiency', 'CCC Efficiency']
    
    # Normalize metrics to 0-100 scale
    current_values = [
        min(metrics['current_ratio'] / 2.0 * 100, 100),  # Target: 2.0
        min(metrics['quick_ratio'] / 1.5 * 100, 100),    # Target: 1.5
        min(60 / max(metrics['dso'], 1) * 100, 100),     # Target: 60 days
        min(45 / max(metrics['dio'], 1) * 100, 100),     # Target: 45 days
        min(90 / max(abs(metrics['ccc']), 1) * 100, 100) if metrics['ccc'] > 0 else 100,
    ]
    
    industry_avg = [70, 65, 60, 55, 50]  # Example industry averages
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=current_values,
        theta=categories,
        fill='toself',
        name='Current',
        line=dict(color=COLORS['accent_gold'], width=2),
    ))
    
    fig.add_trace(go.Scatterpolar(
        r=industry_avg,
        theta=categories,
        fill='toself',
        name='Industry Avg',
        line=dict(color=COLORS['text_secondary'], width=2),
        opacity=0.6,
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                gridcolor=COLORS['text_secondary'],
            ),
            bgcolor='rgba(0,0,0,0)',
        ),
        showlegend=True,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color=COLORS['text_primary']),
        height=450,
    )
    
    return fig


# ============================================================================
# INSIGHT GENERATION
# ============================================================================

def generate_insights(metrics, cash_flow_impact, scenarios):
    """Generate AI-powered insights"""
    
    insights = []
    
    # Liquidity insights
    if metrics['current_ratio'] < 1.0:
        insights.append({
            'type': 'danger',
            'title': 'Critical Liquidity Risk',
            'message': f"Current ratio of {metrics['current_ratio']:.2f} indicates potential inability to meet short-term obligations. Immediate action required."
        })
    elif metrics['current_ratio'] < 1.5:
        insights.append({
            'type': 'warning',
            'title': 'Liquidity Concern',
            'message': f"Current ratio of {metrics['current_ratio']:.2f} is below healthy threshold of 1.5. Consider strengthening liquidity position."
        })
    else:
        insights.append({
            'type': 'success',
            'title': 'Strong Liquidity',
            'message': f"Current ratio of {metrics['current_ratio']:.2f} indicates healthy liquidity position."
        })
    
    # CCC insights
    if metrics['ccc'] < 0:
        insights.append({
            'type': 'success',
            'title': 'Negative CCC - Cash Advantage',
            'message': f"Negative CCC of {metrics['ccc']:.1f} days means suppliers are financing operations. Excellent working capital management."
        })
    elif metrics['ccc'] > 90:
        insights.append({
            'type': 'warning',
            'title': 'Extended CCC',
            'message': f"CCC of {metrics['ccc']:.1f} days is high. Consider improving collection (DSO: {metrics['dso']:.1f}d) or inventory efficiency (DIO: {metrics['dio']:.1f}d)."
        })
    
    # Cash flow insights
    if cash_flow_impact['fcf_impact_pct'] > 50:
        insights.append({
            'type': 'warning',
            'title': 'Significant Cash Tied in Working Capital',
            'message': f"{cash_flow_impact['fcf_impact_pct']:.1f}% of operating cash flow is tied in working capital. Optimization could release ₹{cash_flow_impact['net_cash_tied']/1_000_000:.1f}M."
        })
    
    # Improvement potential
    improvement_potential = scenarios['Best']['impact']
    if improvement_potential > 1_000_000:
        insights.append({
            'type': 'info',
            'title': 'Optimization Opportunity',
            'message': f"Optimizing CCC could release up to ₹{improvement_potential/1_000_000:.1f}M in cash (Best case scenario)."
        })
    
    return insights


# ============================================================================
# MAIN APPLICATION
# ============================================================================

def main():
    st.set_page_config(**PAGE_CONFIG)
    apply_styles()

    # HEADER
    st.markdown(f"""
    <div class="header-container">
        <h1>{BRANDING['icon']} Enhanced Working Capital AI Agent</h1>
        <p>{BRANDING['name']}</p>
        <p>{BRANDING['instructor']} | {BRANDING['credentials']}</p>
    </div>
    """, unsafe_allow_html=True)

    # ================= SIDEBAR =================

    with st.sidebar:
        st.markdown("### 🧾 Income Statement Inputs")
        revenue = st.number_input("Annual Revenue (₹)", value=20_000_000, step=1_000_000)
        cogs = st.number_input("Annual COGS (₹)", value=14_000_000, step=1_000_000)

        st.markdown("### 💰 Current Assets")
        cash = st.number_input("Cash (₹)", value=2_000_000, step=100_000)
        receivables = st.number_input("Accounts Receivable (₹)", value=5_000_000, step=100_000)
        inventory = st.number_input("Inventory (₹)", value=3_000_000, step=100_000)
        other_ca = st.number_input("Other Current Assets (₹)", value=500_000, step=50_000)

        st.markdown("### 💳 Current Liabilities")
        payables = st.number_input("Accounts Payable (₹)", value=3_500_000, step=100_000)
        short_debt = st.number_input("Short-Term Debt (₹)", value=1_500_000, step=100_000)
        other_cl = st.number_input("Other Current Liabilities (₹)", value=400_000, step=50_000)

    # ================= CALCULATIONS =================

    metrics = calculate_working_capital_metrics(
        revenue, cogs, cash, receivables, inventory, 
        other_ca, payables, short_debt, other_cl
    )
    
    scenarios = generate_scenario_analysis(metrics, revenue, cogs)
    cash_flow_impact = calculate_cash_flow_impact(metrics, revenue, cogs)
    insights = generate_insights(metrics, cash_flow_impact, scenarios)

    # ================= TABS =================

    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
        "📊 Dashboard",
        "📈 Liquidity Analysis",
        "🔄 Operating Cycle",
        "💡 AI Insights",
        "📉 Scenario Analysis",
        "🎯 Sensitivity Analysis",
        "📊 Benchmarking"
    ])

    # -------- DASHBOARD --------
    with tab1:
        st.markdown("### Key Working Capital Metrics")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            metric_card("Net Working Capital", f"₹{metrics['net_wc']/1_000_000:.1f}M")
        with col2:
            metric_card("Current Ratio", f"{metrics['current_ratio']:.2f}")
        with col3:
            metric_card("Cash Conversion Cycle", f"{metrics['ccc']:.0f} days")
        with col4:
            metric_card("Cash Tied Up", f"₹{cash_flow_impact['net_cash_tied']/1_000_000:.1f}M")

        st.markdown("<br>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Current Assets vs Liabilities")
            comparison_df = pd.DataFrame({
                'Category': ['Current Assets', 'Current Liabilities'],
                'Amount': [metrics['total_ca'], metrics['total_cl']]
            })
            fig = px.bar(comparison_df, x='Category', y='Amount', 
                        color='Category',
                        color_discrete_map={'Current Assets': COLORS['success'], 
                                          'Current Liabilities': COLORS['danger']})
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color=COLORS['text_primary']),
                showlegend=False,
                height=350,
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("#### Working Capital Composition")
            composition_df = pd.DataFrame({
                'Component': ['Receivables', 'Inventory', 'Cash', 'Other CA', 'Payables', 'ST Debt', 'Other CL'],
                'Amount': [receivables, inventory, cash, other_ca, -payables, -short_debt, -other_cl],
                'Type': ['Asset', 'Asset', 'Asset', 'Asset', 'Liability', 'Liability', 'Liability']
            })
            fig = px.bar(composition_df, x='Component', y='Amount', color='Type',
                        color_discrete_map={'Asset': COLORS['accent_gold'], 
                                          'Liability': COLORS['danger']})
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color=COLORS['text_primary']),
                height=350,
            )
            st.plotly_chart(fig, use_container_width=True)

    # -------- LIQUIDITY ANALYSIS --------
    with tab2:
        st.markdown("### Liquidity Ratios")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            metric_card("Current Ratio", f"{metrics['current_ratio']:.2f}", 
                       delta=((metrics['current_ratio'] - 2.0) / 2.0 * 100))
        with col2:
            metric_card("Quick Ratio", f"{metrics['quick_ratio']:.2f}",
                       delta=((metrics['quick_ratio'] - 1.5) / 1.5 * 100))
        with col3:
            metric_card("Cash Ratio", f"{metrics['cash_ratio']:.2f}",
                       delta=((metrics['cash_ratio'] - 0.5) / 0.5 * 100))

        st.markdown("<br>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Detailed Balance Sheet")
            balance_sheet = pd.DataFrame({
                'Current Assets': ['Cash', 'Receivables', 'Inventory', 'Other CA', 'Total CA'],
                'Amount (₹)': [f"{cash:,.0f}", f"{receivables:,.0f}", f"{inventory:,.0f}", 
                             f"{other_ca:,.0f}", f"{metrics['total_ca']:,.0f}"],
                '% of Total': [f"{cash/metrics['total_ca']*100:.1f}%", 
                             f"{receivables/metrics['total_ca']*100:.1f}%",
                             f"{inventory/metrics['total_ca']*100:.1f}%",
                             f"{other_ca/metrics['total_ca']*100:.1f}%",
                             "100.0%"]
            })
            st.dataframe(balance_sheet, use_container_width=True, hide_index=True)
        
        with col2:
            st.markdown("#### Current Liabilities Breakdown")
            liabilities = pd.DataFrame({
                'Current Liabilities': ['Payables', 'Short-Term Debt', 'Other CL', 'Total CL'],
                'Amount (₹)': [f"{payables:,.0f}", f"{short_debt:,.0f}", 
                             f"{other_cl:,.0f}", f"{metrics['total_cl']:,.0f}"],
                '% of Total': [f"{payables/metrics['total_cl']*100:.1f}%",
                             f"{short_debt/metrics['total_cl']*100:.1f}%",
                             f"{other_cl/metrics['total_cl']*100:.1f}%",
                             "100.0%"]
            })
            st.dataframe(liabilities, use_container_width=True, hide_index=True)

        st.markdown("<br>", unsafe_allow_html=True)
        
        # Liquidity interpretation
        if metrics['current_ratio'] >= 2.0 and metrics['quick_ratio'] >= 1.5:
            st.success("✅ Strong liquidity position with healthy coverage ratios")
        elif metrics['current_ratio'] >= 1.5 and metrics['quick_ratio'] >= 1.0:
            st.info("ℹ️ Adequate liquidity but room for improvement")
        else:
            st.warning("⚠️ Liquidity concerns - consider strengthening current assets or reducing short-term liabilities")

    # -------- OPERATING CYCLE --------
    with tab3:
        st.markdown("### Operating Cycle & Cash Conversion")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            metric_card("DSO", f"{metrics['dso']:.0f} days")
        with col2:
            metric_card("DIO", f"{metrics['dio']:.0f} days")
        with col3:
            metric_card("DPO", f"{metrics['dpo']:.0f} days")
        with col4:
            metric_card("CCC", f"{metrics['ccc']:.0f} days")

        st.markdown("<br>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Cash Conversion Cycle Waterfall")
            fig = create_ccc_waterfall(metrics['dso'], metrics['dio'], metrics['dpo'])
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("#### Turnover Ratios")
            turnover_df = pd.DataFrame({
                'Metric': ['Receivables Turnover', 'Inventory Turnover', 'Payables Turnover'],
                'Times per Year': [
                    f"{metrics['receivables_turnover']:.2f}x",
                    f"{metrics['inventory_turnover']:.2f}x",
                    f"{metrics['payables_turnover']:.2f}x"
                ],
                'Days': [
                    f"{metrics['dso']:.0f}",
                    f"{metrics['dio']:.0f}",
                    f"{metrics['dpo']:.0f}"
                ]
            })
            st.dataframe(turnover_df, use_container_width=True, hide_index=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # Cash Flow Impact
        st.markdown("#### Cash Flow Impact Analysis")
        
        impact_data = pd.DataFrame({
            'Component': ['Cash in Receivables', 'Cash in Inventory', 'Cash from Payables', 'Net Cash Tied'],
            'Amount (₹M)': [
                cash_flow_impact['cash_in_receivables'] / 1_000_000,
                cash_flow_impact['cash_in_inventory'] / 1_000_000,
                -cash_flow_impact['cash_from_payables'] / 1_000_000,
                cash_flow_impact['net_cash_tied'] / 1_000_000
            ]
        })
        
        fig = px.bar(impact_data, x='Component', y='Amount (₹M)', 
                    color='Amount (₹M)',
                    color_continuous_scale=['red', 'yellow', 'green'])
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color=COLORS['text_primary']),
            showlegend=False,
            height=350,
        )
        st.plotly_chart(fig, use_container_width=True)

    # -------- AI INSIGHTS --------
    with tab4:
        st.markdown("### AI-Powered Working Capital Insights")
        
        for insight in insights:
            if insight['type'] == 'success':
                st.success(f"**{insight['title']}**: {insight['message']}")
            elif insight['type'] == 'warning':
                st.warning(f"**{insight['title']}**: {insight['message']}")
            elif insight['type'] == 'danger':
                st.error(f"**{insight['title']}**: {insight['message']}")
            else:
                st.info(f"**{insight['title']}**: {insight['message']}")

        st.markdown("<br>", unsafe_allow_html=True)

        # Actionable Recommendations
        st.markdown("### 🎯 Actionable Recommendations")
        
        recommendations = []
        
        if metrics['dso'] > 60:
            days_reduction = metrics['dso'] - 60
            cash_release = (days_reduction / 365) * revenue
            recommendations.append(f"**Accelerate Collections**: Reduce DSO from {metrics['dso']:.0f} to 60 days → Release ₹{cash_release/1_000_000:.1f}M cash")
        
        if metrics['dio'] > 45:
            days_reduction = metrics['dio'] - 45
            cash_release = (days_reduction / 365) * cogs
            recommendations.append(f"**Optimize Inventory**: Reduce DIO from {metrics['dio']:.0f} to 45 days → Release ₹{cash_release/1_000_000:.1f}M cash")
        
        if metrics['dpo'] < 45:
            days_increase = 45 - metrics['dpo']
            cash_benefit = (days_increase / 365) * cogs
            recommendations.append(f"**Negotiate Payment Terms**: Increase DPO from {metrics['dpo']:.0f} to 45 days → Free up ₹{cash_benefit/1_000_000:.1f}M cash")
        
        if metrics['current_ratio'] < 1.5:
            recommendations.append(f"**Strengthen Liquidity**: Target current ratio of 1.5-2.0 (currently {metrics['current_ratio']:.2f})")
        
        if recommendations:
            for i, rec in enumerate(recommendations, 1):
                st.markdown(f"{i}. {rec}")
        else:
            st.success("Working capital management is currently optimized. Maintain current practices.")

        st.markdown("<br>", unsafe_allow_html=True)

        # 5-Year Forecast
        st.markdown("### 📈 Working Capital Forecast")
        fig = create_trend_forecast(revenue, cogs, metrics)
        st.plotly_chart(fig, use_container_width=True)

    # -------- SCENARIO ANALYSIS --------
    with tab5:
        st.markdown("### Multi-Scenario Working Capital Analysis")
        
        scenario_comparison = pd.DataFrame({
            'Scenario': ['Best Case', 'Base Case', 'Worst Case'],
            'DSO (days)': [scenarios['Best']['dso'], metrics['dso'], scenarios['Worst']['dso']],
            'DIO (days)': [scenarios['Best']['dio'], metrics['dio'], scenarios['Worst']['dio']],
            'DPO (days)': [scenarios['Best']['dpo'], metrics['dpo'], scenarios['Worst']['dpo']],
            'CCC (days)': [scenarios['Best']['ccc'], metrics['ccc'], scenarios['Worst']['ccc']],
            'Cash Impact (₹M)': [
                scenarios['Best']['impact'] / 1_000_000,
                0,
                scenarios['Worst']['impact'] / 1_000_000
            ]
        })
        
        st.dataframe(scenario_comparison.style.format({
            'DSO (days)': '{:.1f}',
            'DIO (days)': '{:.1f}',
            'DPO (days)': '{:.1f}',
            'CCC (days)': '{:.1f}',
            'Cash Impact (₹M)': '{:.2f}'
        }), use_container_width=True, hide_index=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # Scenario comparison chart
        scenario_df = pd.DataFrame({
            'Scenario': ['Best', 'Base', 'Worst'] * 3,
            'Metric': ['DSO'] * 3 + ['DIO'] * 3 + ['CCC'] * 3,
            'Days': [
                scenarios['Best']['dso'], metrics['dso'], scenarios['Worst']['dso'],
                scenarios['Best']['dio'], metrics['dio'], scenarios['Worst']['dio'],
                scenarios['Best']['ccc'], metrics['ccc'], scenarios['Worst']['ccc']
            ]
        })
        
        fig = px.bar(scenario_df, x='Metric', y='Days', color='Scenario',
                    barmode='group',
                    color_discrete_map={'Best': COLORS['success'], 
                                       'Base': COLORS['accent_gold'],
                                       'Worst': COLORS['danger']})
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color=COLORS['text_primary']),
            height=400,
        )
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # Custom scenario builder
        st.markdown("### 🔧 Build Custom Scenario")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            custom_dso = st.slider("Target DSO (days)", 
                                  int(metrics['dso'] * 0.5), 
                                  int(metrics['dso'] * 1.5), 
                                  int(metrics['dso']))
        with col2:
            custom_dio = st.slider("Target DIO (days)", 
                                  int(metrics['dio'] * 0.5), 
                                  int(metrics['dio'] * 1.5), 
                                  int(metrics['dio']))
        with col3:
            custom_dpo = st.slider("Target DPO (days)", 
                                  int(metrics['dpo'] * 0.5), 
                                  int(metrics['dpo'] * 1.5), 
                                  int(metrics['dpo']))
        
        custom_ccc = custom_dso + custom_dio - custom_dpo
        custom_impact = (metrics['ccc'] - custom_ccc) / 365 * revenue * 0.08
        
        col1, col2 = st.columns(2)
        with col1:
            metric_card("Custom CCC", f"{custom_ccc:.0f} days")
        with col2:
            metric_card("Cash Impact", f"₹{custom_impact/1_000_000:.1f}M")

    # -------- SENSITIVITY ANALYSIS --------
    with tab6:
        st.markdown("### DSO vs DIO Sensitivity Matrix")
        fig = create_sensitivity_analysis(metrics['ccc'], revenue)
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown("### Key Sensitivity Insights")
        st.info("The heatmap shows cash impact (in millions) from simultaneous changes in DSO and DIO. Green indicates cash release, red indicates cash requirement.")

    # -------- BENCHMARKING --------
    with tab7:
        st.markdown("### Performance vs Industry Benchmarks")
        fig = create_benchmark_comparison(metrics)
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown("### Industry Benchmark Comparison")
        
        benchmark_df = pd.DataFrame({
            'Metric': ['Current Ratio', 'Quick Ratio', 'DSO', 'DIO', 'DPO', 'CCC'],
            'Your Company': [
                f"{metrics['current_ratio']:.2f}",
                f"{metrics['quick_ratio']:.2f}",
                f"{metrics['dso']:.0f}",
                f"{metrics['dio']:.0f}",
                f"{metrics['dpo']:.0f}",
                f"{metrics['ccc']:.0f}"
            ],
            'Industry Average': ['2.00', '1.50', '60', '45', '45', '60'],
            'Best in Class': ['2.50', '2.00', '45', '30', '60', '15']
        })
        
        st.dataframe(benchmark_df, use_container_width=True, hide_index=True)

    # ================= FOOTER =================
    
    st.divider()
    st.markdown(f"""
    <div style="text-align:center; color:{COLORS['accent_gold']}; font-weight:bold;">
        {BRANDING['icon']} {BRANDING['name']} | Built with Advanced Financial Analytics
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
