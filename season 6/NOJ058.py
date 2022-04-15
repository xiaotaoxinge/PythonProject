s = [int(x) for x in input().split(' ')]
x = int(input())
sum = 0
for i in range(len(s)-1):
    for j in range(i,len(s)):
        sum0 = 0
        for k in range(i,j+1):
            sum0 += s[k]
        if sum0 == x:
            sum += 1
        else:
            pass
print(sum)
