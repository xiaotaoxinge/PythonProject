import numpy as np
x = input()[1:-1].split(',')
x = [int(i) for i in x]
x = np.array(x)
x_max = x[np.where(x!=max(x))]
x_min = x[np.where(x!=min(x))]
x_ma = x_max
x_mi = x_min
if len(x_max) < len(x_min):
    x_ma = np.append(x_max,[-1]*(len(x_min)-len(x_max)))
elif len(x_max) > len(x_min):
    x_mi = np.append(x_max,[-1]*len(x_max)-len(x_min))

con = np.array((x_ma,x_mi))
print(x_max)
print(x_min)
print(con)