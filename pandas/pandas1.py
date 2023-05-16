import numpy as np
import pandas as pd

arr = np.arange(100,105)
print(arr)
s1 = pd.Series(arr)
print(s1)
s2 = pd.Series(arr, dtype=np.int8)
print(s2)
s3 = pd.Series(['부장', '차장', '대리', '사원', '인턴'])
print(s3)