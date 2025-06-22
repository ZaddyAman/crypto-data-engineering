import requests
import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine
from urllib.parse import quote_plus

# 🔧 PostgreSQL Config
user = "postgres"
password = quote_plus("Aman@2003")
host = "13.203.79.75"
port = "5432"
db = "crypto"

engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}")

# 🌐 Fetch Sentiment Data
url = "https://api.alternative.me/fng/?limit=1&format=json"
response = requests.get(url)
data = response.json()["data"][0]

# 🧾 Prepare Row
timestamp = datetime.fromtimestamp(int(data["timestamp"]))
value = int(data["value"])
classification = data["value_classification"]

df = pd.DataFrame([{
    "timestamp": timestamp,
    "value": value,
    "value_classification": classification
}])

# 📥 Insert into DB
df.to_sql("fear_greed_index", engine, schema="sentiment_crypto", if_exists="append", index=False)
print("✅ Sentiment data stored.")
