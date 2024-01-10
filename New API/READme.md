# Cryptocurrency Market Data Processing (New API)

This Python script interacts with the latest Poloniex API to retrieve and process cryptocurrency market data. The workflow includes:

- Fetching ticker24h information from the API.
- Cleaning and adjusting market volumes data.
- Calculating adjusted volumes based on specific criteria.
- Aggregating volumes data for a comprehensive overview.
- Displaying the top N volumes coins in the market.
- Retrieving features for specific coins.
- Fetching market chart data for analysis.
- Storing the processed data in CSV files for further analysis.


## Requirements

- Python 3.x
- pandas library
- requests library

Ensure you have installed the required libraries before running the script

## Directory Structure

- `New-Api-Version/`
  - `MarketVolume_Collector.ipynb`: Main Python Jupyter Notebook for processing market volumes data.
  - `DataBase/`
    - `Ticker24h/`: Directory for storing daily ticker data in CSV format.
    - `Volumes/`: Directory for storing aggregated volumes data in CSV format.

