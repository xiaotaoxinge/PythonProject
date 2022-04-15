import numpy as np

n = eval(input())

mat = np.zeros((n, n), dtype=np.int)
row, col = np.diag_indices_from(mat)
mat [row, col] = np.arange(2, n + 2)
mat = np.pad(mat, (1, 1), 'constant', constant_values=(0, 0))
mat = mat[:-1, 1:]
mat = np.pad(mat, (1, 1), 'constant', constant_values=(-1, -1))
print(mat)
