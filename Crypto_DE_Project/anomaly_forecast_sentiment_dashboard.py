import dash
from dash import html, dcc, Input, Output, State
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
import urllib.parse
import plotly.graph_objects as go

# -------------------------
# 🔧 Database Configuration
# -------------------------
DB_USER = "postgres"
DB_PASS = urllib.parse.quote_plus("🤪🤪🤪🤪🤪🤪")
DB_HOST = "🤪🤪🤪🤪🤪🤪"
DB_PORT = "5432"
DB_NAME = "crypto"
ANOMALY_SCHEMA = "anomaly"
META_SCHEMA = "bronze_crypto"
FORECAST_SCHEMA = "silver_crypto"
SENTIMENT_SCHEMA = "sentiment_crypto"


COINS = ["bitcoin", "ethereum", "tether", "xrp", "solana"]

# ✅ Load sentiment data
def load_sentiment_data():
    engine = create_engine(f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
    try:
        df = pd.read_sql(f"SELECT * FROM {SENTIMENT_SCHEMA}.fear_greed_index ORDER BY timestamp", engine)
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        return df
    except:
        return pd.DataFrame()

# -------------------------
# 🖼️ Load Logos
# -------------------------
def get_coin_logos():
    engine = create_engine(f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
    try:
        df = pd.read_sql(f"SELECT symbol, image FROM {META_SCHEMA}.coins_metadata", con=engine)
        df["symbol"] = df["symbol"].str.lower()
        logo_map = {}
        symbol_map = {
            "bitcoin": "btc",
            "ethereum": "eth",
            "tether": "usdt",
            "xrp": "xrp",
            "solana": "sol"
        }
        for coin in COINS:
            symbol = symbol_map[coin]
            if symbol in df["symbol"].values:
                logo_map[coin] = df.loc[df["symbol"] == symbol, "image"].values[0]
        return logo_map
    except Exception as e:
        print(f"⚠️ Failed to load coin logos: {e}")
        return {}

COIN_LOGOS = get_coin_logos()





# -------------------------
# 📥 Load Anomaly + Forecast
# -------------------------
def load_anomaly_data(coin):
    engine = create_engine(f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
    query = f'SELECT * FROM {ANOMALY_SCHEMA}."{coin}_anomalies"'
    try:
        df = pd.read_sql(query, con=engine)
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        return df
    except:
        return pd.DataFrame(columns=["timestamp", "avg_price", "anomaly_label"])

def load_forecast_data(coin):
    engine = create_engine(f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
    query = f"""
        SELECT forecast_time, yhat, yhat_lower, yhat_upper 
        FROM {FORECAST_SCHEMA}.forecast_price 
        WHERE id = %s ORDER BY forecast_time
    """
    try:
        df = pd.read_sql(query, con=engine, params=(coin,))
        df["forecast_time"] = pd.to_datetime(df["forecast_time"])
        return df
    except:
        return pd.DataFrame()
    


# -------------------------
# 🚀 Initialize App
# -------------------------
app = dash.Dash(__name__)
app.title = "Crypto Dashboard with Forecast"

# -------------------------
# 📊 Layout
# -------------------------
app.layout = html.Div([
    html.H1("📈 Crypto Anomaly & Forecast Dashboard"),

    html.Div([
        html.Label("Select Coin"),
        dcc.Dropdown(
            id="coin-dropdown",
            options=[
                {
                    "label": html.Span([
                        html.Img(src=COIN_LOGOS.get(coin, ""), height=20, style={"marginRight": "6px"}),
                        coin.title()
                    ], style={"display": "flex", "alignItems": "center"}),
                    "value": coin
                } for coin in COINS
            ],
            value=COINS[0],
            clearable=False
        ),
        html.Br(),

        html.Label("Select Date Range"),
        dcc.DatePickerRange(
            id="date-picker",
            start_date_placeholder_text="Start Date",
            end_date_placeholder_text="End Date"
        ),
        html.Br(),

        dcc.Checklist(
            id="dark-toggle",
            options=[{"label": "🌙 Dark Mode", "value": "dark"}],
            value=["dark"],
            inputStyle={"margin-right": "6px", "margin-left": "10px"}
        ),
        dcc.Checklist(
            id="forecast-toggle",
            options=[{"label": "🔮 Show Forecast", "value": "forecast"}],
            value=["forecast"],
            inputStyle={"margin-right": "6px", "margin-left": "10px"}
        ),
        dcc.Checklist(
            id="sentiment-toggle",
            options=[{"label": "📊 Show Sentiment", "value": "sentiment"}],
            value=["sentiment"],
            inputStyle={"margin-right": "6px", "margin-left": "10px"}
        ),
        html.Br(),

        html.Button("📥 Download CSV", id="download-btn"),
        dcc.Download(id="download-data")
    ], style={"width": "35%", "display": "inline-block", "verticalAlign": "top", "padding": "20px"}),

    html.Div([
        dcc.Graph(id="price-plot")
    ], style={"width": "100%", "padding": "20px"})
])

# -------------------------
# 🔁 Callbacks
# -------------------------
@app.callback(
    Output("price-plot", "figure"),
    Input("coin-dropdown", "value"),
    Input("date-picker", "start_date"),
    Input("date-picker", "end_date"),
    Input("dark-toggle", "value"),
    Input("forecast-toggle", "value"),
    Input("sentiment-toggle", "value")  # 👈 new input
)
def update_plot(coin, start_date, end_date, dark_mode, forecast_enabled, sentiment_enabled):
    df = load_anomaly_data(coin)
    forecast_df = load_forecast_data(coin)
    sentiment_df = load_sentiment_data()

    template = "plotly_dark" if "dark" in dark_mode else "plotly_white"

    if df.empty:
        return px.line(title="No data available", template=template)

    if start_date and end_date:
        df = df[(df["timestamp"] >= start_date) & (df["timestamp"] <= end_date)]
        sentiment_df = sentiment_df[(sentiment_df["timestamp"] >= start_date) & (sentiment_df["timestamp"] <= end_date)]

    fig = go.Figure()

    # 📈 Price Line
    fig.add_trace(go.Scatter(
        x=df["timestamp"], y=df["avg_price"],
        mode="lines", name="Avg Price",
        line=dict(color="dodgerblue")
    ))

    # 🔴 Anomalies
    anomalies = df[df["anomaly_label"] == "Anomaly"]
    if not anomalies.empty:
        fig.add_trace(go.Scatter(
            x=anomalies["timestamp"], y=anomalies["avg_price"],
            mode="markers", name="🔴 Anomalies",
            marker=dict(color="red", size=8)
        ))

    # 🔮 Forecast
    if "forecast" in forecast_enabled and not forecast_df.empty:
        fig.add_trace(go.Scatter(x=forecast_df["forecast_time"], y=forecast_df["yhat"],
                                 mode="lines", name="🔮 Forecast", line=dict(dash="dot", color="orange")))
        fig.add_trace(go.Scatter(x=forecast_df["forecast_time"], y=forecast_df["yhat_upper"],
                                 mode="lines", name="Upper Bound", line=dict(width=0.5, color="gray")))
        fig.add_trace(go.Scatter(x=forecast_df["forecast_time"], y=forecast_df["yhat_lower"],
                                 mode="lines", name="Lower Bound", line=dict(width=0.5, color="gray"),
                                 fill="tonexty", fillcolor="rgba(255,165,0,0.2)"))

    # 📊 Sentiment Overlay
    if "sentiment" in sentiment_enabled and not sentiment_df.empty:
        fig.add_trace(go.Scatter(
            x=sentiment_df["timestamp"], y=sentiment_df["value"],
            mode="lines+markers", name="📊 Sentiment (FGI)",
            yaxis="y2", marker=dict(color="green"),
            hovertemplate='Sentiment: %{y}<br>%{text}',
            text=sentiment_df["value_classification"]
        ))

    # 🎨 Layout
    fig.update_layout(
        title=f"{coin.title()} Dashboard: Price + Forecast + Sentiment",
        xaxis_title="Time",
        yaxis=dict(title="Avg Price (USD)", side="left"),
        yaxis2=dict(title="Fear & Greed Index", overlaying="y", side="right", showgrid=False),
        template=template,
        legend=dict(x=0.01, y=0.99),
        height=600
    )

    return fig


@app.callback(
    Output("download-data", "data"),
    Input("download-btn", "n_clicks"),
    State("coin-dropdown", "value"),
    prevent_initial_call=True
)
def download_csv(n_clicks, coin):
    df = load_anomaly_data(coin)
    return dcc.send_data_frame(df.to_csv, filename=f"{coin}_anomalies.csv", index=False)

# -------------------------
# ▶️ Run
# -------------------------
if __name__ == "__main__":
    app.run(debug=True)
