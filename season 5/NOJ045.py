n = int(input())
m = int(input())
query = [[0]*2]*m
for i in range(m):
    query[i] = [int(x) for x in input().split(' ')]
support = [[0]*n]*n
for j in range(m):
    support[query[j][0]][query[j][1]] = 1

support1 = [[-1]*2]
for i in range(n):
    for j in range(n):
        if support[i][j] == 1:
            jug = 0
            link = [0]*2
            for k in range(len(support1)):
                if i in support1[k] or j in support1[k]:
                    link[jug] = k
                    jug += 1
            if jug == 0:
                support1.append([i,j])
            elif jug == 1:
                support1[link[0]].extend([i,j])
            elif jug == 2:
                support1[link[0]].extend([i,j,support1[link[1][0]],support1[link[1][1]]])
                del support1[link[1]]
            else:
                pass

print(len(support1))

