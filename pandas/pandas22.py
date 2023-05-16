import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset('tips')
print(tips.head())
print(tips.info())

# scatter_plot = plt.figure()
plt.plot(tips['total_bill'], tips['tip'], 'o')
plt.xlabel('total bill')
plt.ylabel('tip')
plt.show()