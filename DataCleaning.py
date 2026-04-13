# data cleaning is process of cleaning the data

import pandas as pd

df=pd.read_csv("customers-100.csv")
print(df)

# drop column
df=df.drop("Company",axis=1)
print(df)

# drop multiple columns
df=df.drop(["Index","Customer Id"],axis=1)
print(df)

# drop row
df=df.drop(0,axis=0)
print(df)

# drop multiple rows
df=df.drop([0,1,2],axis=0)
print(df)

# Handling missing values
# remove all rows with missing values
df=df.dropna()

# remove only if all values are missing
df=df.dropna(how="all")

# remove rows with missing values in specific columns
df=df.dropna(subset=["Customer Id"])

# modify orginal df
df.dropna(inplace=True)

# fill missing values
df=df.fillna(0)

# fill missing values with specific values
df=df.fillna({"Customer Id":0,"First Name":"Binge","Last Name":"Binge","Email":"Binge","Status":"Binge"})

# fill missing values with mean
df=df.fillna(df.mean(numeric_only=True))

# fix inconsistent values
df["Customer Id"]=df["Customer Id"].replace("DD37Cf93aecA6Dc","1")
print(df)

# remove duplicates
df=df.drop_duplicates()
print(df)

# remove duplicates based on specific columns
df=df.drop_duplicates(subset=["Customer Id"])
print(df)

# standarize text
df["First Name"]=df["First Name"].str.lower()
print(df)

# fix data types
df["First Name"]=df["First Name"].astype(int)
print(df)
