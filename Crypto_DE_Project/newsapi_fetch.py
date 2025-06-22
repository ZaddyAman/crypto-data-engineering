from newsapi import *
from textblob import TextBlob
import os

# Load API key (store in .env or replace directly)
api_key = 'ccdff7c3145c4ae68da5d2a36371e43f'  # Replace with your key or use os.getenv('API_KEY') with .env
newsapi = NewsApiClient(api_key)

# Define top 10 coins
coins = ['Bitcoin', 'Ethereum', 'Tether', 'XRP', 'BNB', 'Solana', 'USDC', 'Dogecoin', 'TRON', 'Cardano']
coin_symbols = ['BTC', 'ETH', 'USDT', 'XRP', 'BNB', 'SOL', 'USDC', 'DOGE', 'TRX', 'ADA']
query = ' OR '.join(coins) + ' OR ' + ' OR '.join(coin_symbols) + ' OR crypto'

# Fetch news
try:
    headlines = newsapi.get_everything(q=query, language='en', page_size=10)
    with open('crypto_news_data.txt', 'w', encoding='utf-8') as f:
        for article in headlines['articles']:
            title = article['title']
            description = article['description'] or 'No description'
            # Optional sentiment analysis
            sentiment = TextBlob(description).sentiment.polarity
            sentiment_label = 'positive' if sentiment > 0 else 'negative' if sentiment < 0 else 'neutral'
            f.write(f"Title: {title}\nDescription: {description}\nSentiment: {sentiment_label} (Polarity: {sentiment})\n\n")
            print(f"Title: {title}\nDescription: {description}\nSentiment: {sentiment_label}\n")
except Exception as e:
    print(f"Error fetching news: {e}")