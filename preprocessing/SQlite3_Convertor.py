import sqlite3
import pandas as pd

# Connect to the SQLite database
connection = sqlite3.connect('Market-Data-Preprocessing\Previous-Api-Version\DataBase\SQlite\data')
cursor = connection.cursor()

# Fetch table names
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
table_names = [table[0] for table in cursor.fetchall()]

# Print table names
for table_name in table_names:
    print(table_name)

# Read data into a DataFrame
query = f"SELECT * FROM {table_names[0]}"
df = pd.read_sql_query(query, connection)

# Export DataFrame to CSV
output_path = 'Market-Data-Preprocessing\Previous-Api-Version\DataBase\CSV\data.csv'
df.to_csv(output_path, index=False)

# Close the database connection
connection.close()
