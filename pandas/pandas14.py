import pandas as pd

df = pd.read_csv('data/gapminder.tsv', sep='\t')
print(df.groupby('year')['lifeExp'].describe())
print(df.groupby(['year', 'continent'])['lifeExp'].mean())

print(df.groupby('continent')['country'].nunique())