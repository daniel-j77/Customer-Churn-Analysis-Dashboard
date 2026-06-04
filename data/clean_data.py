import pandas as pd

df=pd.read_csv("customers_raw.csv")

print("Before Cleaning")
print(df.shape)

df["MonthlyCharge"]=df["MonthlyCharge"].fillna(
df["MonthlyCharge"].median()
)

df=df.drop_duplicates()

df["Plan"]=df["Plan"].str.strip()

df.to_csv(
"customers_clean.csv",
index=False
)

print("Cleaning Complete")
print(df.shape)