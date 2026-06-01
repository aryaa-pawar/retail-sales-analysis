import pandas as pd
import sqlite3

df = pd.read_csv(
    "data/Sample - Superstore.csv",
    encoding="latin1"
)

conn = sqlite3.connect("sql/superstore.db")

df.to_sql(
    "sales",
    conn,
    if_exists="replace",
    index=False
)

print("Database Created Successfully!")

conn.close()