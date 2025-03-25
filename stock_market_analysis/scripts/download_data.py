#Import Yahoo Finance for data download
import yfinance as yf

# Set date range
start_date = "2013-01-01"
end_date = "2025-12-22"

# Define tickers and output filenames
tickers = {
    "^GSPC": "sp500_data.csv",
    "^VIX": "vix_data.csv",
    "AAPL": "aapl_data.csv",
    "NVDA": "nvda_data.csv",
    "MSFT": "msft_data.csv",
    "AMZN": "amzn_data.csv",
    "GOOGL": "googl_data.csv",
    "GC=F": "gold_data.csv",       # Gold Futures
    "CL=F": "crude_oil_data.csv"   # Crude Oil WTI Futures
}

# Download and save each one
for ticker, filename in tickers.items():
    print(f"Downloading {ticker}...")
    df = yf.download(ticker, start=start_date, end=end_date)
    df.to_csv(f"../data/{filename}")
    print(f"Saved to data/{filename}")
