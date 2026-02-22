# Nassau Candy Distributor – Profitability Intelligence Dashboard

[Live Application](https://nikhil-profitability-dashboard.streamlit.app/)  
[Research Paper DOI](https://doi.org/10.5281/zenodo.18729616)

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![Plotly](https://img.shields.io/badge/Plotly-Visualization-purple)
![Deployment](https://img.shields.io/badge/Deployment-Live-green)
![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18729616.svg)

---

## Overview

This project presents an end-to-end profitability intelligence system designed to analyze product-level and division-level financial performance in a distribution-based business model.

The system transforms raw transactional sales data into structured financial insights using engineered profitability metrics, Pareto modeling, cost diagnostics, and margin volatility analysis.

The objective is to move beyond revenue reporting and enable margin-driven strategic decision-making.

---

## Live Dashboard

Access the deployed Streamlit application:

https://nikhil-profitability-dashboard.streamlit.app/

---

## Research Publication

This project is formally published on Zenodo with a permanent DOI:

https://doi.org/10.5281/zenodo.18729616

The research paper documents:

- Financial metric engineering  
- Profit concentration modeling  
- Margin volatility diagnostics  
- Cost-to-sales imbalance detection  
- Strategic portfolio optimization recommendations  

---

## Dashboard Preview

![Dashboard Overview](assets/dashboard-overview.png)
![Product Profitability](assets/product-profitability.png)
![Pareto Analysis](assets/pareto-analysis.png)

---

## Business Problem

Revenue growth does not guarantee profitability.

Distribution businesses frequently face:

- High-volume, low-margin products  
- Profit concentration dependency  
- Cost-heavy SKUs reducing efficiency  
- Revenue-profit mismatch across divisions  
- Margin instability over time  

This system provides structured analytical visibility into these risks.

---

## Key Features

### Interactive Filtering
- Date range selection  
- Division multi-select  
- Minimum gross margin threshold  
- Product search  
- Dynamic real-time metric recalculation  

### KPI Monitoring
- Total Sales  
- Gross Profit  
- Gross Margin (%)  
- Profit per Unit  
- Record Count  

### Product-Level Intelligence
- Top products by gross profit  
- Margin efficiency ranking  
- Revenue vs profit comparison  
- Contribution analysis  

### Pareto Concentration Modeling
- Cumulative profit percentage curve  
- 80% threshold visualization  
- Dependency risk detection  

### Margin Volatility Analysis
- Monthly average margin trend  
- Stability diagnostics  
- Operational risk signaling  

### Data Export
- Download filtered data as CSV  

---

## Analytical Insights

- A small subset of products generates the majority of total profit  
- Several high-revenue products operate at inefficient margins  
- Profit generation is structurally concentrated  
- Division-level financial imbalance exists  
- Margin volatility indicates operational instability  

---

## Strategic Recommendations

- Reprice high-volume, low-margin SKUs  
- Optimize supplier contracts for cost-heavy products  
- Diversify profit contribution sources  
- Implement margin threshold monitoring  
- Track volatility as an early-warning system  

---

## Tech Stack

- Python  
- Pandas  
- Plotly  
- Streamlit  
- Financial Metric Engineering  
- Exploratory Data Analysis  

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
│   └── Profitability_Intelligence_Journal_Paper.pdf
│
├── requirements.txt
└── README.md
```

---

## Run Locally

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

## Citation

If referencing this work in academic or professional contexts:

Nikhil Singh (2025). *Profitability Intelligence and Margin Risk Modeling for Product Portfolio Optimization in Distribution-Based Enterprises*. Zenodo. https://doi.org/10.5281/zenodo.18729616

---

## Conclusion

This project demonstrates how profitability-focused analytics can provide deeper strategic insight than revenue analysis alone.

By integrating metric engineering, Pareto modeling, volatility analysis, and interactive visualization, the system establishes a structured framework for data-driven portfolio optimization.

It bridges business intelligence with AI-oriented financial reasoning and scalable analytics deployment.

---

## Author

Nikhil Kumar Singh  
BCA (Artificial Intelligence & Machine Learning)  
Aspiring AI & Software Engineer | Machine Learning | Data Analytics  

GitHub: https://github.com/nikhilsingh-k  
LinkedIn: https://www.linkedin.com/in/nikhilsingh-k/
