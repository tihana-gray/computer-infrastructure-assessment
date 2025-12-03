# Computer Infrastructure Assessment


## Problem 1: Data from yfinance

This project uses the `yfinance` library to download hourly stock data for the last five days for the five FAANG companies:

- Facebook (META)
- Apple (AAPL)
- Amazon (AMZN)
- Netflix (NFLX)
- Google (GOOG)

The data is saved as a .csv file inside a `data` folder in the project directory.<br>
Each file is named using a timestamp format:<br>
YYYYMMDD_HHmmss.csv (e.g. 20251022_221515.csv), ensuring a unique filename every time the script runs.


### Tools and Libaries:

`yfinance` - downloads historical stock data from Yahoo Finance.<br>
`pandas` - manages and saves the downloaded data.<br>
`os` - manages folders and file paths.<br>
`datetime` - creates formatted timestamps for filenames.<br>


### What the Script Does:

1. Defines a list of FAANG stock tickers.
2. Downloads hourly data for the last five days using `yfinance`.
3. Displays the first few rows to confirm successful download.
4. Checks if a `data` folder exists (and prints a message if not).
5. Creates a timestamped filename in the required format.
6. Saves the dataset as a `.csv` file in the `data` folder.


### Timezone Handling:

Since FAANG companies trade in the U.S., Yahoo Finance provides timestamps in America/New_York time.<br>
To align with Irish local time, the script performs the following steps:
- Checks if the dataset includes timezone information.
- Localises the data to America/New_York (the stock exchange timezone).
- Converts the timestamps to my local timezone (Europe/Dublin).
- Verifies the conversion by printing the timezone.


### Learning Path:

This task helped me understand how to:
- Combine multiple Python libraries in one workflow.
- Automate data downloads and save them efficiently.
- Handle folders, file paths, and handle date formats + creating timestamps.
- Debug VS Code and GitHub sync issues with packages and environments.
- Work with timezones in pandas, including localising and converting between them.

Each run of the program creates a new, timestamped CSV of FAANG stock data.

### 📚 Tools references:
- https://finance.yahoo.com/news/faang-stocks-161056487.html
- https://pandas.pydata.org/
- https://docs.python.org/3/library/os.html
- https://docs.python.org/3/library/datetime.html

➡️ **Full list of references under tasks in [problems.ipynb](https://github.com/tihana-gray/computer-infrastructure-assessment/blob/main/problems.ipynb)**