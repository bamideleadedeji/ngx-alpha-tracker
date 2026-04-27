# NGX Alpha Tracker: Elite 20 Portfolio Analysis## Overview
This project is a real-time data engine designed to track and analyze the "Heavyweight" companies on the **Nigerian Exchange (NGX)**. Developed during the historic **April 2026 market surge**—where the All-Share Index (ASI) crossed the **225,000-point milestone**—this tool provides a deep dive into sector rotation and capital allocation in the Nigerian economy.

As an independent researcher, I built this to bridge the gap between raw market data and actionable economic insights, specifically focusing on the **Debt-Growth Nexus** in Nigeria.

##  Key Features
- **Resilient Web Scraper:** Custom BeautifulSoup4 engine designed to handle live data-drift and structural shifts on financial portals.
- **Elite 20 Filtering:** Automatically isolates the "Power Players" (Dangote Cement, MTN, Aradel, etc.) from market noise.
- **Sector Analysis:** Categorizes stocks into Banking, Industrial, Energy, and Telecom to visualize capital movement.
- **Live Correction Handling:** Successfully tracked the "Banking Correction" of April 27, 2026, where major banks hit the -10% lower circuit following dividend peaks.

##  The Tech Stack
- **Language:** Python 3.11+
- **Libraries:** Pandas (Data Manipulation), BeautifulSoup4 (Web Scraping), Plotly (Interactive Visualization), Streamlit (Web Dashboard).
- **Environment:** Jupyter Notebooks for R&D; VS Code for deployment.

##  Market Context (April 27, 2026)
During the latest run of this tool, the following market dynamics were observed:
* **Industrial Leadership:** WAPCO and Dangote Cement led growth with gains of +7.24% and +2.13% respectively.
* **Banking Volatility:** Major pullbacks in UBA and FBNH (-10.00%) provided a case study in profit-taking efficiency.
* **Agri-Hedge:** Presco PLC emerged as a top gainer (+6.06%), signaling investor trust in the agricultural sector.

##  Project Structure
```text
ngx-alpha-tracker/
├── data/               # Verified CSV snapshots of the NGX
├── notebooks/          # R&D and data cleaning logic
├── src/                # Core scraping and validation scripts
├── app.py              # Streamlit dashboard entry point
└── requirements.txt    # Project dependencies
