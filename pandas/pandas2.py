import numpy as np
import pandas as pd

s = pd.Series(['부장', '차장', '대리', '사원', '인턴'])
print(s[0])
print(s[[1, 2, 3]])
print(s[np.arange(1, 4, 2)])

np.random.seed(20)
s = pd.Series(np.random.randint(10000, 20000, size=(10,)))
print( s > 15000)
print(s)
print(s[s > 15000])