import numpy as np
import pandas as pd

df1 = pd.DataFrame([[1, 2, 3], [4, 5, 6,],[7, 8, 9]])
print(df1)
df2 = pd.DataFrame([[1, 2, 3], [4, 5, 6,],[7, 8, 9]], columns=['가', '나', '다'])
print(df2)

data = {'name': ['Kim', 'Lee', 'Park'],
        'age': [24, 27, 34],
        'children': [2, 1, 3]
        }
df3 = pd.DataFrame(data)
print(df3.loc[1:2, ['name', 'age']])
