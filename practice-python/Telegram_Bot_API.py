import os
import requests
import time
from dotenv import load_dotenv
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

def get_updates(offset=None):
    params = {"timeout" : 100, "offset": offset}
    response = requests.get(f"{URL}/getUpdates", params=params)
    return response.json()
def send_message_with_reply_keyboard(chat_id):
    keyboard = {
            "keyboard": [
                [{"text": "USD Rate"}]
                [{"text": "Help"}]
            "resize_keyboard":True,
            "one_time_keyboard": False
                ]
            }
    payload = {
            "chat_id": chat_id,
            "text": "Pick action",
            "reply_markup": keyboard
            }
    requests.post(f"{URL}/sendMessage", json=payload)
def send_message(chat_id, text):
    payload = {"chat_id": chat_id, "text": text}
    requests.post(f"{URL}/sendMessage", data=payload)
def get_usd_to_uah_rate():
    response = requests.get("https://api.monobank.ua/bank/currency")
    if response.status_code == 200:
        for item in response.json():
            if item["currencyCodeA"] == 840 and item ["currencyCodeB"] == 980:
                rate_buy = item.get("rateBuy", item.get("rate"))
                rate_sell = item.get("rateSell", item.get("rate"))
                return f"Rate USD to UAH:\nBuy: {rate_buy}\nSell: {rate_sell}"
    return "Not able to get USD rate."
def main():
    print("Bot activated. Awaiting orders....")
    offset = None
    while True:
        updates = get_updates(offset)
        if "result" in updates:
            for update in updates["result"]:
                offset = update["update_id"] + 1
                if "message" in update:
                    message = update["message"]
                    chat_id = update["message"]["chat"]["id"]
                    text = message.get("text", "").lower()
                    if text in ["/start", "start", "hello"]:
                        send_message_with_reply_keyboard(chat_id)
                    elif text.lower() in ["rate", "usd", "usd rate"]:
                        reply = get_usd_to_uah_rate()
                        send_message(chat_id, reply)
                elif text.lower() in ["Help" "help"]:
                        send_message(chat_id, "Write 'Rate', to get USD rate")
        time.sleep(1)

if __name__ == "__main__":
    main()
