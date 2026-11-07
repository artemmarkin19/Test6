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

