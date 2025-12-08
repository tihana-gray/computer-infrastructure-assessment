import yfinance as yf
import pandas as pd
import os
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

# Copying functions from problems.ipynb - Problem 1
def get_data():

    # The list of FAANG stock symbols
    faang = ['META', 'AAPL', 'AMZN', 'NFLX', 'GOOG']

    # Downloading the data from Yahoo Finance
    data = yf.download(tickers=faang, period='5d', interval='1h', group_by='ticker')
    
    print("Downloaded data sample:\n")
    print(data.head())
    
    print("Original timezone information:")
    print(data.index.tz)
    
    # Time conversion
    if data.index.tz is None:
        data = data.tz_localize('America/New_York')
    data = data.tz_convert('Europe/Dublin')
    
    print("Converted to timezone:", data.index.tz)