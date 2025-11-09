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


### Timezone Handling

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

### 📚 Full list of references:
- https://packaging.python.org/en/latest/tutorials/installing-packages/
- https://code.visualstudio.com/docs/python/environments
- https://code.visualstudio.com/docs/python/environments#_select-and-activate-an-environment
- https://pip.pypa.io/en/stable/cli/pip_install/
- https://pandas.pydata.org/
- https://docs.python.org/3/library/os.html
- https://docs.python.org/3/library/datetime.html
- https://stackoverflow.com/questions/15707532/import-datetime-v-s-from-datetime-import-datetime
- https://www.geeksforgeeks.org/python/python-datetime-module/
- https://docs.python.org/3/tutorial/controlflow.html#defining-functions  
- https://aroussi.com/post/python-yahoo-finance, 
- https://medium.com/@kasperjuunge/yfinance-10-ways-to-get-stock-data-with-python-6677f49e8282,
- https://www.youtube.com/watch?v=j0sBKAB75oc 
- https://www.ig.com/sg/trading-strategies/nasdaq-opening-and-closing-times--when-can-you-trade--230527
- https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.tz_localize.html
- https://pandas.pydata.org/docs/user_guide/timeseries.html#localizing-time-zones
- https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.tz_convert.html
- https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.tz.html
- https://stackoverflow.com/questions/16628819/convert-pandas-timezone-aware-datetimeindex-to-naive-timestamp-but-in-certain-t
- https://www.geeksforgeeks.org/pandas/pandas-series-dt-tz_localize/
- https://pandas.pydata.org/docs/user_guide/timeseries.html#time-zone-handling
- https://www.geeksforgeeks.org/python/difference-between-newline-and-carriage-return-in-python/
- https://docs.python.org/3/library/functions.html#print
- https://docs.python.org/3/library/os.path.html#os.path.isdir
- https://www.w3schools.com/python/python_conditions.asp
- https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html
- https://www.geeksforgeeks.org/python/python-os-path-isdir-method/
- https://www.geeksforgeeks.org/python/python-strftime-function/
- https://stackoverflow.com/questions/32490629/getting-todays-date-in-yyyy-mm-dd-in-python
- https://www.geeksforgeeks.org/python/convert-datetime-string-to-yyyy-mm-dd-hhmmss-format-in-python/
- https://docs.python.org/3/library/functions.html#func-str
- https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
- https://docs.python.org/3/library/datetime.html#datetime.datetime.now
- https://docs.python.org/3/library/datetime.html#datetime.date.strftime
- https://docs.python.org/3/tutorial/controlflow.html#defining-functions
- https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html
- https://docs.python.org/3/library/os.path.html#os.path.join
- https://docs.python.org/3/library/os.path.html#os