import numpy as np


url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')
uniques = np.unique(iris, return_counts=True)
for i in range(len(uniques[0])):
    print(f'{uniques[0][i]} - {uniques[1][i]} repeats')

