n = float(input())
x = 1.0
m=2
s = 0
while abs(x**2 - n) > 0.0001:

    s = s + x**2-n
    x = x - (x**2 - n)/s
    m += 1

print('%.4f'% abs(x))