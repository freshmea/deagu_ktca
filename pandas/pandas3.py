import numpy as np
import pandas as pd

s1 = pd.Series(['마케팅', '경영', '개발', '기획', '인사'], index=['a', 'b', 'c', 'd', 'e'])
print(s1)
print(s1[0])
print(s1['a'])

s2 = pd.Series(['마케팅', '경영', '개발', '기획', '인사'])
print(s2)
s2.index = list('abcde') # ['a', 'b', 'c', 'd', 'e']
print(s2)