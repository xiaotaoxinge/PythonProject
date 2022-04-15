x = input().split(',')
x = [int(i) for i in x]
y = int(input())
try:
    print(x.index(y))
except ValueError:
    x.append(y)
    x.sort()
    print(x.index(y))
