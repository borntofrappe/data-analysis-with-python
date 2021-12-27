import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
# BMI = weight / height ^ 2 = kg / m ^ 2
# height is in centimeters
# Normalize False and True to 0 and 1; technically unnecessary as booleans are interpreted with the corresponding integer values
df['overweight'] = (df['weight'] / (df['height'] / 100) **
                    2 > 25).replace({True: 1, False: 0})

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df[['cholesterol', 'gluc']] = df[['cholesterol', 'gluc']].astype(
    str).replace({'1': 0, '[2-9]': 1}, regex=True)


def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=[
                     'active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])

    # Draw the catplot with 'sns.catplot()'
    # .set(ylabel) and .fig necessary to pass the unit tests @freecodecamp
    # technically catplot returns a FacetGrid comopsed of the figure
    fig = sns.catplot(data=df_cat, kind='count', col='cardio',
                      x='variable', hue='value').set(ylabel='total').fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


def draw_heat_map():
    # Clean the data
    df_heat = df.drop(df[
        (df['ap_lo'] > df['ap_hi']) |
        (df['height'] < df['height'].quantile(0.025)) |
        (df['height'] > df['height'].quantile(0.975)) |
        (df['weight'] < df['weight'].quantile(0.025)) |
        (df['weight'] > df['weight'].quantile(0.975))
    ].index)

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.full_like(corr, False)
    mask[np.triu_indices_from(mask)] = True

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(9, 8))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, annot=True, annot_kws={
                'fontsize': 'small'}, fmt='.1f', mask=mask, linewidths=0.5, cbar_kws={'shrink': 0.5}, square=True)

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig


draw_cat_plot()
draw_heat_map()
