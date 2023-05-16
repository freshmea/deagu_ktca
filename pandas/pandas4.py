import numpy as np
import pandas as pd

s1 = pd.Series(['마케팅', '경영', '개발', '기획', '인사'], index=['a', 'b', 'c', 'd', 'e'])
print(s1.values)
print(type(s1.values))
print(s1.ndim)
print(s1.shape)

s2 = pd.Series(['aaaa', 'bbbb', np.nan, 'cccc', 'dddd'])
print(s2)
print(s2.isnull())
print(s2.isna())
print(s2.notnull())
print(s2[s2.notnull()])
