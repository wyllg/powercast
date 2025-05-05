'''
Data Cleanup

1. Test Print Commands
2. Print Data Types
3. Convert Sep-23 to 2023-09
'''
import pandas as pd
import sqlite3

# Connecting to Database
conn = sqlite3.connect("data/database.db")
c = conn.cursor()

df = pd.read_sql_query("SELECT * FROM electricitydb", conn)

def test_fetch(c):
    command = """SELECT * FROM electricitydb WHERE Month='23-09'"""
    c.execute(command)
    print(c.fetchone())

# test_fetch(c)

def find_data_type(c):
    command = """PRAGMA table_info(electricitydb);"""
    c.execute(command)
    column_info = c.fetchall()

    for col in column_info:
        print(f"Column: {col[1]} | Type: {col[2]}")

# find_data_type(c)

def change_data_type(df):
    df["Month"] = pd.to_datetime(df["Month"], format="%b-%y").dt.strftime("%Y-%m")
    df["Month"] = df["Month"].astype(str)

# change_data_type(df)

# # Drop existing table
# cursor = conn.cursor()
# cursor.execute("DROP TABLE electricitydb")

# # Save back with cleaned Month
# df.to_sql("electricitydb", conn, index=False)

# conn.close()