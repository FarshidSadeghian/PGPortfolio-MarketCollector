# Market Data Preprocessing

This project focuses on converting an SQLite3 dataset to a CSV file and making necessary changes to the cryptocurrency market data obtained from the previous Poloniex API. The SQLite database creation process can be found in the [Market-Data-Collector](https://github.com/FarshidSadeghian/Market-Data-Collector) repository.

## SQLite to CSV Converter

This Python script connects to an SQLite database, retrieves table names, and exports the data from the first table to a CSV file.
The exported CSV file will be saved in the specified location. Feel free to customize the script based on your specific needs.

## Coin Data Processor

This Python script processes a CSV file containing cryptocurrency data, separating and saving individual coin data into separate files. It also sorts the data by date and coin, removing unnecessary columns.


### Usage

1. **Run the SQLite3_Convertor:** Ensure you have placed the original SQLite3 database file in the `DataBase` directory.

2. **Run the CSV_Convertor:** After the SQLite3 conversion, execute this script to process the CSV file. Ensure the original CSV file (`data.csv`) is in the `DataBase` directory.

3. Individual coin data will be saved in the `DataBase/individual_coin_data` directory.

4. The sorted data will be saved in the file `sorted_data.csv`.


### File Structure

- `DataBase/`
  - `data`: Original SQLite3 database containing data for all coins.
  - `data.csv`: Converted CSV file of the entire cryptocurrency dataset.
  - `individual_coin_data/`: Directory for storing individual coin data files.
  - `sorted_data.csv`: Sorted CSV file for the entire cryptocurrency dataset.


### Requirements
- Python 3.x
- pandas library

Feel free to customize the scripts or provide feedback! If you're interested in the SQLite database creation process, refer to the [Market-Data-Collector](https://github.com/FarshidSadeghian/Market-Data-Collector) repository.
