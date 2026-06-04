import streamlit as st
import pandas as pd

df=pd.read_csv(
"../data/customers_clean.csv"
)

st.title(
"Customer Churn Dashboard"
)

plan=st.selectbox(
"Plan",
["All"]+
list(df.Plan.unique())
)

if plan!="All":
    df=df[df.Plan==plan]

total=len(df)

avg=df[
"MonthlyCharge"
].mean()

churn=len(
df[df["Churn"]=="Yes"]
)

col1,col2,col3=st.columns(3)

col1.metric(
"Customers",
total
)

col2.metric(
"Avg Charge",
f"₹{avg:.0f}"
)

col3.metric(
"Churned",
churn
)

st.subheader(
"Churn Distribution"
)

st.bar_chart(
df["Churn"].value_counts()
)

st.subheader(
"Plan Distribution"
)

st.bar_chart(
df["Plan"].value_counts()
)

st.dataframe(df)