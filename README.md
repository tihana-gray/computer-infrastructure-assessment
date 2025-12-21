# Computer Infrastructure Assessment


## 🧮 Problem 1: Data from yfinance

This project uses the `yfinance` library to download hourly stock data for the last five days for the five FAANG companies:

- Facebook (META)
- Apple (AAPL)
- Amazon (AMZN)
- Netflix (NFLX)
- Google (GOOG)

The data is saved as a .csv file inside a `data` folder in the project directory.<br>
Each file is named using a timestamp format:<br>
`YYYYMMDD_HHmmss.csv` (e.g. `20251022_221515.csv`), ensuring a unique filename every time the script runs.


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


## 🧮 Problem 2: Plotting Data

This part of the project uses the latest CSV file created in **Problem 1** to plot the Close prices for the five FAANG companies on a single line chart.

The script looks inside the data folder, finds the most recently modified `.csv` file (e.g. `20251129_141725.csv`), loads it with pandas, and selects only the Close prices for each stock.

The resulting plot is saved as a `.png` file inside a plots folder in the project directory. If the plots folder does not exist, it is created automatically. The timestamp from the CSV filename is reused to name the plot.

### Tools and Libaries:

Same as for Problem 1, including also `matplotlib` which creates a plot and saves it as an image.

### What the script does:

- Lists all files inside the data folder using `os.listdir()`.
- Filters this list so that only `.csv` files are kept.
- Builds full paths to each `CSV` file and picks the most recently modified one using `os.path.getmtime()`.
- Loads the chosen `CSV` into a pandas DataFrame with MultiIndex columns.
- Uses pandas indexing to select only the `Close` prices for all FAANG tickers.
- Flattens the column structure so the DataFrame columns become just the ticker symbols (META, AAPL, AMZN, NFLX, GOOG).
- Plots each ticker’s `Close` price over time on the same graph using matplotlib.
- Adds a title, axis labels, a legend, and a grid to make the plot easier to read.
- Checks if a `plots` folder exists, and creates it if it doesn’t.
- Saves the final plot as `png`  file inside the `plots` folder.


## 🧮 Problem 3: Script

The `faang.py` script was designed to function as a standalone executable file by incorporating a shebang line at the top of the script. What it does:
- Downloads FAANG stock data.
- Saves a timestamped CSV file.
- Generates a matching timestamped PNG plot.
- Prints confirmation messages to the terminal.

The script directly reuses the `get_data()` and `plot_data()` functions developed in Problems 1 and 2. 

The conditional statement `if __name__ == "__main__":` was added to control execution flow. It ensures that the data download and plotting processes are only triggered when the script is executed directly and not when it is imported into another Python file. 


## 🧮 Problem 4: Automation

The final part of this project automates the execution of the `faang.py` script using GitHub Actions.

This automation is implemented through a GitHub Actions workflow defined in a YAML file named `faang.yml`, which is stored in the required directory:<br>
`.github/workflows/faang.yml`

### Workflow purpose and schedule

The workflow is configured to run every Saturday morning at 09:00 Irish time using a cron schedule.<br>
When the workflow runs, it performs the following tasks automatically:<br>
- Executes the `faang.py`script.
- Downloads the latest FAANG stock data.
- Saves a new timestamped CSV file to the data folder.
- Generates a matching timestamped PNG plot in the plots folder.
- Commits and pushes created files back to the repository.

This ensures that the repository always contains an up-to-date weekly snapshot of FAANG stock data and visualisations.

### Environment and dependencies

The workflow runs on `ubuntu-latest`Linux virtual machine and default GitHub setting. Since each run starts from a clean environment, Python and required third-party libraries must be installed as part of the workflow.

Python is set up using `actions/setup-python@v5`. The workflow also installs libraries required by `faang.py`:<br>
- yfinance
- pandas
- matplotlib
- numpy<br>
Standard library modules such as `os` and `datetime` do not require installation. This approach also avoids sync problems in virtual environement.

### Commit and push automation

After `faang.py` finishes executing, the workflow automatically stages any newly created or updated files in the data and plots folders. If changes are detected, they are committed using a GitHub Actions and pushed back to the repository.

This completes the automation loop: data is collected, processed, visualised, and stored without any manual steps.

### 📚 Tools references:
- https://finance.yahoo.com/news/faang-stocks-161056487.html
- https://pandas.pydata.org/
- https://docs.python.org/3/library/os.html
- https://docs.python.org/3/library/datetime.html
- https://matplotlib.org/stable/tutorials/introductory/pyplot.html
- https://numpy.org/devdocs/index.html
- https://docs.github.com/en/actions
- https://crontab.guru/#0_9_*_*_6
- https://pip.pypa.io/en/stable/cli/pip_install

➡️ **Full list of references under tasks in [problems.ipynb](https://github.com/tihana-gray/computer-infrastructure-assessment/blob/main/problems.ipynb)**