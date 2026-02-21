Nassau Candy Distributor – Profitability & Margin Dashboard

An interactive business intelligence dashboard built using Streamlit to analyze product-level and division-level profitability.

This project transforms raw transactional order data into actionable financial insights focused on gross margin performance, profit concentration, and cost diagnostics.

Project Objective

For distributors, high sales volume does not always mean high profitability.
This dashboard answers critical business questions:

Which products truly drive gross profit?

Are high-revenue products actually high-margin?

Which divisions underperform financially?

How concentrated is overall profit?

Where do margin risks exist?

The goal is to move beyond revenue metrics and enable margin-focused decision-making.

Key Features
Interactive Filters

Order date range selector

Division multi-select filter

Minimum gross margin threshold slider

Product name search

All filters use AND logic for precise slicing.

KPI Overview

Total Sales

Gross Profit

Gross Margin (%)

Profit per Unit

Rows Shown (Filtered Records)

Product Profitability Analysis

Top products by Gross Profit

Top products by Gross Margin %

Revenue Contribution %

Profit Contribution %

Profit per Unit

Full expandable product-level KPI table

Division Performance Dashboard

Revenue vs Gross Profit comparison

Margin distribution by division (box plot)

Cross-division profitability comparison

Cost vs Margin Diagnostics

Cost vs Sales scatter plot (bubble size = profit)

Margin-risk product identification

Detects:

Cost-heavy, low-margin SKUs

Pricing inefficiencies

Structural margin weakness

Profit Concentration (Pareto) Analysis

Top profit-contributing products

Cumulative profit curve

Dependency indicators:

% profit from top 3 products

% profit from top 5 products

% profit from top 10 products

Number of products generating ~80% of profit

Margin Volatility Analysis

Monthly average gross margin trend

Margin standard deviation (volatility)

Identifies unstable pricing or cost fluctuations over time

Data Export

Download filtered dataset as CSV

Tech Stack

Python

Streamlit

Pandas

Plotly (Express + Graph Objects)

Data Visualization & Exploratory Data Analysis (EDA)

Project Structure
project-root/
│
├── app/
│   └── app.py
│
├── data/
│   └── Nassau Candy Distributor.csv
│
├── requirements.txt
└── README.md
How to Run Locally

Install dependencies:

pip install -r requirements.txt

Run the dashboard:

streamlit run app/app.py

The application will open in your browser at:

http://localhost:8501
Deployment

This dashboard is deployed using Streamlit Cloud with GitHub integration.

Public deployment link available on profile.

Business Insights Generated

A small subset of products generates the majority of total profit.

Some high-revenue products operate at low margins.

Certain divisions show revenue-profit imbalance.

Margin-risk products are flagged dynamically.

Profit concentration exposes dependency risk.

Margin volatility analysis highlights financial instability periods.

Strategic Recommendations

Reprice high-volume, low-margin products.

Renegotiate manufacturing or sourcing costs.

Review consistently loss-making products.

Diversify profit sources to reduce concentration risk.

Monitor monthly margin volatility to stabilize financial performance.

Conclusion

This project demonstrates how profitability-focused analytics can drive smarter business decisions.

Rather than relying on sales volume alone, the dashboard enables:

Margin optimization

Risk mitigation

Portfolio rationalization

Financial efficiency improvement

It showcases end-to-end data analytics workflow — from cleaning and aggregation to interactive business intelligence deployment.

Author

Built by Nikhil Singh
BCA (AI & ML) Student
Machine Learning & Data Analytics Enthusiast

GitHub: https://github.com/nikhilsingh-k

LinkedIn: https://www.linkedin.com/in/nikhilsingh-k/
