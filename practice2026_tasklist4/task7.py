import requests
from datetime import datetime

URL = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
PARAMS = {
    "vs_currency": "usd",
    "days": 7,          
    "interval": "daily"
}

response = requests.get(URL, params=PARAMS)
data = response.json()

prices = data["prices"]

print("Bitcoin: 1 price per day (buy/sell simulation)\n")

for day in prices:
    timestamp = day[0] / 1000
    price = day[1]

    date = datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d")

    buy_price = round(price * 0.995, 2)   
    sell_price = round(price * 1.005, 2)  

    print(f"{date} | BUY: ${buy_price} | SELL: ${sell_price}")
