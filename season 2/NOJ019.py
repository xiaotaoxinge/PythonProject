x = input().split(',')
x = [int(i) for i in x]
x.sort()
i = 0
print("{",end='')
while i < len(x):
    if i + x.count(x[i]) == len(x):
        print(x[i],x.count(x[i]),sep=': ',end='}')
    else:
        print(x[i],x.count(x[i]),sep=': ',end=', ')
    i += x.count(x[i])
