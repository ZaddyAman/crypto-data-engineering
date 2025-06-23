![Alt text](Crypto_Project_Arch.gif)

# 🪙 Real-Time Crypto Analytics Platform

A full-stack real-time cryptocurrency analytics platform combining **data engineering**, **machine learning**, and **interactive dashboards** — featuring anomaly detection, time-series forecasting, and sentiment analysis.

![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-Production--Ready-blue)
![Stack](https://img.shields.io/badge/stack-Kafka%20%7C%20Spark%20%7C%20Airflow%20%7C%20PostgreSQL%20%7C%20Dash%20%7C%20Streamlit-blue)

---

## 🚀 Overview

This project ingests **live cryptocurrency data** from [CoinGecko](https://coingecko.com) and [Alternative.me (Fear & Greed Index)](https://alternative.me/crypto/fear-and-greed-index/), performs real-time ETL, applies ML models for anomaly detection and forecasting, and visualizes insights in a beautiful dashboard using **Dash** and **Streamlit**.

> 🔁 Built for end-to-end data flow: `Kafka → Spark → PostgreSQL → Airflow → ML → Dash`

---

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


