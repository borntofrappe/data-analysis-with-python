import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter('Year', 'CSIRO Adjusted Sea Level', data=df)
    # plt.xlim(right=2050)

    # Create first line of best fit
    result = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    intercept = result.intercept
    slope = result.slope

    xs = [df['Year'][0], 2050]
    ys = [intercept + slope * x for x in xs]
    plt.plot(xs, ys, '--m', linewidth=2,
             label=f'Line of Best Fit ({xs[0]}-{xs[1]})')

    # Create second line of best fit
    xs1 = [2000, 2050]
    index = df[df['Year'] == xs1[0]].index[0]
    result1 = linregress(df['Year'].iloc[index:],
                         df['CSIRO Adjusted Sea Level'].iloc[index:])
    intercept1 = result1.intercept
    slope1 = result1.slope

    ys1 = [intercept1 + slope1 * x1 for x1 in xs1]
    plt.plot(xs1, ys1, ':r', linewidth=2,
             label=f'Line of Best Fit ({xs1[0]}-{xs1[1]})')

    plt.legend()

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()


draw_plot()
