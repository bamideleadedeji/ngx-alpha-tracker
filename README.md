# Nigeria Wealth Intelligence Suite 

## Overview
The **Nigeria Wealth Intelligence Suite** is a unified data analytics platform designed to monitor and compare performance across two critical asset classes in the Nigerian financial landscape: **Direct Equities (NGX Elite 20)** and **Managed Mutual Funds**.

Developed during the historic **April 2026 market surge**, this suite provides real-time insights into capital rotation, risk assessment, and yield gaps, specifically supporting research into the **Debt-Growth Nexus** in frontier markets.

##  Integrated Features
### 1. NGX Alpha Tracker (Equities)
- **Elite 20 Focus:** Real-time tracking of the "Heavyweights" (Aradel, Dangote Cement, MTN, etc.) that drive the All-Share Index.
- **Volatility Monitoring:** Automated tracking of "Lower Circuit" events (e.g., the -10% Banking correction of April 27, 2026).
- **Sector Analysis:** Categorization of performance across Energy, Industrial, Banking, and Agricultural sectors.

### 2. Mutual Fund ROI Tracker (Managed Funds)
- **Comparative Yields:** Tracking ROI across Money Market, Ethical/Shari’ah, and Equity-Based funds.
- **Risk-Reward Mapping:** Visualizing the relationship between fund categories and annual returns.
- **Benchmark Analysis:** Comparing fund performance against the soaring NGX All-Share Index (225k+ points).

##  The Tech Stack
- **Engine:** Python 3.11+
- **Data Handling:** Pandas, NumPy
- **Scraping:** BeautifulSoup4 (BS4), Requests
- **Visualization:** Plotly Express (Interactive Charts)
- **Deployment:** Streamlit Cloud

##  Market Context: April 27, 2026
This project captured a pivotal moment in the Nigerian economy:
* **The "Great Rotation":** Capital moved out of the Banking sector (UBA/FBNH -10%) following the recapitalization cycle and into Industrial leaders (**WAPCO +7.24%**).
* **Managed Stability:** While direct equities showed high volatility, Money Market Mutual Funds maintained a stable **14.5% ROI**, providing a "safe haven" for capital.

##  Repository Structure
```text
ngx-wealth-intelligence/
├── app.py              # The Unified Streamlit Application
├── requirements.txt    # Standard Library & External Dependencies
├── data/               # Verified Market Snapshots (CSV)
├── notebooks/          # R&D for Scrapers & ROI Logic
└── README.md           # Project Documentation
