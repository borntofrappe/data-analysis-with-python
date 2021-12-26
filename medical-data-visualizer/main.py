import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from seaborn.rcmod import axes_style

df = pd.read_csv('medical_examination.csv')

# BMI: weight (kg) / height ^ 2 (meters ^ 2)
# ! height is originally in centimeters
# df['BMI'] = df['weight'] / (df['height'] / 100) ** 2

# overweight: BMI > 25
df['overweight'] = df['weight'] / (df['height'] / 100) ** 2 > 25
# 0 not overweight, 1 overweight
df['overweight'] = df['overweight'].replace({True: 1, False: 0})

# normalize `cholesterol` or `gluc`: 1 -> 0, >1 -> 1
df[['cholesterol', 'gluc']] = df[['cholesterol', 'gluc']
                                 ].astype(str).replace({'1': 0, '[2-9]': 1}, regex=True)

# long format
# df_long = pd.melt(df, value_vars=['active', 'alco', 'cholesterol',
                                  # 'gluc', 'overweight', 'smoke'], id_vars=['cardio'])

# count_plot = sns.catplot(kind='count', col='cardio',
#  x='variable', hue='value', data=df_long)
# count_plot.set(ylabel='total')
# count_plot.despine(bottom=True) # remove x axis line
# count_plot.savefig('count_plot.jpg')

# searborn heatmap
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

ax = sns.heatmap(corr, annot=True, annot_kws={'fontsize': 'x-small'},  fmt='.1f',
                 mask=mask, linewidths=0.5, cbar_kws={'shrink': 0.5})
plt.savefig('heatmap.jpg')
