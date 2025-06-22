from kafka import KafkaProducer
import requests
import json
import time
from time import sleep
from time import sleep, ctime  # <- Make sure ctime is imported

print("✅ Kafka Producer started at", ctime())  # <- This logs when it starts

# Kafka producer config
producer = KafkaProducer(
    bootstrap_servers=["😂😂😂😂😂:9092'],
    value_serializer=lambda x: json.dumps(x).encode('utf-8'),
    key_serializer=lambda k: k.encode('utf-8')
)

# CoinGecko API endpoint
coins = ['bitcoin', 'ethereum', 'tether', 'binancecoin', 'solana', 'ripple', 'usd-coin', 'cardano', 'avalanche-2', 'dogecoin']
topic = 'crypto-prices'

def fetch_and_produce():
    url = f'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids={",".join(coins)}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        for coin in data:
            producer.send(topic, key=coin['id'], value=coin)
        producer.flush()
        print(f"Sent {len(data)} messages")
    except requests.RequestException as e:
        print(f'Error fetching CoinGecko data: {e}')
    time.sleep(1.2)

while True:
    fetch_and_produce()
    time.sleep(60)
