from numpy import NaN, NAN, nan
import numpy as np
import pandas as pd

ebola = pd.read_csv('data/country_timeseries.csv')
print(ebola.info())
ebola_d = ebola[['Date', 'Cases_Mali']].dropna()
print(ebola_d)

print(ebola.Cases_Guinea.sum(skipna=True))
print(ebola.Cases_Guinea.sum())
print(ebola.Cases_Guinea.sum(skipna=False))