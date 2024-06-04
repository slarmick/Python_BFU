import numpy as np


def maxAfterZero(array):
    result = np.max(array[1:][x[:-1] == 0])
    return result


x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0])
print(maxAfterZero(x))
