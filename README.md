# Product Line Profitability & Margin Performance Analysis  
### Nassau Candy Distributor

## 📌 Project Overview
Sales volume alone does not guarantee profitability. Many products generate high revenue while delivering low margins, increasing operational risk and weakening overall business performance.

This project analyzes product-level and division-level profitability for **Nassau Candy Distributor** to identify:
- True profit-driving products
- High-revenue but low-margin risks
- Margin efficiency across divisions
- Profit concentration and dependency risks

The analysis transforms raw sales data into actionable financial intelligence to support pricing, sourcing, and product portfolio decisions.

---

## 🎯 Business Objectives
- Identify products with the highest gross profit and margins  
- Detect high-sales but low-margin products  
- Compare revenue vs profit performance across divisions  
- Analyze profit concentration using Pareto (80/20) principle  
- Flag margin-risk and loss-making products  

---

## 📂 Dataset Description
The dataset contains order-level sales and cost data with key attributes including:
- Product Name & Division
- Sales, Cost, Gross Profit
- Units sold
- Geographic and shipping details

Loss-making records were intentionally retained to identify margin risk products.

---

## 🧮 Key Metrics Used
- **Gross Margin (%)** = Gross Profit ÷ Sales  
- **Profit per Unit** = Gross Profit ÷ Units  
- **Revenue Contribution (%)**  
- **Profit Contribution (%)**  
- **Division-level Average Margin**

---

## 📊 Analysis Workflow
1. **Data Overview & Validation**
   - Dataset structure and missing value checks
2. **Data Cleaning**
   - Removed zero-sales and invalid unit records
   - Standardized division labels
3. **Profitability Metrics**
   - Product-level and division-level calculations
4. **Visual & Pareto Analysis**
   - Top profit products
   - High-sales vs low-margin risk analysis
   - Revenue vs profit imbalance
5. **Executive Insights & Recommendations**
   - Strategic business conclusions

---

## 📈 Streamlit Dashboard
An interactive dashboard was built using **Streamlit** to allow:
- Division-level filtering
- Margin threshold selection
- Product profitability exploration
- KPI monitoring

### To run the dashboard locally:
'''bash
pip install -r requirements.txt
streamlit run app/app.py

---

## 🧠 Key Insights
- A small percentage of products contribute the majority of total profit, indicating profit concentration risk.
- Several high-revenue products operate at low margins, requiring pricing or cost optimization.
- Certain divisions generate strong sales but underperform in profit contribution.
- Loss-making products were identified for immediate review.

---

## 💡 Strategic Recommendations
- Reprice high-sales, low-margin products to improve unit economics.
- Renegotiate manufacturing or sourcing costs for margin-poor products.
- Review consistently loss-making products for discontinuation.
- Reduce dependency on a limited number of profit-driving products.

---

## 🛠 Tools & Technologies
- Python  
- Pandas  
- Matplotlib  
- Streamlit  
- GitHub  

---

## 📌 Conclusion
This project demonstrates how profitability-focused analytics enables data-driven decision-making beyond surface-level sales metrics. The insights support sustainable growth through margin optimization and risk mitigation.
