#Import Dependencies
import pandas as pd
import sqlite3
import os

# Define Paths
data_dir = "../data"
db_path = "../market_data.db"

# Connect to SQLite
conn = sqlite3.connect(db_path)

# File list
files = {
    "sp500_data.csv": "sp500",
    "vix_data.csv": "vix",
    "aapl_data.csv": "aapl",
    "nvda_data.csv": "nvda",
    "msft_data.csv": "msft",
    "amzn_data.csv": "amzn",
    "googl_data.csv": "googl",
    "gold_data.csv": "gold",
    "crude_oil_data.csv": "oil"
}

# Correct column names
column_names = ["date", "close", "high", "low", "open", "volume"]

for filename, table_name in files.items():
    file_path = os.path.join(data_dir, filename)
    print(f"\nLoading {filename} into table '{table_name}'...")

    try:
        # Skip first 3 rows, then assign correct headers
        df = pd.read_csv(file_path, skiprows=3, names=column_names)

        # Convert date column
        df["date"] = pd.to_datetime(df["date"], errors="coerce")
        df.dropna(subset=["date"], inplace=True)

        # Load to SQLite
        df.to_sql(table_name, conn, if_exists="replace", index=False)
        print(f"Loaded {len(df)} rows into '{table_name}'")

    except Exception as e:
        print(f"Failed to load {filename}: {e}")

conn.close()
print("\nAll data successfully loaded into market_data.db")
