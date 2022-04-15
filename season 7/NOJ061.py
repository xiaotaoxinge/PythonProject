from math import sqrt


def distance(x, y, p):
    if x[0] == y[0]:
        return abs(p[0] - x[0])
    elif x[1] == y[1]:
        return abs(y[1] - p[1])
    a = (x[1] - y[1]) / (x[0] - y[0])
    b = y[1] - a * y[0]
    dis = abs(a * p[0] - p[1] + b) / sqrt(a ** 2 + 1)
    return dis


x = input()
y = input()
if len(x) <= 5:
    x = x[1:-1]
    y = y[1:-1]
    x = [int(x) for x in x.split(',')]
    y = [int(x) for x in y.split(',')]
    x = [x]
    y = [y]

else:
    x = x[2:-2]
    y = y[2:-2]
    x = x.split('],[')
    y = y.split('],[')
    for i in range(len(x)):
        x[i] = [int(x) for x in x[i].split(',')]
        y[i] = [int(x) for x in y[i].split(',')]

p = input()[1:-1]
p = [int(x) for x in p.split(',')]

print("[", end='')
for i in range(len(x) - 1):
    dis = distance(x[i], y[i], p)
    print(dis, end=',')
print(distance(x[-1], y[-1], p), end='')
print("]")