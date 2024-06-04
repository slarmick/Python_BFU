import numpy as np


a = np.reshape(np.random.normal(size=40), (10,4))
print(a, '\n')
print(f'Minimum = {np.min(a)}\nMaximum = {np.max(a)}\nAverage = {np.mean(a)}\nDeviation = {np.std(a)}')