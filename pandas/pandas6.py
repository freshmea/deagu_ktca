import numpy as np
import pandas as pd
sample = pd.Series(['IT서비스', np.nan, '반도체', np.nan, '바이오', '자율주행'])

print(sample[sample.isna()])
print(sample[sample.notnull()])
