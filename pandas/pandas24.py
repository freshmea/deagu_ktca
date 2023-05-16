import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def recode_sex(sex):
    if sex == 'Female':
        return False
    else:
        return True

tips = sns.load_dataset('tips')

tips['sex_color'] = tips['sex'].apply(recode_sex)
plt.scatter(x = tips['total_bill'],
            y = tips['tip'],
            s = tips['size']*30,
            c = tips['sex_color'],
            alpha=0.5)

plt.show()