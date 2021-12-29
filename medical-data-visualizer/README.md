# Medical Data Visualizer

Analyse and visualize medical data with two charts:

- [a count plot](https://replit.com/@borntofrappe/boilerplate-medical-data-visualizer#examples/Figure_1.png) to count the number of instances for several binary variables (for instance `active`, `alco`, `cholesterol`), splitting the count according to the value of a defining metric (`cardio`)

- [a correlation matrix](https://replit.com/@borntofrappe/boilerplate-medical-data-visualizer#examples/Figure_2.png) to evaluate the relationship between several variables (for instance `age`, `gender`, `height`, `weight`)

## Links

- [Assignment](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/medical-data-visualizer)

- [Solution](https://replit.com/@borntofrappe/boilerplate-medical-data-visualizer)

## Data

Provided in the assignment.

_Please note:_ to test the code locally I copied the first and last 200 observations of the entire dataset in `medical_examination.csv`.

The rows in the dataset represent patients and the columns represent information like body measurements, results from various blood tests, and lifestyle choices.

|                    Feature                    |    Variable Type    |  Variable   |                    Value Type                    |
| :-------------------------------------------: | :-----------------: | :---------: | :----------------------------------------------: |
|                      Age                      |  Objective Feature  |     age     |                    int (days)                    |
|                    Height                     |  Objective Feature  |   height    |                     int (cm)                     |
|                    Weight                     |  Objective Feature  |   weight    |                    float (kg)                    |
|                    Gender                     |  Objective Feature  |   gender    |                 categorical code                 |
|            Systolic blood pressure            | Examination Feature |    ap_hi    |                       int                        |
|           Diastolic blood pressure            | Examination Feature |    ap_lo    |                       int                        |
|                  Cholesterol                  | Examination Feature | cholesterol | 1: normal, 2: above normal, 3: well above normal |
|                    Glucose                    | Examination Feature |    gluc     | 1: normal, 2: above normal, 3: well above normal |
|                    Smoking                    | Subjective Feature  |    smoke    |                      binary                      |
|                Alcohol intake                 | Subjective Feature  |    alco     |                      binary                      |
|               Physical activity               | Subjective Feature  |   active    |                      binary                      |
| Presence or absence of cardiovascular disease |   Target Variable   |   cardio    |                      binary                      |

## Solution

For the dataset:

- add an `overweight` column

  To determine if a person is overweight it is first necessary to calculate _BMI_ by dividing the weight in kilograms by the square of their height in meters.

  The height in the dataset is in centimeters, so that it is necessary to first change the unit of measure.

  ```py
  df['BMI'] = df['weight'] / (df['height'] / 100) ** 2
  ```

  If the value exceeds 25 then the person is overweight.

  ```py
  df['overweight'] = df['BMI'] > 25
  ```

  Use the value 0 for **NOT** overweight and the value 1 for overweight.

  The previous snippet creates a series of boolean values where `True` describes the overweight status. `.replace` updates the existing boolean to the desired integers.

  ```py
  df['overweight'] = df['overweight'].replace({True: 1, False: 0})
  ```

  _Please note:_ in the script the three snippets are united in the same line, creating the series of booleans and replacing the values.

- normalize the data by making 0 always good and 1 always bad

  If the value of `cholesterol` or `gluc` is 1 make the value 0. If the value is more than 1 make the value 1.

  Start by targeting the desired columns.

  ```py
  df[['cholesterol', 'gluc']] = #...
  ```

  `replace` would help to update the values, and the idea is to find values greater than 1 with a regular expression targeting numbers in the `[2-9]` range.

  ```py
  df[['cholesterol', 'gluc']].replace({1: 0, '[2-9]': 1}), regex=True)
  ```

  The problem with this approach is that regular expressions work on string values, not numerical ones. To work around this issue interpret the values as strings first.

  ```py
  df[['cholesterol', 'gluc']].astype(str).replace({'1': 0, '[2-9]': 1}), regex=True)
  ```

  Note that `1` is also targeted with the character `'1'` since the column includes all string values.

For the count plot:

- convert the data into long format

  The script suggests using `pd.melt`, and the solution is surprisingly straightforward.

  ```py
  df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])
  ```

  The result is a dataframe of 2400 rows where the individual variables are repeated alongside the `cardio` value.

  ```py
  df_cat
  """
        cardio variable  value
  0          0   active      1
  1          1   active      1
  ...
  2398       1    smoke      0
  2399       0    smoke      0
  """
  ```

- create the count plot with seaborn's `catplot()` function

  Following the [seaborn documentation](https://seaborn.pydata.org/generated/seaborn.catplot.html) the relevant type of chart is a catplot with kind set to `count`.

  ```py
  sns.catplot(data=df_cat, kind='count', col='cardio' x='variable', hue='value')
  ```

  Thanks to `col` the data is separated in two adjacent bar charts. On the `x` axis the chart plots the variables, and the `hue` distinguishes the value (0 or 1) with color.

  It would be possible to complete the visualization as follows.

  ```py
  fig = sns.catplot(data=df_cat, kind='count', col='cardio' x='variable', hue='value')
  fig.set(ylabel='total')
  fig.savefig('catplot.png')
  ```

  However, and for the purposes of the assignment, it is necessary to modify the code by extracting the figure from `sns.catplot` as follows.

  ```py
  fig = sns.catplot(data=df_cat, kind='count', col='cardio' x='variable', hue='value').fig
  ```

  This can be explained by the fact that the seaborn function actually returns a "FacetGrid", not a figure (which also makes the preceding snippet incorrect as `fig` doesn't describe the figure).

  The figure doesn't have support the `set(ylabel)` function, so that to change the value you need to chain the method on the instance of the facet grid.

  ```py
  fig = sns.catplot(data=df_cat, kind='count', col='cardio' x='variable', hue='value').set(ylabel='total').fig
  ```

For the correlation matrix:

- clean the data by filtering out the following patient segments, assumed to represent incorrect data:

  - diastolic pressure is higher than systolic

  - height is less than the 2.5th percentile

  - height is more than the 97.5th percentile

  - weight is less than the 2.5th percentile

  - weight is more than the 97.5th percentile

  Start by identifying the invalid data. For instance and for the pressure, consider when `ap_lo` has a greater value than `ap_hi`.

  ```py
  df[df['ap_lo'] > df['ap_hi']]
  ```

  For the percentiles compute the relevant metric with the `.quantile` method. For the height, but for the weight as well.

  ```py
  df[df['height'] < df['height'].quantile(0.025)]
  df[df['height'] > df['height'].quantile(0.975)]
  ```

  You can analyse the conditions separately, but in the same statement identify the relevant rows grouping the conditions in parenthesis, separating them with the pipe character to check at least one condition matches (or operator)

  ```py
  df[(
  (df[df['ap_lo'] > df['ap_hi']]) |
  (df['height'] > df['height'].quantile(0.975)) |
  # ...
  )]
  ```

  The result is a dataframe of rows with invalid data.

  ```py
  """
        id    age  gender  height  ...  alco  active  cardio  overweight
  15      24  16782       2     172  ...     0       0       1           1
  23      33  23376       2     156  ...     0       1       0           0
  46      61  18207       1     162  ...     0       1       1           1
  """
  ```

  To remove the rows from the original dataframe use the index column in the drop function.

  ```py
  df_heat = df.drop(
    df[(
      # ...
    )].index
  )
  ```

- create the correlation matrix with seaborn's `heatmap()` function, making sure to mask the upper portion and show only the lower left triangle

  Start by calculating the correlation matrix with pandas.

  ```py
  corr = df_heat.corr()
  ```

  Following the [seaborn documentation](https://seaborn.pydata.org/generated/seaborn.heatmap.html) it is enough to plot the data as follows.

  ```py
  fig, ax = plt.subplots()
  sns.heatmap(corr)
  fig.savefig('heatmap.png')
  ```

  However, and for the purposes of the assignment it is necessary to change the default visual.

  Keyword arguments allow to include text values in the squares, with small print and the chosen numbers after the decimal point.

  ```py
  annot=True, annot_kws={'fontsize': 'small'}, fmt='.1f'
  ```

  Additional arguments allow to separate the squares with a line, shrink the color bar and maintain each cell as a square.

  ```py
  linewidths=0.5, cbar_kws={'shrink': 0.5}, square=True
  ```

  The square argument helps in the moment the figure is given a rectangular size. The chosen size ensures that the labels on the axis are not cropped.

  ```py
  fig, ax = plt.subplots(figsize=(9, 8))
  ```

  One final argument, `mask`, allows to show only the lower left portion of the matrix. The logic requires a couple of steps, and is taken directly from the example in the seaborn documentation.

  ```py
  mask = np.full_like(corr, False)
  mask[np.triu_indices_from(mask)] = True
  ```

  The idea is to create an array of the same size as the correlation matrix, where the upper right portion is populated with `True` values. The mask arguments hides the squares matching these boolean.
