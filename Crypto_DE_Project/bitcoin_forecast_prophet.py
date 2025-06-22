# forecast_and_save.py
import pandas as pd
from prophet import Prophet
from sqlalchemy import create_engine
from urllib.parse import quote_plus
from datetime import datetime

def run_forecast(coin):
    user = "postgres"
    password = quote_plus("Aman@2003")
    host = "13.203.79.75"
    port = "5432"
    database = "crypto"
    engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}")

    query = f"SELECT timestamp, avg_price FROM anomaly.{coin}_anomalies ORDER BY timestamp"
    df = pd.read_sql(query, engine)
    if df.empty:
        print(f"⚠️ No data for {coin}")
        return

    df = df.rename(columns={"timestamp": "ds", "avg_price": "y"}).dropna()

    model = Prophet()
    model.fit(df)

    future = model.make_future_dataframe(periods=48, freq='H')
    forecast = model.predict(future)

    # Prepare forecast df
    forecast_out = forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]].copy()
    forecast_out["id"] = coin
    forecast_out["model_used"] = "Prophet"
    forecast_out.rename(columns={"ds": "forecast_time"}, inplace=True)

    # Save to DB
    forecast_out.to_sql("forecast_price", engine, schema="silver_crypto", if_exists="append", index=False)
    print(f"✅ Forecast saved for {coin}")

# Example run
if __name__ == "__main__":
    for coin in ["bitcoin", "ethereum", "tether", "solana", "xrp"]:
        run_forecast(coin)
