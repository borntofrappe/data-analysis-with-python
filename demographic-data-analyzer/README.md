# Demographic Data Analyzer

Analyse a dataset of demographic data extracted from the 1994 Census database, considering such properties as age, work class, education, occupation and relationship.

## Links

- [Assignment](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/demographic-data-analyzer)

- [Solution](https://replit.com/@borntofrappe/boilerplate-demographic-data-analyzer)

## Data

Dua, D. and Graff, C. (2019). [UCI Machine Learning Repository](http://archive.ics.uci.edu/ml). Irvine, CA: University of California, School of Information and Computer Science.

_Please note:_ to test the code locally I copied the first and last 200 observations of the entire dataset in `adult.data.csv`.

## Solution

The function is completed point by point exploring the `pandas` library:

- How many people of each race are represented in this dataset?

  The assignment asks for the data in a pandas series, so that it is enough to return the sequence from the `.value_counts()` function.

  ```py
  race_count = df['race'].value_counts()
  ```

  The index of this series is indeed the string describing each race, while the value is the number of times the observations are repeated.

- What is the average age of men?

  Filter the observations according to the `sex` column and the desired field.

  ```py
  df[df['sex'] == 'Male']
  ```

  Many of the remaining functions will leverage the same syntax to consider a subset of the rows.

  Refer to the series making up the `age` column.

  ```py
  df[df['sex'] == 'Male']['age']
  ```

  Compute the average.

  ```py
  df[df['sex'] == 'Male']['age'].mean()
  ```

- What is the percentage of people who have a Bachelor's degree?

  Filter the observations according to the `education` column, looking specifically for the `Bachelors` string.

  ```py
  df[df['education'] == 'Bachelors']
  ```

  Use the `len(DataFrame)` function to estimate the number of rows and divide by value by the number of rows in the original dataframe.

  ```py
  len(df_bachelors) / len(df) * 100
  ```

  _Note:_ `df_bachelors` is actually not defined in the script, where I preferred to include the preceding snippet as-is.

  As per the assignment, round the estimate to the nearest ten.

  ```py
  round(percentage, 1)
  ```

  The same approximation is applied to the rest of the assignment, without further mention.

- What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?

  It would be possible to chain multiple conditions in the square brackets `df[]`:

  ```py
  (df['education'] == 'Bachelors') |
  (df['education'] == 'Masters') |
  (df['education'] == 'Doctorate')
  ```

  In place of this syntax the `.isin` method describes whether the value matches one of the items in the input sequence.

  ```py
  df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
  ```

  With this information, stored in a variable to avoid an excessive number of lines, finding the desired percent value is a matter of considering the number of rows _in this dataframe_ which earn more than 50K.

  ```py
  higher_education[higher_education['salary'] == '>50K']
  ```

  Divide the length of this data structure by the length of the computed dataframe.

- What percentage of people without advanced education make more than 50K?

  The question is approached similarly to the previous bullet point, with the only difference being how to consider the data structure describing values _not_ falling in one of the three categories.

  Once again, it would be possible to chain multiple conditions, and use a tilde character ` ` to consider the opposing instance.

  A different solution is however to drop the values of the preceding dataframe.

  ```py
  lower_education = df.drop(higher_education.index)
  ```

  `higher_education.index` creates a series with the rows including the three string.

- What is the minimum number of hours a person works per week?

  ```py
  min_work_hours = df['hours-per-week'].min()
  ```

- What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?

  First isolate the rows where the number of hours matches the minimum.

  ```py
  df[df['hours-per-week'] == min_work_hours]
  ```

  From this subset consider the rows in which the `salary` column matches the `>50K` string.

  ```py
  min_workers[min_workers['salary'] == '>50K']
  ```

  The percentage is computed exactly like in previous bullet points, considering the number of rows through the `len` function

- What country has the highest percentage of people that earn >50K and what is that percentage?

  To answer the question it is first necessary to describe two data structures, one describing the countries represented in the dataframe, one describing the countries with the specified salary.

  ```py
  countries = df['native-country'].value_counts()
  rich_countries = df[df['salary'] == '>50K']['native-country'].value_counts()
  ```

  From this setup estimate the highest earning countries dividing the second series by the first, sorting the values with `sort_values()` and in descending order.

  ```py
  highest_earning_countries = (rich_countries / countries).sort_values(ascending=False)
  ```

  The problem with this approach is that the series resulting from the division may include `NaN` values when a country exist is one dataframe and not the other. To fix this pandas offers the `series.divide()` function, and allows to customize the division with a fill value.

  ```py
  rich_countries.divide(countries, fill_value=0)
  ```

  The result of the division is a series describing the countries by percentages. The sorting operation makes it possible to have the first row describe the highest earning country. To fulfill the assignment retrieve the name and percentage with the `idxmax()` and `max()` function respectively.

  ```py
  highest_earning_countries.idxmax()
  highest_earning_countries.max()
  ```

  The percentage is rounded as other decimal values, but the logic remains the same.

- What is the most popular occupation for those who earn >50K in India?

  Start by filtering the dataframe for the rows describing the given native country _and_ salary.

  ```py
  df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
  ```

  Do not forger the parenthesis around each condition.

  From this data structure consider the `occupation` column.

  ```py
  df['occupation']
  ```

  Pandas returns a series you can analyze with the `value_counts()` function.

  ```py
  df['occupation'].value_counts()
  ```

  To obtain the most frequent occupation, since the occupations represent the index of the series, access the value with `idxmax()`

  ```py
  df['occupation'].value_counts().idxmax()
  ```

  An alternative solution is through the `describe()` function. Here you'd consider the most frequent observation with the `top` property.

  ```py
  df['occupation'].describe().top
  ```
