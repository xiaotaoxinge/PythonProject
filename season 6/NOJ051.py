s = [int(x) for x in input().split(' ')]
for i in range(len(s)-1):
    for j in range(i+1, len(s)+1):
        if j == len(s):
            s[i] = 0
            break
        else:
            if s[j] > s[i]:
                s[i] = j-i
                break
            else:
                pass
s[-1] = 0
for i in range(len(s)):
    if i != len(s)-1:
        print(s[i], end=' ')
    else:
        print(s[i])
