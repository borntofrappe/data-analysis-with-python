# Page View Time Series Visualizer

Visualize time series using a line chart, a bar chart, and box plots. You will use Pandas, Matplotlib, and Seaborn to visualize a dataset containing the number of page views each day on the freeCodeCamp.org forum from 2016-05-09 to 2019-12-03.

_Please note:_ to test the code locally I copied the data in `fcc-forum-pageviews.csv`.

## Links

- [Assignment](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/page-view-time-series-visualizer)

- [Solution](https://replit.com/@borntofrappe/boilerplate-page-view-time-series-visualizer)

## Solution

Begin by reading and the data from the `.csv` file:

- import the data from "fcc-forum-pageviews.csv"

- set the index to the "date" column.

- parse dates

To achieve the three features store the data in a dataframe with `pd.read_csv`. Specify the index column and the parsing of the dates with the appropriate keyword arguments.

```py
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=['date'])
```

It would be possible to parse the dates considering the entire dataframe, and not just the date column, with a boolean.

```py
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)
```

Regardless, attest the presence of the date type considering the index column.

```py
df.index
'''
DatetimeIndex(['2016-05-09', '2016-05-10', ...], dtype='datetime64[ns]', ...)
'''
```

Following the specification for the project clean the data by filtering out days when the page views were in the top 2.5% or bottom 2.5%.

The relevant function is here `quantile()`. Start by finding the rows exceeding the two thresholds.

```py
df[
    (df['value'] > df['value'].quantile(0.975)) |
    (df['value'] < df['value'].quantile(0.025))
]
```

Drop the rows by index and from the original dataframe.

```py
df = df.drop(df[
  #... quantile checks
])
```

One quick way to confirm that the rows are dropped is considering the length of the dataframe, before and after the snippet.

```py
len(df) # 1304

# drop

len(df) # 1238
```

With the resulting dataframe create three visualizations.

### Line plot

The assignment asks to populate the `draw_line_plot` function to draw a line chart similar to [the example](https://replit.com/@borntofrappe/boilerplate-page-view-time-series-visualizer#examples/Figure_1.png). Page views are plotted on the y axis, while the x axis describes the entire range of the selected data.

In terms of setup, repeated for other visualizations, matplotlib allows to plot data with a figure and ax.

```py
fig, ax = plt.subplots()

# plot on the ax

fig.savefig('visualization.png')
```

For the line plot, given the number of data points, have the figure considerably wider than taller.

```py
fig, ax = plt.subplots(figsize=(16, 4))
```

It would be enough to draw the line with `ax.plot(df)`, referencing the dataframe directly.

```py
ax.plot(df, 'm') # maroon line
```

Per the assignment, however, it is first necessary to set the title and labels.

```py
ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
ax.set_xlabel('Date')
ax.set_ylabel('Page Views')
```

### Bar plot

The assignment asks to populate the `draw_bar_plot` function to draw a bar chart similar to [the example](https://replit.com/@borntofrappe/boilerplate-page-view-time-series-visualizer#examples/Figure_2.png). Page views are averaged by month and grouped by year.

The first step is creating a copy of the dataframe, so that further modifications do not alter the original structure.

```py
df_bar = df.copy(True)
```

The chart needs to plot the average page views on a monthly basis, so modify the dataframe with the desired time range. Pandas offers the `.resample` method which creates a `DatetimeIndexResampler` with a given frequency, here months.

```py
df_bar.resample('M')
```

Based on the resampler retrieve a dataframe describing the averages chaining the `.mean` function.

```py
df_bar.resample('M').mean()
"""
                    value
date
2016-05-31   19432.400000
2016-06-30   21875.105263
2016-07-31   24109.678571
2016-08-31   31049.193548
2016-09-30   41476.866667
2016-10-31   27398.322581
"""
```

Notice the index which is no longer based on days, but on months.

To draw the bars next to each other the relevant function doesn't come from matplotlib, but from pandas (even though it is likely there is a connection between the two APIs). The function is available as a method on the dataframe: `df.plot.bar`.

Learning from the second example [in the documentation](<(https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.bar.html)>) the function requires a dataframe with a specific structure, one where the index describes the four years and the columns describe the months.

```py
"""
month   1       2 ...
2016    5      12 ...
2017    7      21 ...
...
"""
```

To achieve the structure pandas offers the `.pivot` function. However, the dataframe needs to include the year and month for each observations.

```py
df_bar['year'] = df_bar.index.year
df_bar['month'] = df_bar.index.month

"""
      value   year    month
date      5   2016        1
"""
```

With this setup use `pivot` to create the data structure with the years in the index and the months in the columns.

```py
df_bar = df_bar.pivot('year', 'month', 'value')
```

Finally, through the mentioned `.plot.bar` method, plot the data in adjacent bars.

```py
df_bar.plot.bar()
```

To draw the visual in the figure refer to the ax.

```py
fig, ax = plt.subplots(figsize=(7, 6))
df_bar.plot.bar(ax=ax)
```

This completes the bar plot. Per the assignment, however, it is necessary to customize the axis labels.

```py
ax.set_xlabel('Years')
ax.set_ylabel('Average Page Views')
```

For the legend `.legend()` creates the desired section in the top left corner, but displays integer values.

```py
ax.legend(title='Months')
```

One way to work around this is to specify the name of the months directly through the `labels` keyword argument.

```py
ax.legend(title='Months', labels=labels)
```

To create the labels the pandas library allows to rapidly create twelve dates in an arbitrary year and retrieve the month for each date.

```py
labels = pd.date_range(start='2020/01/01', periods=12, freq='M').month_name()
```

### Box plot

The assignment asks to populate the `draw_box_plot` function to draw two plots similar to [the example](https://replit.com/@borntofrappe/boilerplate-page-view-time-series-visualizer#examples/Figure_3.png). Each box plot focuses on a different time range, years and months, to show the distribution and outliers of the page views variable.

The function already includes instructions to prepare the data.

```py
df_box = df.copy()
df_box.reset_index(inplace=True)
df_box['year'] = [d.year for d in df_box.date]
df_box['month'] = [d.strftime('%b') for d in df_box.date]
```

A few things worth noting, which might also lead to modifications in the preceding functions:

- `df.copy()` doesn't include the boolean to create a deep copy

  Checking [the documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.copy.html) it actually seems pandas sets the boolean to `True` by default.

- `df_box.reset_index(inplace=True)` modifies the dataframe to have the `date` and `value` in their respective column

  ```py
  df_box = df.copy()
  '''
              value
  date
  2016-05-19   19736
  2016-05-26   18060
  '''

  df_box.reset_index(inplace=True)
  df
  '''
            date   value
  0    2016-05-19   19736
  1    2016-05-26   18060
  '''
  ```

- the remaining two lines populate two columns with the year and month value

  The operation is achieved with list expressions creating a list of years and month names. Considering the year as an example the following:

  ```py
  years = [d.year for d in df_box.date]
  ```

  Is equivalent to the following sequence:

  ```py
  years = []
  for d in df_box['date']:
    years.append(d.year)
  ```

  A similar logic creates a list of months, but using the name of the month through the `strftime` function.

For the box plot, as required by the project, create two ax objects. With `plt.subplot()` indicate the visualization should have one row and two columns.

```py
fig, axs = plt.subplots(1, 2, figsize=(30, 10))
```

Extract the individual ax objects from the returned sequence of tuples.

```py
ax1, ax2 = axs
```

For the box plot the seaborn library provides the `.boxplot()` function. The relevant keyword arguments for the projects are:

- `data`, pointing toward the data frame

- `x`, the horizontal position of the boxes

- `y`, the variable to examine in distribution, in mean, interquartile range and outliers

- `ax`, the ax on which to plot the data

The difference between the two plots is the `x` argument, directing toward the year and the month respectively.

```py
sns.boxplot(data=df_box, x='year', y='value', ax=ax1)
sns.boxplot(data=df_box, x='month', y='value', ax=ax2)
```

The box plots are drawn. However, the months are drawn starting with the month of May. This is because the first year, 2016, begins indeed from the month of May. To maintain the calendar order the `order` keyword argument allows to specify the desired labels.

```py
order = pd.date_range(start='2020/01/01', periods=12, freq='M').strftime('%b')
```

The process mirrors that of the labels for the bar plot, but creates a series for the short version of the names. The bar plot could be updated to match.

```py
labels = pd.date_range(start='2020/01/01', periods=12, freq='M').strftime('%B')
```

With the box plots drawn, the last step relates to the title and axis labels. Include the strings specified by the assignment in the respective ax.
