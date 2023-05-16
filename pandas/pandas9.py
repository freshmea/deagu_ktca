import pandas as pd

df = pd.read_csv('data/scientists.csv')

print(df)
print(df[['Name', 'Age']])
df[['Name', 'Age']].to_csv('output/scientists_age.csv', index=False)
