import numpy as np


def encode(arr):
    tmp = np.r_[True,arr[:-1]!=arr[1:],True]
    return (arr[tmp[:-1]], np.diff(np.flatnonzero(tmp)))


a = np.array([2, 2, 3, 3, 3, 1, 1, 5, 5, 2, 3, 3])
print(encode(a))