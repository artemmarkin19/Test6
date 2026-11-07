import tkinter as tk
from tkinter import ttk, messagebox
import requests
from datetime import datetime

API = "https://api.coingecko.com/api/v3/simple/price"
COINS = {
    "bitcoin": "BTC",
    "ethereum": "ETH",
    "binancecoin": "BNB",
    "tether": "USDT",
    "ripple": "XRP",
    "cardano": "ADA",
    "dogecoin": "DOGE",
    "tron": "TRX",
    "hyperliquid": "HYPE",
    "matic-network": "MATIC",
}
COIN_NAMES = {
    "bitcoin": "Bitcoin",
    "ethereum": "Ethereum",
    "binancecoin": "Binance Coin",
    "tether": "Tether",
    "ripple": "XRP",
    "cardano": "Cardano",
    "dogecoin": "Dogecoin",
    "tron": "TRON",
    "hyperliquid": "Hyperliquid",
    "matic-network": "Polygon",
}

def fetch_prices():
    params = {
        "ids": ",".join(COINS.keys()),
        "vs_currencies": "usd",
    }
    try:
        resp = requests.get(API, params=params, timeout=10)
        resp.raise_for_status()
        return resp.json()
    except requests.exceptions.Timeout:
        messagebox.showerror("Ошибка сети", "Сервер CoinGecko не ответил вовремя.")
        return None
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Ошибка сети", f"Не удалось получить данные:\n{e}")
        return None
    except ValueError:
        messagebox.showerror("Ошибка данных", "API вернул некорректный JSON.")
        return None


def refresh_data():
    data = fetch_prices()
    if data is None:
        return
    for row in tree.get_children():
        tree.delete(row)
    for coin_id, symbol in COINS.items():
        coin_data = data.get(coin_id)
        if not coin_data:
            continue
        price = coin_data.get("usd")
        tree.insert(
            "", "end",
            values=(COIN_NAMES[coin_id], symbol, price),
        )
    now = datetime.now().strftime("%d-%m-%Y %S%H:%M:%H")
    status_label.config(text=f"Последнее обновление: {now}")


root = tk.Tk()
root.title("Курсы криптовалют к USD")
root.geometry("540x480")
root.minsize(480, 400)
top_frame = tk.Frame(root)
top_frame.pack(fill="x", padx=10, pady=(10, 5))
tk.Label(top_frame, text="Курсы криптовалют к USD",font=("Arial", 14, "bold")).pack(side="left")
btn_refresh = tk.Button(top_frame, text="Обновить", command=refresh_data,padx=12, pady=2)
btn_refresh.pack(side="right")
columns = ("name", "symbol", "price")
tree = ttk.Treeview(root, columns=columns, show="headings", height=12)
tree.heading("name", text="Название")
tree.heading("symbol", text="Сокращение")
tree.heading("price", text="Цена (USD)")
tree.column("name", width=200, anchor="w")
tree.column("symbol", width=80, anchor="center")
tree.column("price", width=150, anchor="e")
tree.pack(fill="both", expand=True, padx=10, pady=5)
status_label = tk.Label(root, text="Загрузка...", anchor="w", fg="gray")
status_label.pack(fill="x", padx=10, pady=(0, 10))
refresh_data()
root.mainloop()
