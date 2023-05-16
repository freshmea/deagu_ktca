import pandas as pd
import random

random.seed(44)
scientists = pd.read_csv('data/scientists.csv')
print(scientists['Age'])
age = list(scientists['Age'])
random.shuffle(age)
print(age)

drop_df = scientists.drop(['Age'], axis=1)
print(drop_df)