# Mean-Variance-Standard Deviation Calculator

Compute the mean, variance, standard deviation and other calculations for a 3 by 3 matrix.

## Links

- [Assignment](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/mean-variance-standard-deviation-calculator)

- [Solution](https://replit.com/@borntofrappe/boilerplate-mean-variance-standard-deviation-calculator)

## Solution

The assignment asks to create a `calculate()` function which uses Numpy to display the different operations.

The function receives as input a list of 9 digits, and returns a dictionary with the desired metrics.

The list of 9 digits is first converted to a 3 by 3 array, so that the dictionary includes three values for each metric, for both axes and for all elements together.

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

Immediately the assignment asks to raise an exception when the input list contains less than 9 elements. This feat is achieved with Python and the `raise` statement.

```py
if len(list) < 9:
    raise ValueError("List must contain nine numbers.")
```

Past the exception

- reshape the list into a 3 by 3 matrix

  ```py
  a = np.array(list).reshape(3, 3)
  ```

- compute the mean, variance and other relevant metrics with the associated functions. For instance and for the mean

  ```py
  np.mean(a)
  ```

  Without additional arguments NumPy considers all the elements. Per the assignment, the `axis` argument allows to compute the value relative to the columns or rows.

  ```py
  np.mean(a, axis=0)
  np.mean(a, axis=1)
  ```

  For each metric the three values are stored in a list.

  ```py
  mean = [
        np.mean(a, axis=0),
        np.mean(a, axis=1),
        np.mean(a)
    ]
  ```

  Per the assignment, however, convert the computations for the two axis from the value returned by NumPy, which is a numpy array. The assignment explictly ask to store the data in python lits.

  ```py
  mean = [
        np.mean(a, axis=0).tolist(),
        np.mean(a, axis=1).tolist(),
        np.mean(a)
    ]
  ```
