import numpy
r_c = int(input())
print(r_c)
a = int(input())
b = int(input())
ret = input()[2:-2]
ret = ret.split('],[')
for i in range(len(ret)):
    ret[i] = [int(x) for x in ret[i].split(',')]

for i in range(len(ret)):
    if r_c == 0:
        temp = ret[a][i]
        ret[a][i] = ret[b][i]
        ret[b][i] = temp
    else:
        temp = ret[i][a]
        ret[i][a] = ret[i][b]
        ret[i][b] = temp

print(numpy.fromiter(ret[0],int))