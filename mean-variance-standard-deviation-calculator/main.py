import numpy as np


def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")

    a = np.array(list).reshape(3, 3)

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

    return {
        'mean': mean,
        'variance': var,
        'standard deviation': std,
        'max': max,
        'min': min,
        'sum': sum,
    }


# print(calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]))
print(calculate([0, 1, 2, 3, 4, 5, 6, 7]))
