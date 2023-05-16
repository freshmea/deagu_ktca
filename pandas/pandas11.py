import numpy as np
import pandas as pd
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')

df = sns.load_dataset('titanic')
print(df.info())
print(df.head())

print(df.describe())
print(type(df.count()))
print(df['age'].count())
con = df['adult_male'] == True
print(df.loc[con]['age'].mean())
print(df.loc[:, ['age', 'fare']].sum())

print(df['fare'].var())
print(df['fare'].std())
