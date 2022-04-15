import numpy as np
x = np.array([int(x) for x in input()[1:-1].split(',')])
ave = sum(x)/len(x)
print('*******',ave)
x = x[np.where(x > ave)]
print(x)
y = np.zeros((len(x),1),dtype=int)
x = x + y
print(x)