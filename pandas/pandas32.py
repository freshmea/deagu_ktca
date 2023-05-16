import pandas as pd

df1 = pd.read_csv('data/concat_1.csv')
df2 = pd.read_csv('data/concat_2.csv')
df3 = pd.read_csv('data/concat_3.csv')

df1.index = [0,1,2,3]
df2.index = [4,5,6,7]
df3.index = [0,2,5,7]

col_concat = pd.concat([df1, df2, df3], axis=1)
print(col_concat)
col_concat = pd.concat([df2, df3], axis=1, join='inner')
print(col_concat)