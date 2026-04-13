import pandas as pd

df=pd.read_csv("customers-100.csv")
print(df)

# Selection by column
print(df["Customer Id"])
print(df[["Customer Id","First Name"]].to_string())

# Selection by row
print(df.loc[0])
print(df.iloc[0])

# Selection by row with index
df=pd.read_csv("customers-100.csv",index_col="First Name")
print(df.loc["Sheryl"])

# Selection by row with index and column
df=pd.read_csv("customers-100.csv")
print(df.loc[0,"Customer Id"])


