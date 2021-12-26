import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from seaborn.rcmod import axes_style

df = pd.read_csv('medical_examination.csv')

# ! height is originally in centimeters
# df['BMI'] = df['weight'] / (df['height'] / 100) ** 2
df['overweight'] = df['weight'] / (df['height'] / 100) ** 2 > 25

df['overweight'] = df['overweight'].replace({True: 1, False: 0})

df[['cholesterol', 'gluc']] = df[['cholesterol', 'gluc']
                                 ].astype(str).replace({'1': 0, '[2-9]': 1}, regex=True)

df_long = pd.melt(df, value_vars=['active', 'alco', 'cholesterol',
                                  'gluc', 'overweight', 'smoke'], id_vars=['cardio'])

fig, ax = plt.subplots()

ax = sns.catplot(kind='count', col='cardio',
                 x='variable', hue='value', data=df_long)
ax.set(ylabel='total')
ax.despine(bottom=True)

plt.savefig('count_plot.jpg')

df_clean = df.drop(df[
    (df['ap_lo'] > df['ap_hi']) |
    (df['height'] < df['height'].quantile(0.025)) |
    (df['height'] > df['height'].quantile(0.975)) |
    (df['weight'] < df['weight'].quantile(0.025)) |
    (df['weight'] > df['weight'].quantile(0.975))
].index)

corr = df_clean.corr()
mask = np.zeros_like(corr)
mask[np.triu_indices_from(mask)] = 1

fig, ax = plt.subplots(figsize=(9, 8))

sns.heatmap(corr, annot=True, annot_kws={'fontsize': 'x-small'},  fmt='.1f',
            mask=mask, linewidths=0.5, cbar_kws={'shrink': 0.5}, square=True)
plt.savefig('heatmap.jpg')
