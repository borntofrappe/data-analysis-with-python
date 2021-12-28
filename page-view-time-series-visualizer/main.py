import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv',
                 index_col='date', parse_dates=['date'])

# Clean data
# by filter out days when the page views were in the top 2.5% or bottom 2.5%
df = df.drop(df[
    (df['value'] > df['value'].quantile(0.975)) |
    (df['value'] < df['value'].quantile(0.025))
].index)


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(20, 5))

    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.plot(df, 'm')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar = df_bar.resample('M').mean()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month

    df_bar = df_bar.pivot('year', 'month', 'value')

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(9, 8))
    df_bar.plot.bar(ax=ax)
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    labels = pd.date_range(
        start='2020/01/01', periods=12, freq='M').month_name()
    ax.legend(title='Months', labels=labels)

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, axs = plt.subplots(1, 2, figsize=(30, 10))
    ax1, ax2 = axs

    sns.boxplot(data=df_box, x='year', y='value', ax=ax1)
    ax1.set_title('Year-wise Box Plot (Trend)')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')

    order = pd.date_range(start='2020/01/01', periods=12,
                          freq='M').strftime('%b')
    sns.boxplot(data=df_box, x='month', y='value', ax=ax2, order=order)
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig


draw_line_plot()
draw_bar_plot()
draw_box_plot()
