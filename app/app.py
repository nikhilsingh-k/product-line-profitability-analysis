import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

# ─── Page config & dark theme ───────────────────────────────────────────────
st.set_page_config(page_title="Nassau Candy Profitability", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #e0e0e0; }
    h1 { color: #f0d25f !important; font-size: 2.1rem; margin-bottom: 0.3rem; }
    h2, h3 { color: #e6e6e6 !important; margin-top: 1.2rem; margin-bottom: 0.6rem; }
    .stMetric {
        background-color: #1a1f2e;
        border-radius: 8px;
        padding: 16px;
        border: 1px solid #2a3345;
        text-align: center;
    }
    .stMetric label { color: #a0a0c0 !important; font-size: 0.92rem; }
    .stMetric div[data-testid="stMetricValue"] { color: #ffffff !important; font-weight: 600; font-size: 1.45rem; }
    .sidebar .sidebar-content { background-color: #161b22; }
    hr { border-color: #2a3345; margin: 1.8rem 0; }
    .stTabs [data-baseweb="tab-list"] { background: #161b22; border-bottom: 1px solid #2a3345; }
    .stTabs [data-baseweb="tab"] { color: #a0a0c0; padding: 10px 20px; }
    .stTabs [aria-selected="true"] { color: #f0d25f !important; border-bottom: 3px solid #f0d25f !important; }
    .insight-box {
        background: rgba(240, 210, 95, 0.08);
        border-left: 4px solid #f0d25f;
        padding: 1.2rem;
        border-radius: 6px;
        margin: 1.4rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# ─── Load data ──────────────────────────────────────────────────────────────
csv_path = os.path.join(os.path.dirname(__file__), "..", "data", "Nassau Candy Distributor.csv")

@st.cache_data
def load_data():
    df = pd.read_csv(csv_path)
    df['Order Date'] = pd.to_datetime(df['Order Date'], format='%d-%m-%Y', errors='coerce')
    df['Gross Margin %'] = (df['Gross Profit'] / df['Sales'] * 100).round(2)
    df['Profit per Unit'] = df['Gross Profit'] / df['Units']
    return df

df = load_data()

# ─── Sidebar filters ────────────────────────────────────────────────────────
with st.sidebar:
    st.header("Filters")
    
    date_range = st.date_input(
        "Order date range",
        value=(df['Order Date'].min().date(), df['Order Date'].max().date())
    )
    
    divisions = sorted(df['Division'].unique())
    selected_div = st.multiselect("Division", divisions, default=divisions)
    
    min_margin = st.slider(
        "Minimum Gross Margin %",
        min_value=0,
        max_value=100,
        value=35,
        step=1
    )
    
    prod_search = st.text_input("Search product name", "").strip()

    st.markdown("---")
    st.caption("Built by a Developer • [LinkedIn](https://www.linkedin.com/in/nikhilsingh-k/) • [GitHub](https://github.com/nikhilsingh-k)")

# ─── Dynamic title ──────────────────────────────────────────────────────────
active_divs = ", ".join(selected_div) if len(selected_div) < len(divisions) else "All Divisions"
title_text = "Nassau Candy Distributor – Profitability & Margin Dashboard"
st.title(title_text)
st.caption("Product line margin & profit analysis • 2024–2025 data")

# ─── Apply filters ──────────────────────────────────────────────────────────
f_df = df.copy()

if len(date_range) == 2:
    f_df = f_df[(f_df['Order Date'].dt.date >= date_range[0]) & 
                (f_df['Order Date'].dt.date <= date_range[1])]

if selected_div:
    f_df = f_df[f_df['Division'].isin(selected_div)]

f_df = f_df[f_df['Gross Margin %'] >= min_margin]

if prod_search.strip():
    f_df = f_df[f_df['Product Name'].str.contains(prod_search.strip(), case=False, na=False)]

# ─── KPI cards – with all 5 KPIs ────────────────────────────────────────────
total_sales = f_df['Sales'].sum()
total_profit = f_df['Gross Profit'].sum()
total_units = f_df['Units'].sum()

cols = st.columns(5)
cols[0].metric("Total Sales", f"${total_sales:,.0f}")
cols[1].metric("Gross Profit", f"${total_profit:,.0f}")
cols[2].metric("Gross Margin", f"{(total_profit / total_sales * 100):.1f}%")
cols[3].metric("Profit per Unit", f"${(total_profit / total_units):.2f}" if total_units > 0 else "N/A")
cols[4].metric("Rows shown", f"{len(f_df):,}")

st.markdown("---")

# ─── Tabs ───────────────────────────────────────────────────────────────────
tab1, tab2, tab3, tab4 = st.tabs([
    "Product Profitability Overview",
    "Division Performance",
    "Cost vs Margin Diagnostics",
    "Profit Concentration Analysis"
])

# ─── Tab 1: Product Profitability Overview ──────────────────────────────────
with tab1:
    st.subheader("Product-level margin leaderboard & contribution")
    
    prod = f_df.groupby(['Product Name', 'Division']).agg({
        'Sales': 'sum',
        'Gross Profit': 'sum',
        'Gross Margin %': 'mean',
        'Units': 'sum',
        'Profit per Unit': 'mean'  
    }).reset_index().round(2)
    
    # Add contribution percentages
    prod['Revenue Contribution %'] = (prod['Sales'] / total_sales * 100).round(1)
    prod['Profit Contribution %'] = (prod['Gross Profit'] / total_profit * 100).round(1)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Top by Gross Profit**")
        fig_profit = px.bar(prod.nlargest(10, 'Gross Profit'),
                            x='Product Name', y='Gross Profit', color='Division',
                            height=560, template="plotly_dark")
        fig_profit.update_layout(xaxis_tickangle=45, font_size=13, margin_b=140)
        st.plotly_chart(fig_profit, use_container_width=True)
    
    with col2:
        st.markdown("**Top by Gross Margin %**")
        fig_margin = px.bar(prod.nlargest(10, 'Gross Margin %'),
                            x='Product Name', y='Gross Margin %', color='Division',
                            height=560, template="plotly_dark")
        fig_margin.update_layout(xaxis_tickangle=45, font_size=13, margin_b=140)
        st.plotly_chart(fig_margin, use_container_width=True)
    
    with st.expander("Full product table (with all KPIs)"):
        st.dataframe(prod[['Product Name', 'Division', 'Sales', 'Revenue Contribution %', 
                           'Gross Profit', 'Profit Contribution %', 'Gross Margin %', 
                           'Profit per Unit']], use_container_width=True)

# ─── Tab 2: Division Performance ────────────────────────────────────────────
with tab2:
    st.subheader("Division Performance")
    
    div = f_df.groupby('Division').agg({
        'Sales': 'sum',
        'Gross Profit': 'sum',
        'Gross Margin %': 'mean'
    }).reset_index().round(2)
    
    colA, colB = st.columns([6, 5])
    
    with colA:
        st.markdown("**Revenue vs Gross Profit by Division**")
        fig_bar = px.bar(div, x='Division', y=['Sales', 'Gross Profit'],
                         barmode='group', height=480, template="plotly_dark")
        st.plotly_chart(fig_bar, use_container_width=True)
    
    with colB:
        st.markdown("**Margin Distribution by Division**")
        fig_box = px.box(f_df, x='Division', y='Gross Margin %',
                         color='Division', points='outliers',
                         height=480, template="plotly_dark")
        st.plotly_chart(fig_box, use_container_width=True)

# ─── Tab 3: Cost vs Margin Diagnostics ──────────────────────────────────────
with tab3:
    st.subheader("Cost vs Margin Diagnostics")
    
    agg = f_df.groupby('Product Name').agg({
        'Sales': 'sum',
        'Cost': 'sum',
        'Gross Profit': 'sum',
        'Gross Margin %': 'mean'
    }).reset_index().round(2)
    
    colX, colY = st.columns([7, 5])
    
    with colX:
        st.markdown("**Cost vs Sales Scatter (size = Profit)**")
        fig_scatter = px.scatter(
            agg,
            x='Sales',
            y='Cost',
            size='Gross Profit',
            color='Gross Margin %',
            hover_name='Product Name',
            color_continuous_scale='RdYlGn_r',
            height=520,
            template="plotly_dark"
        )
        st.plotly_chart(fig_scatter, use_container_width=True)
    
    with colY:
        st.markdown(f"**Margin Risk Products** (< {min_margin}%)")
        risk = agg[agg['Gross Margin %'] < min_margin].sort_values('Gross Margin %')
        if risk.empty:
            st.success("No products below the selected margin threshold.")
        else:
            st.dataframe(risk[['Product Name', 'Sales', 'Cost', 'Gross Profit', 'Gross Margin %']], use_container_width=True)

# ─── Tab 4: Profit Concentration Analysis ───────────────────────────────────
with tab4:
    st.subheader("Profit Concentration Analysis")
    
    pareto = f_df.groupby('Product Name')['Gross Profit'].sum().sort_values(ascending=False).reset_index()
    pareto['cum_%'] = pareto['Gross Profit'].cumsum() / pareto['Gross Profit'].sum() * 100
    
    fig_pareto = go.Figure()
    fig_pareto.add_trace(go.Bar(x=pareto['Product Name'][:15], y=pareto['Gross Profit'][:15], name='Profit'))
    fig_pareto.add_trace(go.Scatter(x=pareto['Product Name'][:15], y=pareto['cum_%'][:15],
                                    mode='lines+markers', name='Cumulative %', yaxis='y2'))
    fig_pareto.update_layout(
        title="Pareto – Profit Contribution by Product",
        height=520,
        template="plotly_dark",
        yaxis2=dict(title='Cumulative %', overlaying='y', side='right', range=[0,110])
    )
    st.plotly_chart(fig_pareto, use_container_width=True)
    
    # Dependency indicators
    if len(pareto) >= 5:
        top3 = pareto['cum_%'].iloc[2]
        top5 = pareto['cum_%'].iloc[4]
        top10 = pareto['cum_%'].iloc[9] if len(pareto) >= 10 else 100.0
        sku80 = (pareto['cum_%'] <= 80).sum()
        
        st.markdown(f"""
        <div class="insight-box">
        <strong>Key Dependency Indicators:</strong><br><br>
        • Top 3 products → <strong>{top3:.1f}%</strong> of total gross profit<br>
        • Top 5 products → <strong>{top5:.1f}%</strong> of total gross profit<br>
        • Top 10 products → <strong>{top10:.1f}%</strong> of total gross profit<br>
        • ≈80% of profit comes from <strong>{sku80}</strong> products
        </div>
        """, unsafe_allow_html=True)

# ─── Margin Volatility Chart ────────────────────────────────────────────────
with tab1:
    st.subheader("Margin Volatility Over Time")
    
    monthly_vol = (
        f_df
        .assign(month=f_df['Order Date'].dt.to_period('M').astype(str))
        .groupby('month')['Gross Margin %']
        .agg(['mean', 'std'])
        .reset_index()
        .rename(columns={'mean': 'Avg Margin %', 'std': 'Margin Volatility (Std Dev)'})
    )
    
    fig_vol = px.line(
        monthly_vol,
        x='month',
        y=['Avg Margin %', 'Margin Volatility (Std Dev)'],
        height=480,
        template="plotly_dark",
        title="Monthly Margin Trend & Volatility"
    )
    fig_vol.update_layout(showlegend=True, legend_orientation="h", legend_y=-0.25)
    st.plotly_chart(fig_vol, use_container_width=True)

# ─── Download ───────────────────────────────────────────────────────────────
st.markdown("---")
if not f_df.empty:
    st.download_button(
        "Download Filtered Data (CSV)",
        f_df.to_csv(index=False).encode('utf-8'),
        file_name="nassau_profitability_filtered.csv",
        mime="text/csv"
    )
