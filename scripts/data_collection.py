import os
from pathlib import Path
import yfinance as yf

stocks = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA"]

data = yf.download(stocks, start="2018-01-01", end="2024-01-01")

close_prices = data["Close"]

# Determine a reliable output path relative to this script's location
output_dir = Path(__file__).parent.parent / "Data"
output_dir.mkdir(parents=True, exist_ok=True)
output_file = output_dir / "stock_data.csv"

close_prices.to_csv(output_file)

print(f"Data downloaded successfully and saved to {output_file}.")
