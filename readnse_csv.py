import pandas as pd 

data  = pd.read_csv("MW-All-Indices-25-Jan-2023.csv")
print(data.head())
print(data.columns)
index = data['INDEX \n'].values
print(len(index))