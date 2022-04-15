import functools
n = int(input())
s = [int(x) for x in input().split(' ')]
s_l = []
for i in range(n):
    s_l.append(s[2*i:2*i+2])
s_l.sort(key = functools.cmp_to_key(lambda a,b:-1 if a[0]<b[0] else 0))
star = 0
while(star < len(s_l)-1):
    if max(s_l[star][0],s_l[star+1][0]) <= (min(s_l[star][1],s_l[star+1][1])):
        s_l[star][0] = min(s_l[star][0],s_l[star+1][0])
        s_l[star][1] = max(s_l[star][1],s_l[star+1][1])
        del s_l[star+1]
    else:
        star += 1

for i in range(len(s_l)):
    if i == len(s)-1:
        print(s_l[i][0],end=' ')
        print(s_l[i][1])
    else:
        print(s_l[i][0],end=' ')
        print(s_l[i][1],end=' ')