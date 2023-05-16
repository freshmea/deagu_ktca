import pandas as pd

df = pd.read_csv('data/gapminder.tsv', sep='\t')
print(df.info())
print(df.iloc[-1]) # 가능
# print(df.iloc[1710]) out of bounds
print(df.loc[1])
print(df.iloc[[1,2,120, 1230]])

small_range = list(range(3, 6))
print(df.iloc[:, small_range])
print(df.loc[:, ['lifeExp', 'pop', 'gdpPercap']])

print(df.iloc[:, 3:6])