s = [int(x) for x in input().split(' ')]
n = int(input())
s.sort()
sum = 0
for i in range(len(s)-2):
    for j in range(i+1,len(s)-1):
        if s[j]+s[i] > n:
            break
        else:
            for k in range(j+1,len(s)):
                if s[i]+s[j]+s[k] >= n:
                    break
                else:
                    sum += 1
print(sum)
