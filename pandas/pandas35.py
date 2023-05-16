from numpy import NaN, NAN, nan
import numpy as np
import pandas as pd

# NaN 이 생기는 원인
# 1. 데이터 집합을 연결할 때 누락 값(결측치)
# 2. 데이터 입력 할 때 누락 값
# 3. 범위를 지정하여 데이터를 추출 할 때 

ebola = pd.read_csv('data/country_timeseries.csv')
print(ebola.info())
print(ebola.head(3))
print(ebola.count())

total_row = ebola.shape[0]
missing = total_row - ebola.count()
print(missing)

print(np.count_nonzero(ebola['Cases_Guinea'].isnull()))

print(ebola['Cases_Guinea'].value_counts(dropna=False).head())

print(ebola.fillna(0).iloc[0:10 , 0:5])
print(ebola.iloc[0:10 , 0:5])
# print(ebola.fillna(method='ffill').iloc[0:10 , 0:5])
# print(ebola.fillna(method='bfill').iloc[0:10 , 0:5])
print(ebola.interpolate().iloc[0:10 , 0:5])