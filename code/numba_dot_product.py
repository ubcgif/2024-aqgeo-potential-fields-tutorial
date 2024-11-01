import numba
import numpy as np


def dot_product_slow(matrix, x):
    nrows, ncols = matrix.shape
    result = np.zeros(nrows, dtype=np.float64)
    for i in range(nrows):
        for j in range(ncols):
            result[i] += matrix[i][j] * x[j]
    return result


@numba.jit(nopython=True)
def dot_product(matrix, x):
    nrows, ncols = matrix.shape
    result = np.zeros(nrows, dtype=np.float64)
    for i in range(nrows):
        for j in range(ncols):
            result[i] += matrix[i][j] * x[j]
    return result


size = 300
rng = np.random.default_rng(seed=42)
a = rng.random(size=(size, size))
x = rng.random(size=size)

dot_product(a, x)

# %timeit dot_product_slow(a, x)
# %timeit dot_product(a, x)
