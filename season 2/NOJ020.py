x = input().split()
x = [int(i) for i in x]
print(len(x),end=',')
print(max(x),end=',')
print(min(x),end=',')
print(sum(x))
for i in range(len(x)):
    x[i] = abs(x[i])
x.sort()
print(x)