import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('medical_examination.csv')

# BMI = weight / height ^ 2 = kg / m ^ 2
# height is in centimeters
df['overweight'] = df['weight'] / (df['height'] / 100) ** 2 > 25

# map False to 0, map True to 1 (superfluous since booleans are interpreted with the corresponding integer values)
df['overweight'] = df['overweight'].replace({True: 1, False: 0})

# map 1 to 0, map greater than 1 to 1
df[['cholesterol', 'gluc']] = df[['cholesterol', 'gluc']].astype(
    str).replace({'1': 0, '[2-9]': 1}, regex=True)


def draw_cat_plot():
    # long format studying the 'active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke' columns per the 'cardio' value
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=[
                     'active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])

    fig = sns.catplot(data=df_cat, kind='count',
                      col='cardio', x='variable', hue='value')
    fig.set(ylabel='total')

    fig.savefig('catplot.png')
    return fig


def draw_heat_map():
    # drop invalid data following the specs
    df_heat = df.drop(df[
        (df['ap_lo'] > df['ap_hi']) |
        (df['height'] < df['height'].quantile(0.025)) |
        (df['height'] > df['height'].quantile(0.975)) |
        (df['weight'] < df['weight'].quantile(0.025)) |
        (df['weight'] > df['weight'].quantile(0.975))
    ].index)

    corr = df_heat.corr()

    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = 1

    fig, ax = plt.subplots(figsize=(9, 8))

    sns.heatmap(corr, annot=True, annot_kws={
                'fontsize': 'small'}, fmt='.1f', mask=mask, linewidths=0.5, cbar_kws={'shrink': 0.5}, square=True)

    fig.savefig('heatmap.png')
    return fig


draw_cat_plot()
draw_heat_map()
