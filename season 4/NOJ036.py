import re
import functools

def print_list(l):
    for x in l:
        if x == l[-1]:
            end = ""
        else:
            end = " "
        print(x, end=end)


n, x = [int(x) for x in re.split(" ", input())]
list1 = [int(x) for x in re.split(" ", input())]

cmp = lambda a, b: -1 if abs(a - x) < abs(b - x) else 1 if abs(a - x) > abs(b - x) else 0

list1 = sorted(list1, key=functools.cmp_to_key(cmp))

print_list(list1)
