import requests

def GetUsdToUahRate():
    url1 = "https://api.monobank.ua/bank/currency"
    response = requests.get(url1)

    if response.status_code == 200:
        data = response.json()
        for item in data:
            if item["currencyCodeA"] == 840 and item["currencyCodeB"] ==980:
                rate_buy = item.get("rateBuy", item.get("rate"))
                rate_sell = item.get("rateSell", item.get("rate"))
                return rate_buy, rate_sell
    return None, None

buy, sell = GetUsdToUahRate()

if buy and sell:
    print(f"Rate USD to UAH\nBuy: {buy}\nSell: {sell}")
else:
    print("Failed to get dollar rate")
