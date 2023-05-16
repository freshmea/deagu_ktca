import numpy as np
import pandas as pd
import seaborn as sns

df = sns.load_dataset('titanic')
print(df.info())
print(df.head())

print(df['who'].value_counts())
print(df['pclass'].value_counts())
print(df['pclass'].astype('int8').head())
print(df['pclass'].head())

# 정렬
print(df.sort_values('age').head())
print(df.sort_values('age', ascending=False).head())

#조건
cond = df['age'] >= 70
print(df.loc[cond][['age', 'who', 'alive']])
cond1 = df['who'] == 'woman'
cond2 = df['fare'] > 30
print(df.loc[cond1 & cond2][['age', 'who', 'alive', 'fare']])