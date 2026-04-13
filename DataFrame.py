import pandas as pd

# DataFrame is a 2D labeled data structure with columns of potentially different types
# think it like a spreadsheet or SQL table

#dictionary with lists converted into DataFrame
data={"Name":["Binge","Binge","Binge"],
    "Age":[21,22,23],
    "City":["Delhi","Mumbai","Kolkata"]}
df=pd.DataFrame(data)
print(df)

# custom index
df=pd.DataFrame(data,index=["a","b","c"])
print(df)

# locating using loc,iloc and column name
print(df.loc["a"])
print(df.iloc[0])
print(df["Name"])


# add a new column
# no of values must match with the number of rows
df["salary"]=[100,200,300]
print(df)

# add a new row
new_row=pd.DataFrame([{"Name":"Ajay","Age":24,"City":"Kolkata","salary":400}])

# ignore list index = True makes rearrange indexes
df=pd.concat([df,new_row],ignore_index=True)
print(df)

# ignore list index = False makes keep indexes
new_row=pd.DataFrame([{"Name":"Ajay","Age":24,"City":"Kolkata","salary":400}],index=["d"])
df=pd.concat([df,new_row],ignore_index=False)
print(df)

# drop a column
# axis=1 mean column
# inplace=True means modify the original DataFrame
pdf=df.drop("salary",axis=1,inplace=False)
print(pdf)
print(df)

# drop a row
# axis=0 mean row
df.drop("d",axis=0,inplace=True)
print(df)

# conditional filtering
print(df[df["Age"]>22])
