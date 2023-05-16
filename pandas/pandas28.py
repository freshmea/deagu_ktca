import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset('tips')
sns.violinplot([tips[tips['sex'] == 'Female']['tip'],tips[tips['sex'] == 'Male']['tip']])
plt.xlabel('total bill')
plt.ylabel('tip')
plt.show()