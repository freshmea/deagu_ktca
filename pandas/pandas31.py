import pandas as pd

df1 = pd.read_csv('data/concat_1.csv')
df2 = pd.read_csv('data/concat_2.csv')
df3 = pd.read_csv('data/concat_3.csv')

df1.columns = list('ABCD')
df2.columns = list('EFGH')
df3.columns = list('ACFH')

row_concat = pd.concat([df1, df2, df3])
print(row_concat)

print(pd.concat([df1, df3], ignore_index=True, join='inner'))