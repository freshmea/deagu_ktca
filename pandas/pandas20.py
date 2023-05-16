import pandas as pd

scientist_name = pd.read_pickle('output/scientists_name_pickle')
scientists = pd.read_pickle('output/scientists_df_pickle')
print(scientist_name)
print(scientists)