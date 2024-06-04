import numpy as np
matrix = np.loadtxt("input.txt", delimiter=',', dtype=np.int64)
print(f"Minimum: {np.min(matrix)}\nMaximum: {np.max(matrix)}\nSumm: {np.sum(matrix)}")
        
