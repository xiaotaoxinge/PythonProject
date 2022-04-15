import numpy as np
x = [float(x) for x in input()[1:-1].split(',')]
x1 = [int(x) for x in input()[1:-1].split(',')]
x = [int(i) for i in x]
x.sort()
x = list(set(x))
x = [i for i in x if i not in x1]
ave = sum(x)/len(x)
y = [abs(i-ave) for i in x]
mi = min(y)
print(y.index(mi))