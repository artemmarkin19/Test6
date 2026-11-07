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

