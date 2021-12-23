import numpy as np


def calculate(list):
    if len(list) < 9:
        # https://docs.python.org/3/tutorial/errors.html#raising-exceptions
        raise ValueError("List must contain nine numbers.")

    # https://numpy.org/doc/stable/user/basics.creation.html#converting-python-sequences-to-numpy-arrays
    # reshape in a matrix 3 by 3
    a = np.array(list).reshape(3, 3)

    # store the information in lists
    # include lists instead of numpy arrays
    # https://numpy.org/doc/stable/reference/generated/numpy.ndarray.tolist.html
    mean = [
        np.mean(a, axis=0).tolist(),
        np.mean(a, axis=1).tolist(),
        np.mean(a)
    ]

    var = [
        np.var(a, axis=0).tolist(),
        np.var(a, axis=1).tolist(),
        np.var(a)
    ]

    std = [
        np.std(a, axis=0).tolist(),
        np.std(a, axis=1).tolist(),
        np.std(a)
    ]

    max = [
        np.max(a, axis=0).tolist(),
        np.max(a, axis=1).tolist(),
        np.max(a)
    ]

    min = [
        np.min(a, axis=0).tolist(),
        np.min(a, axis=1).tolist(),
        np.min(a)
    ]

    sum = [
        np.sum(a, axis=0).tolist(),
        np.sum(a, axis=1).tolist(),
        np.sum(a)
    ]

    # return a dictionary
    return {
        'mean': mean,
        'variance': var,
        'standard deviation': std,
        'max': max,
        'min': min,
        'sum': sum,
    }


print(calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]))
