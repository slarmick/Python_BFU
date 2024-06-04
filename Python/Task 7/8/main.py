import numpy as np
import scipy


def ln_multivariate_normal(x: np.array, m: np.array, c: np.array) -> np.array:
  quad_form = np.einsum('ij,ij->i', x - m, np.dot(np.linalg.inv(c), x - m))
  ln = -0.5 * (np.log(2 * np.pi) + np.log(np.linalg.det(c)) + quad_form)
  return ln


def using_scipy(x: np.array, m: np.array, c: np.array) -> np.array:
    return scipy.stats.multivariate_normal(m, c).logpdf(x)


X = np.array([[2, 4], [6, 5]])
M = np.array([0, 0])
C = np.array([[1, 0.7], [0.7, 2]])
print(f"The result of my function is: {ln_multivariate_normal(X, M, C)}")
print(f"The result of SciPy function is: {using_scipy(X, M, C)}")
print(f"Difference between those two answers is {(using_scipy(X, M, C)[0]/ln_multivariate_normal(X, M, C)[0]-1)*100}%.")