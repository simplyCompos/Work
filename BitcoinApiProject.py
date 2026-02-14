from flask import Flask, jsonify, request
from datetime import datetime, timedelta
import random

app = Flask(__name__)

currencies = ["BTC", "ETH", "USD"]
data = []

base_prices = {"BTC": 24000, "ETH": 1600, "USD": 27}

for i in range(30, -1, -1):
    day = datetime.now() - timedelta(days=i)
    entry = {"date": day.strftime("%Y-%m-%d")}
    for cur in currencies:
        change = random.uniform(-0.02, 0.02)  
        base_prices[cur] *= (1 + change)
        entry[cur] = round(base_prices[cur], 2)
    data.append(entry)

@app.route("/")
def index():
    return jsonify(status="ok", message="Crypto Price API is running")

@app.route("/prices", methods=["GET"])
def get_prices():
    period_days = request.args.get("days", default=30)
    try:
        days = int(period_days)
        cutoff_date = datetime.now() - timedelta(days=days)
        filtered = [entry for entry in data if datetime.strptime(entry["date"], "%Y-%m-%d") >= cutoff_date]
        return jsonify(status="ok", data=filtered, message=f"Last {days} days")
    except ValueError:
        return jsonify(status="error", message="Invalid days value"), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
