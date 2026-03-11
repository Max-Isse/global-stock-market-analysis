import yfinance as yf
import pandas as pd

stocks = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA"]

data = yf.download(stocks, start="2018-01-01", end="2024-01-01")

close_prices = data["Close"]

close_prices.to_csv("../data/stock_data.csv")

print("Data downloaded successfully.")