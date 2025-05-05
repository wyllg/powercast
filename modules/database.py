'''
Database Preprocessing

1. Cleaned up the CSV file before transferring to SQLite database
2. Removed Solar mWatts because of empty values
3. Created a table and transferred the data
4. Closed the connection
'''

import pandas as pd
import sqlite3

# Loading the Data File
df = pd.read_csv("data/electricity.csv")
df.info()

# Data Clean Up
df.columns = df.columns.str.strip()

# Delete Unwanted Column
df = df.drop(columns=["all solar thousand megawatthours"])

# Create/Connect to SQL Database
conn = sqlite3.connect("data/database.db")
cursor = conn.cursor()

# Load Data File to SQLite
df.to_sql('electricitydb', conn, if_exists='fail')

# Close the connection
conn.close()

