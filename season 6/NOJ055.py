s1 = [int(x) for x in input().split(' ')]
s2 = [int(x) for x in input().split(' ')]
s1.extend(s2)
s1.sort()
for i in range(len(s1)):
    if i != len(s1)-1:
        print(s1[i],end=' ')
    else:
        print(s1[i])
