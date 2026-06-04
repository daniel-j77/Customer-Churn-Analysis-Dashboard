import sqlite3
import pandas as pd

df=pd.read_csv("../data/customers_clean.csv")

conn=sqlite3.connect(
"customers.db"
)

df.to_sql(
"customers",
conn,
if_exists="replace",
index=False
)

print("Database Created")

conn.close()