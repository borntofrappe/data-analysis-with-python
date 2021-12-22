# Mean-Variance-Standard Deviation Calculator

## Links

- [Assignment](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/mean-variance-standard-deviation-calculator)

- [Repl](https://replit.com/@borntofrappe/boilerplate-mean-variance-standard-deviation-calculator)

## Preface

The assignment asks to create a function named `calculate()` that uses Numpy to display the mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix.

**Input**: a list containing 9 digits

**Output**: a dictionary containing the desired metrics

The list of 9 digits is first converted in a 3 by 3 array, so that each metric describes the value for each of the axis and the value for the flattened the array.

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

If a list containing less than 9 elements is passed into the function, it should raise a `ValueError` exception with the message: "List must contain nine numbers."

The values in the returned dictionary should be lists and not Numpy arrays.
