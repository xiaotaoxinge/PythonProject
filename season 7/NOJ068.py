import numpy as np
n = int(input())
a = []
for i in range(0,11-n):
    li = [x for x in range(i,i+n)]
    a.append(li)
a = np.array(a)
print(a)