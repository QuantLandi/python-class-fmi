# Cross-Asset Market Regime Dashboard (Work in Progress)

## 📌 Overview
This project is part of the **Python Programming for Finance** course in the MSc Financial Markets & Investments program at **Skema Business School**.  
It is a **work in progress** toward building a full **Cross-Asset Market Regime Monitor**, as specified in the [project brief](dashboard_project.pdf).

The current stage (`finance_dashboard_pipeline.py`) focuses on **data collection, preprocessing, and basic visualization** of macroeconomic indicators and financial assets. The end goal is to deliver an interactive **Streamlit dashboard** for traders and portfolio managers.

---

## 🎯 Purpose
The final dashboard will:
- Visualize the performance of major asset classes across different **market regimes**.
- Include indicators for **growth, inflation, volatility, and yields**.
- Provide insights into **term structures** and **bond yield curves**.

---

## 👥 Target Audience
- Traders and portfolio managers who need a **concise overview** of cross-asset performance.
- Students and researchers interested in building **financial dashboards** with Python.

---

## 📊 Current Features
- **Data Collection**  
  - Macroeconomic data (CPI, GDP) from **FRED**  
  - Asset data (Equities, Bonds, Commodities, Dollar) from **Yahoo Finance**

- **Preprocessing**  
  - Save data to CSV (for resilience if APIs are unavailable)  
  - Handle missing values with **forward fill**  
  - Compute **arithmetic returns** and **cumulative compounded growth**  

- **Visualization**  
  - Line charts of cumulative growth for macroeconomic indicators  
  - Line charts of cumulative growth for financial assets  

---

## 📈 Planned Features (Work in Progress)
According to the specification:
- **Term structures** of futures (equity, gold, crude oil, wheat, dollar)
- **Yield curves** for US and German bonds
- **Heatmaps** comparing performance metrics across regimes
- **Filters**:  
  - Time periods  
  - Asset classes  
  - Market regimes  

- **Deployment**  
  - Build full dashboard in **Streamlit**  
  - Embed on personal website  
  - Auto-update daily with fresh data  

---

## 🛠️ Technical Requirements
- **Python packages**:  
  `pandas`, `numpy`, `matplotlib`, `yfinance`, `pandas_datareader`, `streamlit` (planned)  
- **Update frequency**: Daily (planned)  
- **Deployment**: Hosted on a web server with Streamlit support (planned)  

---

## 🚧 Status
✅ Data pipeline (CSV handling, preprocessing, cumulative growth plots)  
🔄 Visualization refinements (separating macro vs asset charts)  
🔜 Streamlit dashboard with interactive filters  
🔜 Deployment and automation  


---

## 📢 Notes
This project is **not finished yet**. The current focus is on **data reliability and preprocessing**.  
Visualization and dashboard interactivity will be added in the next phase.

---
