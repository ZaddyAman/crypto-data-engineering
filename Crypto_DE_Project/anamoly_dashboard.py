import dash
from dash import html, dcc, Input, Output, State
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
import urllib.parse

# -------------------------
# 🔧 Database Configuration
# -------------------------
DB_USER = "postgres"
DB_PASS = urllib.parse.quote_plus("Aman@2003")
DB_HOST = "13.203.79.75"
DB_PORT = "5432"
DB_NAME = "crypto"
SCHEMA = "anomaly"
META_SCHEMA = "bronze_crypto"

# -------------------------
# ✅ Use Only These 5 Valid Coins
# -------------------------
COINS = ["bitcoin", "ethereum", "tether", "bnb", "solana"]

# -------------------------
# 🖼 Load Logos for These Coins Only
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
            "bnb": "bnb",
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

# ---------------------
# 🚀 Initialize the App
# ---------------------
app = dash.Dash(__name__)
app.title = "Crypto Anomaly Dashboard"

# -------------------
# 📥 Load Data Helper
# -------------------
def load_data(coin):
    if coin not in COINS:
        print(f"⚠️ Invalid coin: {coin}")
        return pd.DataFrame(columns=["timestamp", "avg_price", "anomaly_label"])

    engine = create_engine(f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
    query = f'SELECT * FROM {SCHEMA}."{coin}_anomalies"'
    try:
        df = pd.read_sql(query, con=engine)
        if df.empty:
            return pd.DataFrame(columns=["timestamp", "avg_price", "anomaly_label"])
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        return df
    except Exception as e:
        print(f"⚠️ Failed to load data for {coin}: {e}")
        return pd.DataFrame(columns=["timestamp", "avg_price", "anomaly_label"])

# -------------------
# 📊 Layout
# -------------------
app.layout = html.Div([
    html.H1("📈 Crypto Price Anomaly Dashboard"),

    html.Div([
        html.Label("Select Coin:"),
        dcc.Dropdown(
            id='coin-dropdown',
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

        html.Label("Select Date Range:"),
        dcc.DatePickerRange(
            id='date-picker',
            start_date_placeholder_text="Start Date",
            end_date_placeholder_text="End Date"
        ),
        html.Br(), html.Br(),

        html.Button("📥 Download CSV", id="download-btn"),
        dcc.Download(id="download-data")
    ], style={"width": "40%", "display": "inline-block", "verticalAlign": "top"}),

    html.Div([
        dcc.Graph(id="price-plot")
    ], style={"width": "100%"})
])

# ------------------
# 🔁 Callbacks
# ------------------
@app.callback(
    Output("price-plot", "figure"),
    Input("coin-dropdown", "value"),
    Input("date-picker", "start_date"),
    Input("date-picker", "end_date")
)
def update_plot(coin, start_date, end_date):
    df = load_data(coin)

    if df.empty:
        return px.line(title=f"No data available for {coin.title() if coin else 'Unknown'}")

    if start_date and end_date:
        df = df[(df["timestamp"] >= start_date) & (df["timestamp"] <= end_date)]

    fig = px.line(df, x="timestamp", y="avg_price", title=f"{coin.title()} Price Trend with Anomalies",
                  labels={"timestamp": "Time", "avg_price": "Avg Price (USD)"})

    anomalies = df[df["anomaly_label"] == "Anomaly"]

    if not anomalies.empty:
        fig.add_scatter(x=anomalies["timestamp"], y=anomalies["avg_price"],
                        mode="markers", name="🔴 Anomalies",
                        marker=dict(color="red", size=8, symbol="circle"))
    else:
        fig.add_annotation(
            text="🟨 No Anomalies Detected",
            xref="paper", yref="paper",
            x=0.5, y=0.9, showarrow=False,
            font=dict(size=14, color="orange"),
            bgcolor="rgba(255,255,255,0.7)", bordercolor="orange", borderwidth=1
        )

    fig.update_layout(template="plotly_white")
    return fig

@app.callback(
    Output("download-data", "data"),
    Input("download-btn", "n_clicks"),
    State("coin-dropdown", "value"),
    prevent_initial_call=True
)
def download_csv(n_clicks, coin):
    df = load_data(coin)
    return dcc.send_data_frame(df.to_csv, filename=f"{coin}_anomalies.csv", index=False)

# -------------------
# ▶️ Run App
# -------------------
if __name__ == "__main__":
    app.run(debug=True)
