import streamlit as st
st.set_page_config(page_title="Crypto Dashboard", layout="wide")  # 👈 MUST be first

# ⬇️ Now other imports and setup
from streamlit_autorefresh import st_autorefresh
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
from urllib.parse import quote_plus
import humanize
from datetime import datetime, timedelta

# ---------------------
# 🎛️ Sidebar Settings
# ---------------------
with st.sidebar:
    st.header("Filters")

    # Auto-refresh toggle and interval dropdown (in MINUTES)
    auto_refresh = st.checkbox("🔄 Enable Auto-Refresh", value=True)

    refresh_interval_label = st.selectbox(
        "⏱️ Refresh Interval",
        options=["15 min", "30 min", "60 min"],
        index=0 if auto_refresh else 1
    )
    interval_mapping = {
        "15 min": 15 * 60 * 1000,
        "30 min": 30 * 60 * 1000,
        "60 min": 60 * 60 * 1000,
    }
    refresh_interval = interval_mapping[refresh_interval_label]

    # Trigger auto-refresh if enabled
    if auto_refresh:
        st_autorefresh(interval=refresh_interval, key="crypto_dashboard_refresh")

    # Dark mode toggle
    dark_mode = st.checkbox("🌙 Dark Mode", value=True)

# ---------------------
# 🔧 Database Connection
# ---------------------
user = "postgres"
password = quote_plus("Aman@2003")  # <-- Replace with your password
host = "13.203.79.75"
port = "5432"
database = "crypto"

engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}")

# ---------------------
# 🔍 Coin Filters
# ---------------------
coins = pd.read_sql("SELECT DISTINCT id FROM silver_crypto.crypto_hourly_summary", engine)['id'].tolist()
coin_options = ["All"] + coins
selected_options = st.sidebar.multiselect("Select Coins", coin_options, default=["All"])

if "All" in selected_options:
    selected_coins = coins
else:
    selected_coins = selected_options

time_options = {
    "Last 24 hours": 1,
    "Last 3 days": 3,
    "Last 7 days": 7
}
selected_range = st.sidebar.selectbox("Time Range", list(time_options.keys()))
start_time = datetime.utcnow() - timedelta(days=time_options[selected_range])

# ---------------------
# 📥 Load Silver Table
# ---------------------
if selected_coins:
    placeholders = ','.join(['%s'] * len(selected_coins))
    query = f"""
    SELECT * FROM silver_crypto.crypto_hourly_summary
    WHERE id IN ({placeholders})
    AND hour_start >= %s
    ORDER BY hour_start DESC
    """
    df = pd.read_sql(query, engine, params=tuple(selected_coins + [start_time]))

    # ---------------------
    # 🖼️ Load Logos from Bronze Table
    # ---------------------
    logo_query = f"""
    SELECT DISTINCT ON (id) id, image
    FROM bronze_crypto.raw_crypto_prices
    WHERE id IN ({placeholders})
    """
    logo_df = pd.read_sql(logo_query, engine, params=tuple(selected_coins))

    # ---------------------
    # 🔗 Merge latest records for metrics
    # ---------------------
    latest_data = df.sort_values('hour_start').drop_duplicates('id', keep='last')
    latest_data = latest_data.merge(logo_df, on='id', how='left')

    # ---------------------
    # 🚀 Key Metrics Section
    # ---------------------
    st.title("📊 Real-Time Crypto Dashboard")
    st.subheader("📌 Key Metrics per Coin")
    col_count = 3
    cols = st.columns(col_count)

    for i, (_, row) in enumerate(latest_data.iterrows()):
        with cols[i % col_count]:
            st.markdown(f"""
            <div style="text-align: center;">
                <img src="{row['image']}" width="40">
                <h3>{row['name']}</h3>
                <p>💰 Avg Price: ${row['avg_price']:.2f}</p>
                <p>📈 24h Change: {row['price_change_percentage_24h']:.2f}%</p>
                <p>📊 Volume: {humanize.intword(row['volume'])}</p>
                <p>🏦 Market Cap: {humanize.intword(row['market_cap'])}</p>
            </div>
            """, unsafe_allow_html=True)

    # ---------------------
    # 📈 Line Charts
    # ---------------------
    st.subheader("📉 Price Trend")
    fig_price = px.line(df, x='hour_start', y='avg_price', color='id', title="Avg Price Over Time")
    st.plotly_chart(fig_price, use_container_width=True)

    st.subheader("📊 Volume Trend")
    fig_vol = px.line(df, x='hour_start', y='volume', color='id', title="Volume Over Time")
    st.plotly_chart(fig_vol, use_container_width=True)

    # ---------------------
    # 🔥 24h Price Change Heatmap
    # ---------------------
    st.subheader("🔥 24h Price Change Heatmap")
    heat_df = latest_data[['id', 'price_change_percentage_24h']]
    fig_heat = px.imshow([heat_df['price_change_percentage_24h'].tolist()],
                         labels=dict(x="Coin", color="24h % Change"),
                         x=heat_df['id'].tolist(),
                         y=["Change"],
                         color_continuous_scale="Inferno" if dark_mode else "RdYlGn")
    st.plotly_chart(fig_heat, use_container_width=True)

    # ---------------------
    # 🔍 Coin Comparator
    # ---------------------
    st.subheader("🔍 Coin Comparator")
    compare_coins = st.multiselect("Compare Coins", coins, default=coins[:2], key="compare")
    comp_df = df[df['id'].isin(compare_coins)]
    if not comp_df.empty:
        fig_comp = px.line(comp_df, x="hour_start", y="avg_price", color="id", title="Coin Price Comparison")
        st.plotly_chart(fig_comp, use_container_width=True)

    # ---------------------
    # 📤 CSV Download
    # ---------------------
    st.subheader("📁 Download Aggregated Data")
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download CSV", csv, "crypto_hourly_summary.csv", "text/csv")

else:
    st.warning("⚠️ Please select at least one coin to visualize the dashboard.")
