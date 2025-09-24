#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
finance_dashboard_pipeline.py

This script synthesizes the key lessons from the Python for Finance lectures:
- Download financial and macroeconomic data (yfinance + FRED)
- Save and reload data from CSV files
- Handle missing values correctly (forward fill, no interpolation)
- Compute arithmetic returns
- Compute cumulative compounded returns (growth indexes)
- Plot and save charts
- Write modular code (each function does one thing only)

Author: Alexandre Landi (Skema Business School)
Academic Year 2025/26 — Fall 2025
"""

# -----------------------------
# Imports
# -----------------------------
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import pandas_datareader.data as dr

# -----------------------------
# Functions
# -----------------------------

def download_yfinance_close(ticker, start, end):
    """
    Download adjusted close prices from Yahoo Finance.
    Returns a DataFrame with Date as index and one column (the ticker).
    """
    raw_data = yf.download(
        ticker,
        start=start,
        end=end,
        progress=False,
        auto_adjust=False  # explicitly choose adjusted or raw prices
    )
    price_data = raw_data[["Close"]].rename(columns={"Close": ticker})
    return price_data



def save_csv(dataframe, filename):
    """Save a DataFrame to CSV in the current folder."""
    dataframe.to_csv(filename)


def load_csv(filename):
    """Load a CSV into a DataFrame (date index)."""
    dataframe = pd.read_csv(filename, index_col=0, parse_dates=True)
    return dataframe


def download_fred(series, start=None):
    """Download one or several series from FRED (macro data)."""
    fred_data = dr.DataReader(series, data_source="fred", start=start_date)
    return fred_data


def forward_fill_only(dataframe):
    """Forward fill missing values (no interpolation)."""
    cleaned_data = dataframe.ffill()
    return cleaned_data


def drop_leading_nas(dataframe):
    """Drop any remaining missing values at the start of the series."""
    cleaned_data = dataframe.dropna()
    return cleaned_data


def pct_change(dataframe):
    """Compute arithmetic returns: (P_t / P_{t-1}) - 1."""
    arithmetic_returns = dataframe.pct_change()
    return arithmetic_returns


def compound_from_arithmetic(arithmetic_returns):
    """From arithmetic returns to cumulative compounded growth index."""
    cumulative_returns = (1 + arithmetic_returns).cumprod()
    return cumulative_returns


def plot_series(dataframe, title, ylabel, filename):
    """
    Generic plot function.
    Saves figure as PNG in the current folder.
    """
    fig, ax = plt.subplots(figsize=(10, 5))  # create a fresh figure
    dataframe.plot(ax=ax)                    # plot into this figure
    ax.set_title(title)
    ax.set_ylabel(ylabel)
    ax.set_xlabel("Date")
    ax.legend()
    fig.tight_layout()
    fig.savefig(filename)
    plt.close(fig)  # close to avoid overlapping plots

# -----------------------------
# Main workflow
# -----------------------------


# -------------------------
# 1. Download macro data (CPI, GDP) from FRED
# -------------------------

start_date = "2000-01-01"
end_date = "2025-09-09"

fred_series = ["CPIAUCNS", "GDP"]
macroeconomic_data = download_fred(fred_series, start=start_date)
save_csv(macroeconomic_data, "macro.csv")

# Clean missing values
macroeconomic_data = forward_fill_only(macroeconomic_data)
macroeconomic_data = drop_leading_nas(macroeconomic_data)

# Compute returns
macroeconomic_returns = pct_change(macroeconomic_data)

# Compute cumulative growth
macro_cumulative_returns = compound_from_arithmetic(macroeconomic_returns)

# Plot
plot_series(
    macro_cumulative_returns,
    "Cumulative Growth of CPI and GDP",
    "Index",
    "macro_cum.png"
)

# -------------------------
# 2. Download financial assets from Yahoo
# -------------------------
tickers_and_files = {
    "SPY": "SPY.csv",     # Equities (S&P 500 ETF)
    "TLT": "TLT.csv",     # Bonds (US Treasuries ETF)
    "GC=F": "Gold.csv",   # Gold futures
    "CL=F": "Crude.csv",  # Crude Oil futures
    "ZW=F": "Wheat.csv",  # Wheat futures
    "DX=F": "USD.csv" # Dollar index
}



all_assets_cumulative = pd.DataFrame()

for ticker, filename in tickers_and_files.items():
    price_data = download_yfinance_close(ticker, start_date, end_date)
    save_csv(price_data, filename)

    price_data = forward_fill_only(price_data)
    # price_data = drop_leading_nas(price_data)

    # Compute cumulative arithmetic returns for each asset
    arithmetic_returns = pct_change(price_data)
    cumulative_returns = compound_from_arithmetic(arithmetic_returns)

    all_assets_cumulative[ticker] = cumulative_returns[ticker]

# -------------------------
# 3. Separate visualizations
# -------------------------

# Plot only macroeconomic indicators
plot_series(
    macro_cumulative_returns,
    "Cumulative Growth of CPI and GDP",
    "Cumulative Growth",
    "macro_only.png"
)

# Plot only financial assets
plot_series(
    all_assets_cumulative,
    "Cumulative Growth of Financial Assets",
    "Cumulative Growth",
    "assets_only.png"
)


print("Pipeline finished. Data and plots saved in the current folder.")
