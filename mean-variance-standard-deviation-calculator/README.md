# Mean-Variance-Standard Deviation Calculator

## Links

- [Assignment](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/mean-variance-standard-deviation-calculator)

- [Solution](https://replit.com/@borntofrappe/boilerplate-mean-variance-standard-deviation-calculator)

## Preface

The assignment asks to create a `calculate()` function which uses Numpy to display the mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix.

**Input**: a list of 9 digits

**Output**: a dictionary with the desired metrics

The list of 9 digits is first converted to a 3 by 3 array, so that the dictionary should include three values for each metric, for both axes and for all elements together.

```py
{
  'mean': [axis1, axis2, flat],
  'variance': [axis1, axis2, flat],
  'standard deviation': [axis1, axis2, flat],
  'max': [axis1, axis2, flat],
  'min': [axis1, axis2, flat],
  'sum': [axis1, axis2, flat]
}
```

As per the assignment:

- raise a `ValueError` exception with the message: "List must contain nine numbers." if the list contains less than 9 elements

- return the metrics in lists, **not** NumPy arrays
