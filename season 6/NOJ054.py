n,m = (int(x) for x in input().split(' '))
s = []
for i in range(n):
    s.append([int(x) for x in input().split(' ')])

for_1 = []
def find_father(dic,fin):
    if dic[fin[0]][fin[1]] == fin:
        return fin
    else:
        return find_father(dic,dic[fin[0]][fin[1]])
for i in range(n):
    for j in range(m):
        if s[i][j] == 1:
            s[i][j] = [i,j]
            for_1.append(s[i][j])

for k in range(len(for_1)-1):
    for l in range(k+1,len(for_1)):
        if abs(for_1[k][0] - for_1[l][0]) + abs(for_1[k][1] - for_1[l][1]) == 1:
            if find_father(s,for_1[k]) == for_1[k]:
                s[for_1[k][0]][for_1[k][1]] = find_father(s,for_1[l])
            else:
                s[for_1[l][0]][for_1[l][1]] = find_father(s,for_1[k])

sum = 0
for i in range(len(for_1)):
    if find_father(s,for_1[i]) == for_1[i]:
        sum += 1
print(sum)
