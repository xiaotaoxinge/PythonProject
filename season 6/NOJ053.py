n = int(input())
m = int(input())
line = []
for i in range(m):
    s = [int(x) for x in input().split(' ')]
    if s[0] == 1:
        if len(line) == n:
            print('False')
        else:
            print('True')
            line.append(s[1])
    elif s[0] == 2:
        if len(line) == 0:
            print(-1)
        else:
            print(line[0])
            del line[0]
