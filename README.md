# Nassau Candy Distributor – Profitability & Margin Dashboard

[Live Application](https://nikhil-profitability-dashboard.streamlit.app/)

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![Plotly](https://img.shields.io/badge/Plotly-Visualization-purple)
![Deployment](https://img.shields.io/badge/Deployment-Live-green)

---

## Overview

This project is an end-to-end profitability analytics dashboard built using Streamlit.  
It analyzes product-level and division-level financial performance to uncover margin inefficiencies, profit concentration risks, and cost-performance mismatches.

The dashboard transforms raw transactional order data into actionable business intelligence for strategic decision-making.

---

## Dashboard Preview

![Dashboard Overview](assets/dashboard-overview.png)
![Product Profitability](assets/product-profitability.png)
![Pareto Analysis](assets/pareto-analysis.png)

---

## Business Problem

High sales volume does not always translate into high profitability.

Distributors often face challenges such as:

- High-volume products generating low margins  
- Revenue-profit imbalance across divisions  
- Hidden cost-heavy SKUs  
- Profit concentration risk from limited products  

This dashboard provides a structured analytical framework to identify and address these issues.

---

## Core Features

### Interactive Filtering
- Order date range selection  
- Division multi-select filter  
- Minimum gross margin threshold slider  
- Product name search  
- AND-based filter logic  

### KPI Dashboard
- Total Sales  
- Gross Profit  
- Gross Margin (%)  
- Profit per Unit  
- Filtered record count  

### Product-Level Profitability
- Top products by Gross Profit  
- Top products by Gross Margin %  
- Revenue Contribution %  
- Profit Contribution %  
- Expandable detailed KPI table  

### Division Performance Analysis
- Revenue vs Gross Profit comparison  
- Margin distribution across divisions  
- Identification of financial imbalance  

### Cost vs Margin Diagnostics
- Cost vs Sales scatter visualization  
- Bubble size representing profit  
- Margin-risk product identification  

### Profit Concentration (Pareto Analysis)
- Cumulative profit contribution curve  
- Dependency indicators:
  - % profit from top 3 products  
  - % profit from top 5 products  
  - % profit from top 10 products  
  - Number of products generating ~80% of total profit  

### Margin Volatility Analysis
- Monthly average gross margin trend  
- Margin standard deviation over time  
- Detection of unstable pricing or cost behavior  

### Data Export
- Download filtered dataset as CSV  

---

## Business Insights Generated

- A small subset of products contributes the majority of total profit  
- Several high-revenue products operate at low margins  
- Certain divisions show revenue-profit mismatch  
- Profit concentration reveals structural dependency risk  
- Margin volatility highlights financial instability periods  

---

## Strategic Recommendations

- Reprice high-volume, low-margin products  
- Renegotiate sourcing or manufacturing costs  
- Review and rationalize loss-making SKUs  
- Diversify profit sources to reduce dependency risk  
- Monitor margin volatility for financial stability  

---

## Tech Stack

- Python  
- Streamlit  
- Pandas  
- Plotly (Express and Graph Objects)  
- Data Visualization  
- Exploratory Data Analysis  

---

## Project Structure

```
project-root/
│
├── app/
│   └── app.py
│
├── data/
│   └── Nassau Candy Distributor.csv
│
├── assets/
│   ├── dashboard-overview.png
│   ├── product-profitability.png
│   └── pareto-analysis.png
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

Run the dashboard:

```
streamlit run app/app.py
```

Open in browser:

```
http://localhost:8501
```

---

## Deployment

The application is deployed using Streamlit Cloud with GitHub integration, enabling real-time interaction and continuous deployment.

Live link:  
https://nikhil-profitability-dashboard.streamlit.app/

---

## Conclusion

This project demonstrates how profitability-focused analytics can drive smarter business decisions beyond surface-level revenue metrics.

It showcases:

- Data cleaning and transformation  
- KPI engineering  
- Financial performance analysis  
- Interactive dashboard design  
- Cloud deployment  

The solution bridges data analytics with business strategy, making it suitable for data analyst, business intelligence, and machine learning-oriented roles.

---

## Author

Nikhil Kumar Singh  
BCA (AI & ML) Student  
Aspiring AI & Software Engineer | Machine Learning | Data Analytics  

GitHub  : https://github.com/nikhilsingh-k  
LinkedIn: https://www.linkedin.com/in/nikhilsingh-k/
