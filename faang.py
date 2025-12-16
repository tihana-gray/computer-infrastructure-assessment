#!/usr/bin/env python3

# https://realpython.com/python-shebang/
# https://www.geeksforgeeks.org/python/why-we-write-usr-bin-env-python-on-the-first-line-of-a-python-script/
# https://stackoverflow.com/questions/7670303/purpose-of-usr-bin-python3-shebang
# https://medium.com/cloud-for-everybody/i-kept-seeing-usr-bin-env-python3-and-finally-decided-to-figure-it-out-a3376a21316b


import yfinance as yf
import pandas as pd
import os
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

# Copying functions from problems.ipynb 

# Problem 1

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
    
     # Confirming that data folder exists
    folder_name = 'data'
    if not os.path.isdir(folder_name):
        print(f"Folder '{folder_name}' not found! Please create it manually.")
        return  
    else:
        print(f"Folder '{folder_name}' found. Proceeding to save the data.")
        
    # Timestamp & filename creation
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = str(timestamp) + ".csv"
    
    # Saving
    filepath = os.path.join(folder_name, filename)
    data.to_csv(filepath)

    
    # Problem 2
    
def plot_data():
    data_folder = "data"
    plot_folder = "plots"
        
    files = os.listdir(data_folder)  
    print("All files found:", files)
        
    csv_files = [f for f in files if ".csv" in f]  
    print("CSV files found:", csv_files)
        
    csv_paths = [os.path.join(data_folder, f) for f in csv_files] 
    latest_file = max(csv_paths, key=os.path.getmtime)
    
    # Extracting filename from full path
    csv_filename = os.path.basename(latest_file)
    # https://docs.python.org/3/library/os.path.html#os.path.basename
    
    # Removing .csv extension and replace with .png (saving png with the same name as csv)
    plot_filename = os.path.splitext(csv_filename)[0] + ".png"
    # https://docs.python.org/3/library/os.path.html#os.path.splitext
    
    print("Latest file picked:", latest_file)
        
    file_path = latest_file
    df = pd.read_csv(file_path, header=[0, 1], index_col=0)
    print(df.head())
        
    arrays = [ 
        ["META", "META", "AAPL", "AAPL", "AMZN", "AMZN", "NFLX", "NFLX", "GOOG", "GOOG"],
        ["Open", "Close", "Open", "Close", "Open", "Close", "Open", "Close", "Open", "Close"]
        ]
         
    tuples = list(zip(*arrays))
    index = pd.MultiIndex.from_tuples(tuples, names=["first", "second"])
        
    close_data = df.loc[:, (slice(None), 'Close')].copy()
    close_data.columns = close_data.columns.get_level_values(0)
        
    plt.figure(figsize=(12, 6))
    for ticker in close_data.columns:
        plt.plot(close_data.index, close_data[ticker], label=ticker)
            
    plt.xlabel("Date and Time (Irish Local Time)", fontsize=12)
    plt.ylabel("Stock Closing Price", fontsize=12)
    plt.legend(title="Ticker", loc="upper left")
    plt.xticks(rotation=45) # Rotating x-axis labels for better readability
    plt.grid(True)
        
    #Saving the plot
    if not os.path.isdir(plot_folder):
         os.makedirs(plot_folder)
    print(f"Created folder: {plot_folder}")
            
    # Saving the plot into plots folder
    plt.savefig(
        os.path.join(plot_folder, plot_filename),
        dpi=300,
        bbox_inches='tight'
    )
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html
    # https://docs.python.org/3/library/os.path.html#os.path.join
    
    plt.close()
        
    print(f"Plot saved successfully in '{plot_folder}' folder as 'faang_close_prices.png'.")
        
if __name__ == "__main__":
    # https://www.geeksforgeeks.org/python/what-does-the-if-__name__-__main__-do/
    # https://realpython.com/python-main-function/
    # https://docs.python.org/3/library/__main__.html
    # https://stackoverflow.com/questions/419163/what-does-if-name-main-do
    # https://realpython.com/python-main-function/
    get_data()
    plot_data()
    print("All saved successfully.")
