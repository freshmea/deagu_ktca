import pandas as pd
data = {'name': ['Kim', 'Lee', 'Park'],
    'age': [24, 27, 34],
    'children': [2, 1, 3]
    }

df = pd.DataFrame(data, index=['a', 'b', 'c'], columns=['name', 'children', 'age'])
print(df)
print(df.keys())