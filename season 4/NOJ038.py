n, m = (int(x) for x in input().split(' '))
children = [0]*n
s = 1
while m > 0:
    for i in range(n):
        rem = m
        m -= s
        if m > 0:
            children[i] += s
            s += 1
        else:
            children[i] += rem
            break
for i in range(len(children)-1):
    print(children[i], end=' ')
print(children[len(children)-1])
