import pandas as pd
# it is a one dimensional labeled array
# it can hold any data type
# think it like a single column in spreadsheet

# pythin list
data=[1,2,3,4]

# convert into series
series=pd.Series(data)
print(series)

# create series with custom index
series=pd.Series(data,index=["a","b","c","d"])
print(series)

# create series from dictionary
data={"a":1,"b":2,"c":3,"d":4}
series=pd.Series(data)
print(series)

# locate by index label
print(series.loc["c"])

# locate by index position
print(series.iloc[2])

data=[100,200,300,400,50]
series=pd.Series(data)
print(series[series<=100])

series={"day-1":100,"day-2":200,"day-3":300,"day-4":400,"day-5":50}
series["day-5"]=600
series=pd.Series(series)
print(series)
series.loc["day-1"]=1000
print(series)

