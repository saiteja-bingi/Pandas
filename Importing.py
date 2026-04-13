import pandas as pd

df=pd.read_csv("customers-100.csv")

# first 5 and last 5 rows are printed if it was a large file
print(df)

# to print enrtire dataframe
print(df.to_string())

# to print first n rows
print(df.head(10))

# to print last n rows
print(df.tail(10))

# slicing
print(df[10:20])

# importing json file

df=pd.read_json("sample_users_with_id.json")
print(df)

