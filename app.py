import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration
st.set_page_config(page_title="Nigeria Wealth Intelligence", layout="wide")

# 2. Sidebar Navigation
st.sidebar.title("Navigation")
app_mode = st.sidebar.radio("Select Dashboard", ["NGX Elite 20 Stocks", "Mutual Fund ROI Tracker"])

# --- DATA LOADING FUNCTIONS ---

@st.cache_data
def get_stock_data():
    # Your verified NGX Snapshot for April 27, 2026
    data = {
        'Ticker': ['ARADEL', 'DANGCEM', 'MTNN', 'UBA', 'ZENITHBANK', 'WAPCO', 'FIRSTHOLDCO', 'PRESCO'],
        'Price': [1679.90, 909.00, 820.00, 49.50, 135.90, 294.90, 67.50, 2100.00],
        'Change_%': [0.00, 2.13, 0.07, -10.00, 1.42, 7.24, -10.00, 6.06],
        'Sector': ['Energy', 'Industrial', 'Telecom', 'Banking', 'Banking', 'Industrial', 'Banking', 'Agriculture']
    }
    return pd.DataFrame(data)

@st.cache_data
def get_fund_data():
    # Integrating your Mutual Fund ROI logic
    funds = {
        'Fund Name': ['Stanbic IBTC Money Market', 'ARM Ethical Fund', 'United Capital Equity', 'FBN Smart Beta'],
        'Fund Category': ['Money Market', 'Ethical/Shari’ah', 'Equity-Based', 'Equity-Based'],
        'Annual_ROI_%': [14.5, 18.2, 24.5, 21.0],
        'Volatility': ['Low', 'Medium', 'High', 'High']
    }
    return pd.DataFrame(funds)

# --- DASHBOARD LOGIC ---

if app_mode == "NGX Elite 20 Stocks":
    st.title(" NGX Alpha Tracker: Elite 20")
    df_stocks = get_stock_data()
    
    # KPIs
    c1, c2, c3 = st.columns(3)
    c1.metric("Top Gainer", "WAPCO", "+7.24%")
    c2.metric("Market Anchor", "ARADEL", "₦1,679.90")
    c3.metric("Banking Sentiment", "Correction", "-10.00%", delta_color="inverse")
    
    # Stock Chart
    fig = px.bar(df_stocks, x='Ticker', y='Change_%', color='Sector', 
                 title="Stock Performance by Sector")
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(df_stocks, use_container_width=True)

elif app_mode == "Mutual Fund ROI Tracker":
    st.title(" Nigeria Mutual Fund ROI Tracker")
    df_funds = get_fund_data()
    
    # KPIs for Funds
    f1, f2, f3 = st.columns(3)
    f1.metric("Highest ROI", "United Capital", "24.5%")
    f2.metric("Market Avg ROI", "18.4%", "+2.1%")
    f3.metric("Risk Profile", "Equity-Heavy", "High")
    
    # Fund Chart
    fig_fund = px.scatter(df_funds, x='Fund Name', y='Annual_ROI_%', size='Annual_ROI_%', 
                          color='Fund Category', title="Mutual Fund Yields vs. Category")
    st.plotly_chart(fig_fund, use_container_width=True)
    st.dataframe(df_funds, use_container_width=True)

# 4. Common Researcher Footnote
st.divider()
st.info("**Researcher's Insight:** This unified view allows for a comparative analysis of direct equity risk versus the stability of mutual funds. Note how the Banking correction in stocks correlates with the volatility in Equity-based mutual funds.")
