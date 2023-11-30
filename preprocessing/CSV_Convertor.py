# Import necessary libraries
import pandas as pd
import os

# Load the original CSV file
csv_path = 'Market-Data-Preprocessing\Previous-Api-Version\DataBase\CSV\data.csv'
df = pd.read_csv(csv_path)

# Get unique coin names from the 'coin' column
unique_coins = df['coin'].unique()

# ----------------------------------------------------------------------------------------------------------------- #
#                                     Create Sorted CSV for Nueral Net Training                                     #
# ----------------------------------------------------------------------------------------------------------------- #

# Sort the DataFrame based on 'date' and 'coin' columns
sorted_df = df.sort_values(by=['date', 'coin'])

# Drop unnecessary columns from the sorted DataFrame
sorted_df.drop(columns=['volume', 'quoteVolume', 'weightedAverage'], inplace=True)

# Save the sorted DataFrame to a new CSV file
sorted_df.to_csv('Market-Data-Preprocessing\Previous-Api-Version\DataBase\CSV\sorted_data.csv', index=False)

# ----------------------------------------------------------------------------------------------------------------- #
#                                               Separate each Coin CSV                                              #
# ----------------------------------------------------------------------------------------------------------------- #

# Create a directory to save individual coin data files
output_dir = 'Market-Data-Preprocessing\Previous-Api-Version\DataBase\individual_coin_data'
os.makedirs(output_dir, exist_ok=True)

# Separate and save data for each coin
for coin in unique_coins:
    coin_data = df[df['coin'] == coin]
    coin_csv_file = f'{output_dir}/{coin}.csv'
    coin_data.to_csv(coin_csv_file, index=False)

    # Print coin name and the corresponding data length
    print(f"Coin Name: {coin}, Number of TimeStamps: {len(coin_data)}")