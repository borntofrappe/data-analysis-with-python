import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter('Year', 'CSIRO Adjusted Sea Level', data=df)
    # once you plot the lines of best fit the plot expands to the appropriate year
    # plt.xlim(right=2050)

    # Create first line of best fit
    result = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    intercept = result.intercept
    slope = result.slope

    xs = pd.period_range(df['Year'].iloc[0], 2050, freq='Y').year.tolist()
    ys = [intercept + slope * x for x in xs]
    plt.plot(xs, ys, '--m', linewidth=2,
             label=f'Line of Best Fit ({xs[0]}-{xs[-1]})')

    # Create second line of best fit
    # start from the year 2000
    df_2000 = df[df['Year'] >= 2000]

    result1 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    intercept1 = result1.intercept
    slope1 = result1.slope

    xs1 = pd.period_range(df_2000['Year'].iloc[0],
                          2050, freq='Y').year.tolist()
    ys1 = [intercept1 + slope1 * x1 for x1 in xs1]

    plt.plot(xs1, ys1, ':r', linewidth=2,
             label=f'Line of Best Fit ({xs1[0]}-{xs1[-1]})')

    # Add labels and title
    plt.legend()
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()


draw_plot()
