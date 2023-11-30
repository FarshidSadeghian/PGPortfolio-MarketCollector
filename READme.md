# Market Date

## File 1: poloniex.py

This Python script provides a class `Poloniex` that interacts with the Poloniex API to fetch various market-related data. Here's a brief overview of its functionality:

- **Poloniex Class**: This class represents the Poloniex API interface.
  
  - **Constructor**: Initializes the Poloniex object with API key and secret.
  
  - **Market Ticker**: Method `market_ticker()` retrieves market ticker data.
  
  - **Market Volume**: Method `market_volume()` fetches 24-hour trading volume data.
  
  - **Market Status**: Method `market_status()` gets information about currencies and their status in the market.
  
  - **Market Loans**: Method `market_loans(coin)` retrieves loan orders for a specific coin.
  
  - **Market Orders**: Method `market_orders(pair='all', depth=10)` fetches order book data for a specific currency pair.
  
  - **Market Chart**: Method `market_chart(pair, period=day, start=None, end=None)` gets historical market chart data for a specific currency pair within a given time period.
  
  - **Market Trade History**: Method `market_trade_hist(pair)` retrieves trade history for a specific currency pair.

  - **API Method**: Method `api(command, args=None)` is the internal method used to make API requests. It handles both public and private API calls.

## File 2: coin_list.py

This Python script defines a class `CoinList` used for managing a list of coins and their corresponding market data. Here's a summary of its functionality:

- **CoinList Class**: This class manages a list of coins and their data.

  - **Constructor**: Initializes the CoinList object. It fetches market volume and ticker data to compile a list of active coins.
  
  - **Active Coins**: Method `all_active_coins` returns a DataFrame containing active coins along with their volume and price data.
  
  - **All Coins**: Method `all_coins` retrieves a list of all available coins in the market.
  
  - **Top N Volume**: Method `top_n_volume(n=5, order=True, min_volume=0)` returns the top N coins by trading volume. It allows filtering by minimum volume.
  
  - **Chart Data**: Method `get_chart_until_success(pair, start, period, end)` fetches historical chart data for a specific currency pair until a successful connection is established.

## File 3: coin_data_manager.py

This Python script defines a class `CoinDataManager` responsible for managing and retrieving historical market data for a specified number of coins. Here's an overview of its functionality:

- **CoinDataManager Class**: This class manages historical market data for a specified number of coins.

  - **Constructor**: Initializes the CoinDataManager object with parameters such as the number of coins, time period, and data source (online/offline).
  
  - **Coins Selection**: Method `select_coins(start, end)` selects a specific number of coins based on trading volume within a given time period.
  
  - **Coin Features**: Method `get_coin_features(start, end, period=300, features=('close',))` retrieves features (e.g., close price, open price, volume) for selected coins within a specified time period.
  
  - **Data Filling**: Method `_fill_data(start, end, coin, cursor)` fills historical market data for a specific coin within a given time range.
  
  - **Data Initialization**: Method `_initialize_db()` initializes the database for storing historical market data.
  
  - **Data Update**: Method `_update_data(start, end, coin)` updates historical market data for a specific coin within a given time range.
  
  - **Data Retrieval**: Method `_fill_part_data(start, end, coin, cursor)` fetches and fills historical market data for a specific coin within a given time range.
  
  - **Data Validation**: Method `_check_period(period)` validates the specified time period.
  
  - **Data Manipulation**: Method `_fill_nan_and_invalid(array, bound=(0, 1), forward=True, axis=-1)` fills NaN values and invalid data in the input array.

  - **Helper Function**: Method `coin_data_manager_init_helper(config, online=True, download=False, db_directory=None)` initializes the CoinDataManager object with the provided configuration settings. It also allows downloading historical data if specified.

These scripts provide a comprehensive interface for interacting with the Poloniex API, managing coin data, and retrieving historical market features for analysis and trading strategies.