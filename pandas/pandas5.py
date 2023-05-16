import numpy as np
import pandas as pd

np.random.seed(20)
sample2 = pd.Series(np.random.randint(100, 200, size=(50,)))
print(sample2[sample2<160])
