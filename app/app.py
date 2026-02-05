import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

st.set_page_config(page_title="Nassau Candy Profitability Dashboard", layout="wide")

st.title("📊 Product Line Profitability & Margin Analysis")
st.write("Interactive dashboard for Nassau Candy Distributor")
csv_path = os.path.join(os.path.dirname(__file__), "..", "data", "Nassau Candy Distributor.csv")

@st.cache_data
def load_data():
    df = pd.read_csv(csv_path)
    df = df[(df['Sales'] > 0) & (df['Units'] > 0)]
    df['Division'] = df['Division'].str.strip().str.title()
    df['Gross_Margin_Percent'] = (df['Gross Profit'] / df['Sales']) * 100
    return df

df = load_data()

st.sidebar.header("Filters")

division = st.sidebar.selectbox(
    "Select Division",
    ["All"] + sorted(df['Division'].unique().tolist())
)

margin_threshold = st.sidebar.slider(
    "Minimum Gross Margin (%)",
    min_value=0,
    max_value=100,
    value=10
)

filtered_df = df.copy()

if division != "All":
    filtered_df = filtered_df[filtered_df['Division'] == division]

filtered_df = filtered_df[filtered_df['Gross_Margin_Percent'] >= margin_threshold]

st.subheader("Key Performance Indicators")

col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", f"{filtered_df['Sales'].sum():,.0f}")
col2.metric("Total Profit", f"{filtered_df['Gross Profit'].sum():,.0f}")
col3.metric("Avg Margin (%)", f"{filtered_df['Gross_Margin_Percent'].mean():.2f}")

st.subheader("Top Products by Gross Profit")

top_products = (
    filtered_df.groupby('Product Name')['Gross Profit']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

fig, ax = plt.subplots()
top_products.plot(kind='bar', ax=ax)
plt.xticks(rotation=45, ha='right')
st.pyplot(fig)

st.subheader("Sales vs Gross Margin")

fig2, ax2 = plt.subplots()
ax2.scatter(filtered_df['Sales'], filtered_df['Gross_Margin_Percent'])
ax2.set_xlabel("Sales")
ax2.set_ylabel("Gross Margin (%)")
st.pyplot(fig2)

st.subheader("Filtered Product Data")
st.dataframe(filtered_df[['Product Name', 'Division', 'Sales', 'Gross Profit', 'Gross_Margin_Percent']])