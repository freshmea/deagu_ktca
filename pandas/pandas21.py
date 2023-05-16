import seaborn as sns
import matplotlib.pyplot as plt

anscombe = sns.load_dataset('anscombe')
print(anscombe)
print(type(anscombe))
print(anscombe.info())
dataset1 = anscombe[anscombe['dataset'] == 'I']
# plt.plot(dataset2['x'], dataset1['y'], 'o')
dataset2 = anscombe[anscombe['dataset'] == 'II']
dataset3 = anscombe[anscombe['dataset'] == 'III']
dataset4 = anscombe[anscombe['dataset'] == 'IV']

fig = plt.figure()
axes1 =fig.add_subplot(2,2,1)
axes2 =fig.add_subplot(2,2,2)
axes3 =fig.add_subplot(2,2,3)
axes4 =fig.add_subplot(2,2,4)

axes1.plot(dataset1['x'], dataset1['y'], 'o')
axes2.plot(dataset2['x'], dataset2['y'], 'o')
axes3.plot(dataset3['x'], dataset3['y'], 'o')
axes4.plot(dataset4['x'], dataset4['y'], 'o')
plt.show()