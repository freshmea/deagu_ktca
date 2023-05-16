import numpy as np
import pandas as pd

excel = pd.read_excel('output/scientists_df.xlsx', sheet_name='scientists', engine='openpyxl')
print(excel)
print(excel.head())

excel.to_excel('data/scientists_edit_ed.xlsx', index=False, sheet_name='sci_edit')