import pandas as pd

df = pd.read_csv('data/gapminder.tsv', sep='\t')
print(df.info())
print(df.head())
print(df.columns)
print(type(df.columns))
print(df.columns[0])
print(df.tail())

subset = df[['country', 'continent', 'year']]
print(subset)

# print(subset.loc[-1]) 에러
print(df.shape[0]) # 전체 줄의 갯수
print(df.count()[0]) # 전체 줄의 갯수 
print(df.tail(1))