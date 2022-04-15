import numpy as np

mat = np.array(eval(input()))

print((mat - mat.mean()) / mat.std())