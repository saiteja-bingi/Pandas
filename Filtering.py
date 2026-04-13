# filtering = keeping the rows which matches the condition

import pandas as pd

df=pd.read_csv("customers-100.csv")

x=df[df["Index"]>10]
print(x.to_string())

# use c & | !
x=df[(df["Index"]>10) | (df["Index"]<5)]
print(x.to_string())

# use isin() method
x=df[df["Index"].isin([1,2,3,4,5])]
print(x.to_string())

# use notisin() method
x=df[~df["Index"].isin([1,2,3,4,5])]
print(x.to_string())
