from flask import Flask, jsonify
import requests

app = Flask(name)

@app.route("/")
def home():
    return jsonify(status="ok", message="Crypto API working")

@app.route("/prices")
def prices():
    url = "https://api.coingecko.com/api/v3/simple/price"

    params = {
        "ids": "bitcoin,ethereum",
        "vs_currencies": "usd"
    }

    response = requests.get(url)

    if response.status_code != 200:
        return jsonify(status="error", message="API error"), 500

    data = response.json()

    return jsonify(
        status="ok",
        data=data
    )

if name == "main":
    print("Running API...")
    app.run(debug=True)
