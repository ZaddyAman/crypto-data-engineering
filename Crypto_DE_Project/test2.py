import streamlit as st
import pandas as pd
import altair as alt
import psycopg2
from sqlalchemy import create_engine, text
from urllib.parse import quote_plus
import humanize
from datetime import datetime, timedelta

# -------------------- CONFIG --------------------
st.set_page_config(page_title="Crypto Dashboard", layout="wide")

DB_USER = "postgres"
DB_PASS = quote_plus("Aman@2003")  # update this
DB_HOST = "13.203.79.75"
DB_PORT = 5432
DB_NAME = "crypto"

engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

# -------------------- SIDEBAR FILTERS --------------------
st.sidebar.header("🔎 Filters")

# Fetch available coins
with engine.connect() as conn:
    coins_df = pd.read_sql("SELECT DISTINCT id FROM silver_crypto.crypto_hourly_summary", conn)
    coin_options = coins_df['id'].dropna().sort_values().tolist()

selected_coins = st.sidebar.multiselect("Select Coins", coin_options, default=coin_options[:3])

hours_range = st.sidebar.slider("Lookback Hours", 1, 72, 24)
start_time = datetime.utcnow() - timedelta(hours=hours_range)

# -------------------- LOAD DATA --------------------
if selected_coins:
    query = text("""
        SELECT * FROM silver_crypto.crypto_hourly_summary
        WHERE id IN :coin_ids
          AND hour_start >= :start_time
        ORDER BY hour_start DESC
    """)

    with engine.connect() as conn:
        df = pd.read_sql(query, conn, params={
            "coin_ids": tuple(selected_coins),
            "start_time": start_time
        })

    if df.empty:
        st.warning("No data available for selected filters.")
        st.stop()

    # -------------------- OVERVIEW CARDS --------------------
    st.subheader("📌 Overview Metrics")

    for coin in selected_coins:
        coin_df = df[df['id'] == coin].sort_values("hour_start", ascending=False)

        if not coin_df.empty:
            latest = coin_df.iloc[0]
            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                st.metric(label=f"{coin.title()} - Avg Price", value=f"${latest['avg_price']:.2f}")
            with col2:
                st.metric(label="Max Price", value=f"${latest['max_price']:.2f}")
            with col3:
                st.metric(label="Min Price", value=f"${latest['min_price']:.2f}")
            with col4:
                st.metric(label="Volume", value=humanize.intword(latest['volume'] or 0))
            with col5:
                st.metric(label="Market Cap", value=humanize.intword(latest['market_cap'] or 0))

    # -------------------- PRICE TREND CHART --------------------
    st.subheader("📈 Price Trend Over Time")
    price_chart = alt.Chart(df).mark_line().encode(
        x='hour_start:T',
        y='avg_price:Q',
        color='id:N',
        tooltip=['id', 'avg_price', 'hour_start']
    ).properties(height=400)
    st.altair_chart(price_chart, use_container_width=True)

else:
    st.info("Please select at least one coin to view data.")
