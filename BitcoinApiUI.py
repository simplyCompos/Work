import tkinter as tk
from tkinter import ttk
import requests
from datetime import datetime
import matplotlib.pyplot as plt

def load_data():
    coins = coins_entry.get()
    days = days_entry.get()
    currency = currency_var.get()

    url = f"http://127.0.0.1:5000/prices?coins={coins}&days={days}&currency={currency}"

    try:
        response = requests.get(url)
        data = response.json()["data"]

        for row in tree.get_children():
            tree.delete(row)

        for coin, prices in data.items():
            if prices == "error" or not prices:
                continue

            seen_dates = set()

            for p in prices:
                date = datetime.fromtimestamp(p["time"]/1000).strftime("%Y-%m-%d")

                if date in seen_dates:
                    continue

                seen_dates.add(date)

                price = round(p["price"], 2)

                tree.insert("", "end", values=(coin, date, price, currency.upper()))

    except Exception as e:
        print(e)

def show_chart():
    coins = coins_entry.get()
    days = days_entry.get()
    currency = currency_var.get()

    url = f"http://127.0.0.1:5000/prices?coins={coins}&days={days}&currency={currency}"

    try:
        response = requests.get(url)
        data = response.json()["data"]

        plt.figure()  

        for coin, prices in data.items():
            dates = []
            values = []
            seen_dates = set()

            for p in prices:
                date = datetime.fromtimestamp(p["time"]/1000).strftime("%Y-%m-%d")

                if date in seen_dates:
                    continue

                seen_dates.add(date)

                dates.append(date)
                values.append(p["price"])

            plt.plot(dates, values, label=coin)

        plt.xticks(rotation=45)
        plt.title("Crypto Prices")
        plt.xlabel("Date")
        plt.ylabel(f"Price ({currency.upper()})")
        plt.legend()
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(e)

root = tk.Tk()
root.title("Crypto Viewer")
root.geometry("500x400")

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Coins:").grid(row=0, column=0)
coins_entry = tk.Entry(frame)
coins_entry.insert(0, "bitcoin,ethereum")
coins_entry.grid(row=0, column=1)

tk.Label(frame, text="Days:").grid(row=1, column=0)
days_entry = tk.Entry(frame)
days_entry.insert(0, "30")
days_entry.grid(row=1, column=1)

tk.Label(frame, text="Currency:").grid(row=2, column=0)
currency_var = tk.StringVar(value="usd")

currency_menu = ttk.Combobox(frame, textvariable=currency_var)
currency_menu["values"] = ("usd", "eur", "uah")
currency_menu.grid(row=2, column=1)

tk.Button(root, text="Load Data", command=load_data).pack(pady=10)

tk.Button(root, text="Show Chart", command=show_chart).pack(pady=5)

columns = ("Coin", "Date", "Price", "Currency")
tree = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)

tree.pack(fill="both", expand=True)

root.mainloop()
