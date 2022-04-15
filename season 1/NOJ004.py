def select_maxnum(num, hex):
    if hex == 2:
        tmp = int(num, 2)
    elif hex == 8:
        tmp = int(num, 8)
    elif hex == 10:
        tmp = num
    elif hex == 16:
        tmp = int(num, 16)
    return tmp


a = input()
b = input()
c = input()
d = input()
maxnum = max(int(select_maxnum(a, 2)), int(select_maxnum(b, 8)), int(select_maxnum(c, 10)), int(select_maxnum(d, 16)))
print(bin(maxnum), oct(maxnum), maxnum, hex(maxnum), sep=',')
