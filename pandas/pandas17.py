import pandas as pd

scientists = pd.read_csv('data/scientists.csv')
ages = scientists['Age']
cond = ages > ages.mean()
print(ages.mean())
print(scientists.loc[cond])

born_datetime = pd.to_datetime(scientists['Born'], format='%Y-%m-%d')
died_datetime = pd.to_datetime(scientists['Died'], format='%Y-%m-%d')
print(scientists)
scientists['born_dt'] = born_datetime # 데이터프레임에 컴럼 추가.
scientists['died_dt'] = died_datetime 
scientists['age_days_dt'] = scientists['died_dt']-scientists['born_dt']
print(scientists)