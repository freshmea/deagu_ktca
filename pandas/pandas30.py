import pandas as pd

df1 = pd.read_csv('data/concat_1.csv')
df2 = pd.read_csv('data/concat_2.csv')
df3 = pd.read_csv('data/concat_3.csv')

col_concat = pd.concat([df1, df2, df3], axis=1)
print(col_concat['A'])
col_concat_noindex = pd.concat([df1, df2, df3], axis=1, ignore_index=True)
print(col_concat_noindex)