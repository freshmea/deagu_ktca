import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/gapminder.tsv', sep='\t')
aa = df.groupby('year')['lifeExp'].mean()
print(type(aa))
# aa.plot()
plt.plot(aa)
plt.show()