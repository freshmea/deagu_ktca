import pandas as pd

df1 = pd.read_csv('data/concat_1.csv')
df2 = pd.read_csv('data/concat_2.csv')
df3 = pd.read_csv('data/concat_3.csv')

row_concat = pd.concat([df1, df2, df3])
print(row_concat)
# print(row_concat.loc[0])
# print(row_concat.iloc[4])

new_df = pd.DataFrame([['n1', 'n2', 'n3', 'n4']], index=[4,],columns=list('ABCD'))
print(new_df)
print(pd.concat([df1, new_df]))
print(df1.combine_first(new_df))
print(df1._append(new_df))