n = int(input())
m = []
for i in range(n):
    s = input().split(' ')
    s = [int(x) for x in s]
    m.append(s)

for i in range(n):
    for j in range(i+1):
        p = m[i][j]
        m[i][j] = m[j][i]
        m[j][i] = p
for i in range(n//2):
    for j in range(n):
        p = m[i][j]
        m[i][j] = m[n-1-i][j]
        m[n-1-i][j] = p
for i in range(n):
    for j in range(n):
        if j == n-1:
            print(m[i][j])
        else:
            print(m[i][j],end=' ')