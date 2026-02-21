# **Nassau Candy Distributor – Profitability & Margin Dashboard**

An interactive Business Intelligence dashboard built using **Streamlit** to analyze product-level and division-level profitability.

This project transforms raw transactional order data into actionable financial insights focused on **gross margin performance, profit concentration, cost diagnostics, and financial efficiency**.

---

## **Project Objective**

High sales volume does not always translate to high profitability.  
This dashboard answers critical business questions:

- Which products truly drive gross profit?
- Are high-revenue products actually high-margin?
- Which divisions underperform financially?
- How concentrated is overall profit?
- Where do margin risks and pricing inefficiencies exist?

The goal is to enable **margin-focused, data-driven decision-making** instead of relying solely on revenue metrics.

---

## **Key Features**

### **Interactive Filters**
- Order date range selector  
- Division multi-select filter  
- Minimum gross margin threshold slider  
- Product name search  
- AND-based filtering logic  

---

### **KPI Overview**
- Total Sales  
- Gross Profit  
- Gross Margin (%)  
- Profit per Unit  
- Rows shown (filtered dataset size)  

---

### **Product Profitability Analysis**
- Top products by Gross Profit  
- Top products by Gross Margin %  
- Revenue Contribution %  
- Profit Contribution %  
- Profit per Unit  
- Expandable detailed product-level KPI table  

---

### **Division Performance Dashboard**
- Revenue vs Gross Profit comparison  
- Margin distribution by division  
- Cross-division profitability comparison  

---

### **Cost vs Margin Diagnostics**
- Cost vs Sales scatter plot (bubble size represents profit)  
- Identification of cost-heavy, low-margin products  
- Dynamic margin-risk flagging  

---

### **Profit Concentration (Pareto) Analysis**
- Profit contribution by product  
- Cumulative profit percentage curve  
- Dependency indicators:
  - % of profit from top 3 products  
  - % of profit from top 5 products  
  - % of profit from top 10 products  
  - Number of products generating approximately 80% of total profit  

---

### **Margin Volatility Analysis**
- Monthly average gross margin trend  
- Margin standard deviation over time  
- Identification of unstable pricing or cost patterns  

---

### **Data Export**
- Download filtered dataset as CSV  

---

## **Tech Stack**

- Python  
- Streamlit  
- Pandas  
- Plotly (Express and Graph Objects)  
- Data Visualization  
- Exploratory Data Analysis (EDA)  

---

## **Project Structure**

```
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
```

---

## **How to Run Locally**

Install dependencies:

```
pip install -r requirements.txt
```

Run the dashboard:

```
streamlit run app/app.py
```

The application will open in your browser at:

```
http://localhost:8501
```

---

## **Deployment**

This dashboard is deployed using **Streamlit Cloud** with GitHub integration, enabling real-time interaction and cloud-based access.

---

## **Business Insights Generated**

- A small subset of products contributes the majority of total profit  
- Some high-revenue products operate at low margins  
- Certain divisions show imbalance between revenue and profitability  
- Margin-risk products are dynamically identified  
- Profit concentration reveals dependency risks  
- Margin volatility highlights financial instability periods  

---

## **Strategic Recommendations**

- Reprice high-volume, low-margin products  
- Renegotiate manufacturing or sourcing costs  
- Review consistently loss-making products  
- Diversify profit sources to reduce dependency risk  
- Monitor margin volatility to stabilize financial performance  

---

## **Conclusion**

This project demonstrates how profitability-focused analytics enables smarter business decisions.

By transforming transactional order data into an interactive analytics dashboard, stakeholders gain visibility into margin performance, product efficiency, and structural financial risks.

The solution showcases end-to-end analytical capability, including:

- Data cleaning  
- KPI engineering  
- Aggregation  
- Visualization  
- Cloud deployment  

---

## **Author**

**Nikhil Singh**  
BCA (AI & ML) Student  
Machine Learning & Data Analytics Enthusiast  

GitHub: https://github.com/nikhilsingh-k  
LinkedIn: https://www.linkedin.com/in/nikhilsingh-k  
