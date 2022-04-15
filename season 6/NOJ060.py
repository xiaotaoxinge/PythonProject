l = input().split(' ')
n, pre, i = None, None, 0
for j in range(len(l)):
    n = l[i]
    if n == pre:
        del l[i]
        i -= 1
    else:
        pre = n

    if i >= len(l) - 1:
        break
    i += 1

print(len(l))
