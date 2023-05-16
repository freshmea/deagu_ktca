import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset('tips')

plt.boxplot([tips[tips['sex'] == 'Female']['tip'],tips[tips['sex'] == 'Male']['tip']], labels=['Female', 'Male'])
plt.xlabel('total bill')
plt.ylabel('tip')
plt.show()