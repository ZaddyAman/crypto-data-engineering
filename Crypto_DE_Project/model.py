import requests
import pandas as pd
import numpy as np
from datetime import datetime
from sklearn.ensemble import IsolationForest
from sqlalchemy import create_engine
import joblib

# -------------------------------
# 1. Config
# -------------------------------
from urllib.parse import quote_plus
PG_HOST = "13.203.79.75"
PG_PORT = 5432
PG_DB = "crypto"
PG_USER = "postgres"
PG_PASS = quote_plus("Aman@2003")  # ✅ encode special chars

engine = create_engine(f"postgresql://{PG_USER}:{PG_PASS}@{PG_HOST}:{PG_PORT}/{PG_DB}")



# -------------------------------
# 2. Fetch Historical Data
# -------------------------------
def fetch_coin_data(coin_id, days=15):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
    params = {"vs_currency": "usd", "days": days}

    print(f"🔄 Fetching data for {coin_id}...")
    response = requests.get(url, params=params)

    if response.status_code != 200:
        print(f"❌ Error {response.status_code} for {coin_id}: {response.text}")
        return pd.DataFrame()

    data = response.json()
    if not all(k in data for k in ['prices', 'market_caps', 'total_volumes']):
        print(f"❌ Missing keys in data: {list(data.keys())}")
        return pd.DataFrame()

    df = pd.DataFrame({
        "timestamp": [datetime.fromtimestamp(x[0] / 1000) for x in data['prices']],
        "avg_price": [x[1] for x in data['prices']],
        "avg_market_cap": [x[1] for x in data['market_caps']],
        "avg_volume": [x[1] for x in data['total_volumes']]
    })

    df["avg_24h_price_change_pct"] = df["avg_price"].pct_change(periods=24) * 100
    df.fillna(method="bfill", inplace=True)
    print(f"✅ {coin_id} data shape: {df.shape}")
    return df


# -------------------------------
# 3. Train Isolation Forest
# -------------------------------
def train_model(df):
    features = ["avg_price", "avg_market_cap", "avg_volume", "avg_24h_price_change_pct"]
    model = IsolationForest(n_estimators=100, contamination=0.03, random_state=42)
    model.fit(df[features])
    df["anomaly"] = model.predict(df[features])
    df["anomaly_label"] = df["anomaly"].map({1: "Normal", -1: "Anomaly"})
    return model, df


# -------------------------------
# 4. Save Model & Insert to DB
# -------------------------------
def save_model(model, coin_id):
    filename = f"{coin_id}_anomaly_model.pkl"
    joblib.dump(model, filename)
    print(f"💾 Model saved: {filename}")


def store_to_postgres(df, coin_id):
    table = f"{coin_id}_anomalies"
    print(f"📥 Inserting into anomaly.{table}...")
    df.to_sql(name=table, schema="anomaly", con=engine, if_exists="replace", index=False)
    print("✅ Data inserted successfully.")


# -------------------------------
# 5. Main Routine
# -------------------------------
if __name__ == "__main__":
    coin_list = ["bitcoin", "ethereum", "tether", "bnb", "solana"]

    for coin in coin_list:
        df = fetch_coin_data(coin, days=15)
        if df.empty:
            print(f"⚠️ Skipping {coin} — no data.")
            continue

        model, df = train_model(df)
        save_model(model, coin)
        store_to_postgres(df, coin)

    print("🎉 All coins processed.")
