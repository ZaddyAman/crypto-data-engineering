# 🪙 Real-Time Crypto Analytics Platform

A full-stack real-time cryptocurrency analytics platform combining **data engineering**, **machine learning**, and **interactive dashboards** — featuring anomaly detection, time-series forecasting, and sentiment analysis.


---

## 🚀 Overview

This project ingests **live cryptocurrency data** from [CoinGecko](https://coingecko.com) and [Alternative.me (Fear & Greed Index)](https://alternative.me/crypto/fear-and-greed-index/), performs real-time ETL, applies ML models for anomaly detection and forecasting, and visualizes insights in a beautiful dashboard using **Dash** and **Streamlit**.

> 🔁 Built for end-to-end data flow: `Kafka → Spark → PostgreSQL → Airflow → ML → Dash`

---

## 🏗️ Architecture


+-------------+        +--------+         +------------------------+
| CoinGecko   | -----> | Kafka  | ----->  | Spark Streaming (Bronze Layer) |
+-------------+        +--------+         +------------------------+
                                                 |
                                                 v
                                  +----------------------------+
                                  | PostgreSQL (Bronze Layer)  |
                                  +----------------------------+
                                                 |
                                                 v
          +----------------+         +-----------------------------+
          | Airflow DAGs   |<------->| ETL Job: Bronze ➜ Silver     |
          +----------------+         +-----------------------------+
                                                 |
                                                 v
                                  +----------------------------+
                                  | PostgreSQL (Silver Layer)  |
                                  +----------------------------+
                                        |              |
                                        |              v
                                        |      +-----------------------------+
                                        |      | Forecasting (Prophet)       |
                                        |      | ➜ silver_crypto.forecast_price|
                                        |      +-----------------------------+
                                        |
                                        v
                        +------------------------------+
                        | Anomaly Detection (IsoForest)|
                        | ➜ anomaly.<coin>_anomalies    |
                        +------------------------------+

                                        |
                       +----------------+------------------+
                       |                                 |
                       v                                 v
       +-----------------------------+     +------------------------------+
       | Dash Dashboard (Forecast,   |     | Streamlit Dashboard (KPIs,   |
       | Anomalies, Sentiment 📈)    |     | Comparisons, Heatmaps 📊)     |
       +-----------------------------+     +------------------------------+

                                  🔁 Sentiment Analysis (Fear & Greed API)
                                  ➜ Stored in sentiment_crypto.fear_greed_index







---

## 🔧 Tech Stack

| Layer          | Technologies Used                                      |
|----------------|--------------------------------------------------------|
| **Ingestion**   | Kafka, Python Kafka Producer, CoinGecko API            |
| **ETL**         | Apache Spark Structured Streaming, PySpark             |
| **Database**    | PostgreSQL (Bronze, Silver, Anomaly, Sentiment Layers) |
| **ML Models**   | Isolation Forest, Prophet (Forecasting), LOF (Planned) |
| **Scheduler**   | Apache Airflow                                         |
| **Dashboard**   | Dash (Plotly), Streamlit                               |
| **Infra**       | AWS EC2, Docker (Planned), systemd                     |

---

## 📊 Features

✅ Real-time crypto price streaming from CoinGecko  
✅ Spark Streaming-based ETL to PostgreSQL  
✅ Anomaly detection using Isolation Forest  
✅ Time-series price forecasting using Prophet  
✅ Sentiment analysis via Fear & Greed Index API  
✅ Interactive Dash dashboard with:
- 📈 Price & anomaly overlay
- 🔮 Forecast prediction
- 🌙 Dark mode
- 📥 CSV download
- 🎭 Date range picker  
✅ Streamlit version available with heatmaps and autorefresh

---

---

## 📈 ML Capabilities

### 🔍 Anomaly Detection

- **Model**: Isolation Forest (`scikit-learn`)
- **Input Features**:
  - `avg_price`
  - `avg_volume`
  - `market_cap`
  - `24h price change %`
- **Labeling**: Normal (1), Anomaly (-1)
- **Storage**: Stored in `anomaly.<coin>_anomalies`

> 📌 Supports expansion to LOF or One-Class SVM

### 📉 Forecasting

- **Model**: [Facebook Prophet](https://facebook.github.io/prophet/)
- **Predicted Feature**: Future `avg_price`
- **Visuals**:
  - Forecast line with 95% confidence bounds
- **Storage**: `silver_crypto.forecast_price`

---

## 😱 Sentiment Analysis

- Source: [Alternative.me Crypto Fear & Greed Index](https://alternative.me/crypto/fear-and-greed-index/)
- API: `https://api.alternative.me/fng/`
- Stored to: `sentiment_crypto.fear_greed_index`
- Dashboard Integration: Dual Y-axis chart (price + sentiment)

---

## 📺 Dash UI Highlights

- 🌙 **Dark Mode** toggle  
- 🔮 **Show Forecast** toggle  
- 📉 Price + anomaly markers  
- 📤 Export CSV  
- 📅 Date filtering  
- 📊 Fear & Greed sentiment overlay  
- 🪙 Logo-rich dropdown with 5 top coins (BTC, ETH, USDT, XRP, SOL)

---

## 🛠️ Setup Instructions

### 1. Clone and Create Virtual Env

```bash
git clone https://github.com/your-username/crypto-analytics-platform.git
cd crypto-analytics-platform
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt


2. Set Up PostgreSQL
Create DB crypto and schemas:

bronze_crypto

silver_crypto

anomaly

sentiment_crypto

3. Start Kafka, Spark, and Run Producers

# Start Kafka
bin/zookeeper-server-start.sh config/zookeeper.properties
bin/kafka-server-start.sh config/server.properties

# Start producer
python kafka_producer/producer.py

# Submit Spark ETL
spark-submit bronze_etl_job/spark_bronze_etl.py
