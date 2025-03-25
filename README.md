# Project-3---Team-5
# Post-Inauguration Stock Market Trends

## Project Overview

This project explores how key market indicators and tech stocks responded during the first two months following U.S. presidential inaugurations in **2013**, **2017**, **2021**, and **2025**. Using interactive visualizations, users can compare performance across presidencies and asset classes, including:

- **S&P 500**
- **VIX (Volatility Index)**
- **Gold**
- **Crude Oil**
- **Major Tech Stocks**: AAPL, AMZN, MSFT, NVDA, GOOGL

The goal is to provide a clear, visual perspective on short-term market behavior during political transitions.

---

## Tools & Technologies

- **Python**
- **Pandas** — data manipulation
- **SQLite** — local database storage
- **Seaborn & Matplotlib** — data visualization
- **IPyWidgets** — interactive dropdowns for user input
- **Jupyter Notebook** — interface for analysis and visuals

---

## Project Features

- 📈 **Line charts** comparing 2-month post-inauguration trends by president  
- 📊 **Bar charts** showing percentage change in each asset  
- 🔥 **Heatmaps** for side-by-side tech stock comparison  
- 🔄 **Interactive dropdown menu** to toggle between visual types  

---

## Data Source

Historical financial data was downloaded using the **Yahoo Finance API** via the `yfinance` Python library.

- Tickers include:  
  - `^GSPC` (S&P 500), `^VIX` (VIX), `GC=F` (Gold), `CL=F` (Crude Oil)  
  - `AAPL`, `AMZN`, `MSFT`, `NVDA`, `GOOGL` (tech stocks)

Two custom scripts were used for data handling:

- `download_data.py` — Downloads CSV files for each ticker using `yfinance`
- `load_to_sqlite.py` — Loads the cleaned CSVs into a local SQLite database (`market_data.db`)

---

## How It Works

1. The script reads daily close prices from the database.
2. For each presidential term, it extracts data from **Jan 20 to Mar 20** of that year.
3. Percent changes are calculated and stored for summary visuals.
4. The user selects a chart type via dropdown, and the appropriate plot is displayed.

---

## Visualization Examples

- **S&P 500 Line Chart**: Tracks the 60-day performance post-inauguration.  
- **Tech Stock Bar Charts**: Displays 2-month % changes by president for each stock.  
- **Heatmap**: Quickly shows winners and losers across all tech stocks.  

---

## Getting Started

### Requirements

- Python 3.x
- Jupyter Notebook
- Required libraries:

```bash
pip install pandas matplotlib seaborn ipywidgets yfinance
```

### Run the Notebook

1. Run `download_data.py` to fetch the latest data.
2. Run `load_to_sqlite.py` to populate `market_data.db`.
3. Open the notebook in Jupyter.
4. Run all cells.
5. Use the dropdown to explore different visualizations.

---

## Future Improvements

- Add more historical presidents or expand the analysis window.
- Include economic indicators (GDP, unemployment, etc.).
- Add export options for the charts.
- Have selected charts replace the current one.

---

## Author

Created by **Liaman Aghayeva**, **Lindsey Davies**, **Willa Grimes**, and **Isaac Ofori** as part of a data visualization project for the Columbia Engineering Data Analytics Boot Camp.
