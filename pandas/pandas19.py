import pandas as pd

scientists = pd.read_csv('data/scientists.csv')
names = scientists['Name']
scientists.to_pickle('output/scientists_df_pickle')
names.to_pickle('output/scientists_name_pickle')
