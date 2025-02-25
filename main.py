from flask import Flask, jsonify
import os
import requests

app = Flask(__name__)

# Retrieve API keys from environment variables (set these later on Render)
ALPHA_VANTAGE_API_KEY = os.environ.get("ALPHA_VANTAGE_API_KEY")
FINNHUB_API_KEY = os.environ.get("FINNHUB_API_KEY")
FMP_API_KEY = os.environ.get("FMP_API_KEY")

@app.route("/")
def home():
    return "Market Tracker Backend is Running!"

@app.route("/api/market-data")
def market_data():
    # Example: Fetch daily market data for SPY from Alpha Vantage
    symbol = "SPY"
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={ALPHA_VANTAGE_API_KEY}"
    response = requests.get(url)
    data = response.json()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
