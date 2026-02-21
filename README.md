# Nassau Candy Distributor – Profitability & Margin Intelligence Dashboard

[Live Application](https://nikhil-profitability-dashboard.streamlit.app/)

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![Plotly](https://img.shields.io/badge/Plotly-Visualization-purple)
![Deployment](https://img.shields.io/badge/Deployment-Live-green)

---

## Overview

This project is an end-to-end profitability intelligence dashboard built using Streamlit, Pandas, and Plotly.

It transforms raw transactional sales data into strategic financial insights by analyzing:

- Product-level profitability  
- Division performance  
- Margin volatility  
- Cost-to-sales diagnostics  
- Profit concentration risk  

The objective is to move beyond revenue reporting and enable margin-driven business decision-making.

---

## Live Demo

Access the deployed dashboard here:

https://nikhil-profitability-dashboard.streamlit.app/

---

## Dashboard Preview

![Dashboard Overview](assets/dashboard-overview.png)
![Product Profitability Leaderboard](assets/product-profitability.png)
![Pareto Profit Concentration](assets/pareto-analysis.png)

---

## Business Problem

Revenue growth does not guarantee profitability.

Distributors frequently encounter:

- High-volume products with low margins  
- Hidden cost-heavy SKUs  
- Revenue-profit mismatch across divisions  
- Over-dependence on a small number of products  
- Margin instability over time  

This dashboard provides a structured analytical framework to uncover and quantify these risks.

---

## Key Features

### Interactive Filtering
- Order date range selection  
- Division multi-select filter  
- Minimum gross margin threshold  
- Product name search  
- Dynamic AND-based filtering logic  

### KPI Monitoring
- Total Sales  
- Gross Profit  
- Gross Margin (%)  
- Profit per Unit  
- Record count  

### Product-Level Profitability
- Top products by Gross Profit  
- Top products by Gross Margin %  
- Revenue contribution percentage  
- Profit contribution percentage  
- Expandable full KPI table  

### Division Performance Analysis
- Revenue vs Gross Profit comparison  
- Margin distribution visualization  
- Performance imbalance detection  

### Cost vs Margin Diagnostics
- Cost vs Sales scatter analysis  
- Bubble size proportional to profit  
- Margin risk identification  

### Profit Concentration (Pareto Analysis)
- Cumulative profit contribution curve  
- Top 3 / Top 5 / Top 10 dependency indicators  
- 80% concentration threshold detection  

### Margin Volatility Analysis
- Monthly average margin trend  
- Standard deviation tracking  
- Detection of unstable pricing patterns  

### Data Export
- Download filtered dataset as CSV  

---

## Analytical Insights

The analysis reveals:

- A small subset of products generates the majority of total profit  
- Several high-revenue products operate at thin margins  
- Certain divisions show revenue-profit imbalance  
- Profit concentration exposes dependency risk  
- Margin volatility highlights operational instability  

---

## Strategic Recommendations

- Reprice high-volume, low-margin SKUs  
- Optimize sourcing to reduce cost-heavy products  
- Rationalize underperforming product lines  
- Diversify profit contribution across products  
- Monitor margin volatility for long-term stability  

---

## Research Paper

A structured research-style report documenting the complete analytical workflow is included in the `report/` directory.

The paper covers:

- Problem definition  
- Dataset overview  
- Data preprocessing methodology  
- Profitability metric engineering  
- Pareto concentration modeling  
- Margin volatility analysis  
- Business interpretation  
- Strategic recommendations  
- Limitations and future scope  

File location:

report/Profitability_Analysis_Research_Paper.pdf

---

## Tech Stack

- Python  
- Streamlit  
- Pandas  
- Plotly (Express + Graph Objects)  
- Exploratory Data Analysis  
- Financial Metric Engineering  

---

## Project Structure

```
project-root/
│
├── app/
│   └── app.py
│
├── assets/
│   ├── dashboard-overview.png
│   ├── product-profitability.png
│   └── pareto-analysis.png
│
├── data/
│   └── Nassau Candy Distributor.csv
│
├── notebooks/
│   ├── 01_data_overview.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_profitability_metrics.ipynb
│   ├── 04_visual_analysis.ipynb
│   └── 05_insights_recommendations.ipynb
│
├── report/
│   └── Profitability_Analysis_Research_Paper.pdf
│
├── requirements.txt
└── README.md
```

---

## How to Run Locally

Install dependencies:

```
pip install -r requirements.txt
```

Run the application:

```
streamlit run app/app.py
```

Open in browser:

```
http://localhost:8501
```

---

## Deployment

The dashboard is deployed using Streamlit Cloud with GitHub integration, enabling continuous deployment and live updates.

Live URL:  
https://nikhil-profitability-dashboard.streamlit.app/

---

## Conclusion

This project demonstrates how profitability-focused analytics can drive smarter business decisions beyond surface-level revenue metrics.

It showcases:

- Structured data preprocessing  
- Financial metric engineering  
- Advanced exploratory analysis  
- Interactive dashboard development  
- Cloud deployment  
- Research-style documentation  

The solution bridges data analytics, business intelligence, and AI-driven financial reasoning.

---

## Author

Nikhil Kumar Singh  
BCA (AI & ML)  
Aspiring AI & Software Engineer | Machine Learning | Data Analytics  

GitHub: https://github.com/nikhilsingh-k  
LinkedIn: https://www.linkedin.com/in/nikhilsingh-k/
