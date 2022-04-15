tr1 = [int(x) for x in input().split(' ')]
tr2 = [int(x) for x in input().split(' ')]


def isoverlap(x11,x12,x21,x22):
    if max(x11,x21) < min(x12,x22):
        return 1
    else:
        return 0


if isoverlap(tr1[0],tr1[2],tr2[0],tr2[2]) and isoverlap(tr1[3],tr1[1],tr2[3],tr2[1]):
    x = max(tr1[0],tr2[0]) - min(tr1[2],tr2[2])
    y = max(tr1[3],tr2[3]) - min(tr1[1],tr2[1])
    sq = x * y
else:
    sq = 0
print(sq)
