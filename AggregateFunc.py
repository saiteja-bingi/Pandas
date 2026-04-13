import pandas as pd

df=pd.read_csv("customers-100.csv")

# whole dataframe
print(df.sum(numeric_only=True))
print(df.mean(numeric_only=True))
print(df.median(numeric_only=True))
print(df.mode())
print(df.std(numeric_only=True))
print(df.var(numeric_only=True))
print(df.min())
print(df.max())
print(df.count())

#  single column

print(df["Index"].sum())
print(df["Index"].mean())
print(df["Index"].median())
print(df["Index"].mode())
print(df["Index"].std())
print(df["Index"].var())
print(df["Index"].min())
print(df["Index"].max())
print(df["Index"].count())

# groupby

print("\nGrouping:")
group=df.groupby("Company")
print(group.mean(numeric_only=True))