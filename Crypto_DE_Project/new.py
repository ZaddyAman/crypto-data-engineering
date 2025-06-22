import streamlit as st
import pandas as pd
import plotly.express as px
import psycopg2
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Load environment variables if needed
# load_dotenv()  # Uncomment if you're using a .env file

# Set page config
st.set_page_config(
    page_title="Crypto Dashboard",
    layout="wide",
    page_icon="💹"
)

# Title
st.title("💹 Real-Time Crypto Dashboard")

# DB Connection
@st.cache_resource
def get_connection():
    user = "postgres"
    password = "Aman@2003"
    host = "13.203.79.75"
    port = "5432"
    dbname = "crypto"
    return create_engine(f"postgresql://{user}:{password}@{host}:{port}/{dbname}")

engine = get_connection()

# Load Data
@st.cache_data(ttl=300)
def load_data():
    query = """
    SELECT 
        symbol,
        avg_price,
        avg_volume,
        avg_market_cap,
        avg_24h_price_change_pct,
        hour_start_time
    FROM silver_crypto.crypto_hourly_summary
    """
    df = pd.read_sql(query, engine)

    # Parse hour from timestamp
    if "hour_start_time" in df.columns:
        df["hour"] = pd.to_datetime(df["hour_start_time"]).dt.hour
    else:
        st.error("❌ 'hour_start_time' column missing from table.")
    
    return df

df = load_data()

# Show raw data
with st.expander("🔍 Show Raw Data"):
    st.dataframe(df)

# Clean and validate data
df["avg_price"] = pd.to_numeric(df["avg_price"], errors="coerce")
df["hour"] = pd.to_numeric(df["hour"], errors="coerce")
df = df.dropna(subset=["avg_price", "hour", "symbol"])

# Filter Options
symbols = df["symbol"].unique().tolist()
selected_symbols = st.multiselect("📌 Select Symbols", symbols, default=symbols)

filtered_df = df[df["symbol"].isin(selected_symbols)]

# Plot - Price Trend by Hour
st.markdown("### 📈 Hourly Avg Price per Symbol")

if not filtered_df.empty:
    fig_price = px.line(
        filtered_df,
        x="hour",
        y="avg_price",
        color="symbol",
        markers=True,
        title="Hourly Avg Price per Symbol"
    )
    fig_price.update_layout(
        xaxis_title="Hour of Day",
        yaxis_title="Avg Price",
        legend_title="Crypto Symbol",
        template="plotly_white"
    )
    st.plotly_chart(fig_price, use_container_width=True)
else:
    st.warning("⚠️ No data to display for selected symbols.")
