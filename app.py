import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration
st.set_page_config(page_title="NGX Alpha Tracker", layout="wide")

# 2. Header & Research Context
st.title("📈 NGX Alpha Tracker: Elite 20")
st.markdown(f"""
**Market Date:** April 27, 2026 | **ASI:** 225,724.33 | **Status:** 45.05% YTD Rally
*Developed by Bamidele Adedeji (Independent Researcher)*
""")

# 3. Data Loading (Using your verified April 27 Snapshot)
@st.cache_data
def load_data():
    data = {
        'Ticker': ['ARADEL', 'DANGCEM', 'MTNN', 'UBA', 'ZENITHBANK', 'WAPCO', 'FIRSTHOLDCO', 'PRESCO'],
        'Price': [1679.90, 909.00, 820.00, 49.50, 135.90, 294.90, 67.50, 2100.00],
        'Change_%': [0.00, 2.13, 0.07, -10.00, 1.42, 7.24, -10.00, 6.06]
    }
    df = pd.DataFrame(data)
    
    # Sector Mapping Logic
    sectors = {
        'ARADEL': 'Energy', 'DANGCEM': 'Industrial', 
        'MTNN': 'Telecom', 'UBA': 'Banking', 
        'ZENITHBANK': 'Banking', 'WAPCO': 'Industrial', 
        'FIRSTHOLDCO': 'Banking', 'PRESCO': 'Agriculture'
    }
    df['Sector'] = df['Ticker'].map(sectors)
    return df

df = load_data()

# 4. Top Metrics Bar
col1, col2, col3 = st.columns(3)
col1.metric("Top Gainer", "WAPCO", "+7.24%")
col2.metric("Market Anchor", "ARADEL", "₦1,679.90")
col3.metric("Banking Sentiment", "Correction", "-10.00%", delta_color="inverse")

st.divider()

# 5. Visualization: Performance by Ticker
st.subheader("Individual Stock Performance")
fig_tickers = px.bar(
    df, 
    x='Ticker', 
    y='Change_%', 
    color='Change_%',
    color_continuous_scale=['red', 'yellow', 'green'],
    title="Daily Percentage Change (NGX Elite 20)",
    labels={'Change_%': 'Day Change (%)'}
)
st.plotly_chart(fig_tickers, use_container_width=True)

# 6. Two-Column Analysis
left_col, right_col = st.columns(2)

with left_col:
    st.subheader("Sectoral Heat")
    avg_sector = df.groupby('Sector')['Change_%'].mean().reset_index()
    fig_sector = px.pie(
        avg_sector, 
        values=avg_sector['Change_%'].clip(lower=0.1), # Ensures negative sectors still show in legend
        names='Sector', 
        hole=0.4,
        title="Market Weight by Sector Activity"
    )
    st.plotly_chart(fig_sector, use_container_width=True)

with right_col:
    st.subheader("Verified Price List")
    st.dataframe(df.sort_values(by='Change_%', ascending=False), use_container_width=True)

# 7. Research Conclusion
st.info("""
**Researcher's Note:** Today's data confirms a 'Sector Rotation.' While the Banking sector is 
experiencing a natural correction after record dividends, the Industrial and Agriculture sectors 
continue to drive real-economy growth.
""")
