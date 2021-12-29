# Sea Level Predictor

Anaylyse a dataset of the global average sea level change since 1880. and predict the sea level change through the year 2050.

## Links

- [Assignment](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/sea-level-predictor)

- [Solution](https://replit.com/@borntofrappe/boilerplate-sea-level-predictor)

_Please note:_ the online REPL includes an additional line of code in the body of the `draw_plot` function.

```py
plt.clf()
```

The instruction is necessary to avoid overlapping plots, caused by calling the function repeatedly (the testing module has four tests, each calling the function once) and by relying on the global matplotlib API.

## Data

[Global Average Absolute Sea Level Change](https://datahub.io/core/sea-level-rise), 1880-2014 from the US Environmental Protection Agency using data from CSIRO, 2015; NOAA, 2015.

_Please note:_ to test the code locally I copied the data in `epa-sea-level.csv`.

## Solution

Start by reading the data from the comma separated file.

```py
df = pd.read_csv('epa-sea-level.csv')
```

Immediately, the assignment asks to create a scatter plot with matplotlib, analysing the observations in their year and adjusted sea level.

```py
plt.scatter('Year', 'CSIRO Adjusted Sea Level', data=df)
```

The x axis covers the years in the year column, between 1880 and 2013. As the line of best fit stretches to 2050 it would be possible to manually extend the range through the `plt` instance.

```py
plt.xlim(right=2050)
```

This works to have the x axis expand beyond the last data point in the dataset, but the instruction is ultimately superfluous. As the plot includes the lines of best fit, the axis automatically expand to cover the appropriate interval.

For the line of best fit the assignment asks to rely on the `linregress` function from `scipy.stats` module. [From the documentation]() the function provides a tuple of named arguments, among which the relevant slope and intercept.

```py
result = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
#
```

Given a slope and intercept the line is described by the following equation.

```text
y = slope * x + intercept
```

Pass a `x` in the function, a year, and you retrieve the `y`, the predicted sea level.

It would be enough to plot a line with two points, for the 1880 and 2050 years.

```py
xs = [df['Year'][0], 2050]
ys = [intercept + slope * x for x in xs]
plt.plot(xs, ys)
```

This would work, but the tests for the projects fail asking to provide a line of one point for each year. To work around this the years are retrieved with `pd.period_range()` in a perhaps convoluted manner:

- describe a range of year values between start and end year

  ```py
  pd.period_range(df['Year'][0], 2050, freq='Y')
  ```

- retrieve a reference to only the year value, not a date

  ```py
  period.year
  ```

- return a list

  ```py
  period.year.tolist()
  ```

The end result is that `xs` is populated with the years from 1880 to 2050.

```py
xs1 = pd.period_range(df_2000['Year'][0], 2050, freq='Y').year.tolist()
```

To compute the y coordinates `ys` can rely on the same list expression, since it builds on top of the horizontal coordinate.

With this setup `plt.plot` receives the list of x and y coordinates.

```py
plt.plot(xs, ys)
```

Additional arguments are a matter of changing the style, the color, line width and associated label.

On top of the first line the assignment asks for a second line of best fit, time time computed only with the values after a chosen year, 2000. The process is similar, but requires a smaller set of values in the `. lingress()` function. There are several options, but here I want to highlight just a couple of them:

- find the index of the year and slice the series from said index, leaning on the `iloc` function

  ```py
  index = df[df['Year'] == 2000].index[0]

  df['Year'].iloc[index:]
  df['CSIRO Adjusted Sea Level'].iloc[index:]
  ```

- create a separate data structure where the rows consider only the chosen years

  ```py
  df_2000 = df[df['Year'] > 2000]
  ```

  This approach has the added benefit of repeating the exact logic used for the first line, just computing the horizontal coordinates from the first year of the new dataframe.

  Just be careful that the dataframe has a different index column, and the first year value cannot be accessed as `df_2000['Year'][0]`. Use `df_2000['Year'].iloc[0]` instead.

  It could also be possible to use the `.min()` function, which would also accommodate for a situation in which the data is not ordered by year.

  ```py
  df['Year'].iloc[0] # first row
  df['Year'].min() # earliest year
  ```

To complete the assignment add a title and axis labels. It's not explictly asked by the project, but the plot benefits from a legend as well.

```py
plt.legend()
```

Automatically the plot adds a reference to the dots plotted through the scatterplot, using the name of the two columns passed as arguments.

By adding a label on the line of best fit the legend includes a reference to the lines as well.

```py
plt.plot(xs1, ys1, label=f'Line of Best Fit ({xs[0]}-{xs[-1]})')
```
