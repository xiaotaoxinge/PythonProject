count = 0
for x in range(1,10):
    for y in range(1,10):
        if y == x:
            continue
        else:
            for z in range(1,10):
                if z == y or z == x:
                    continue
                else:
                    for m in range(1,10):
                        if m == z or m == x or m == y:
                            continue
                        else:
                            for n in range(1,10):
                                if n == z or n == x or n == y or n == m:
                                    continue
                                else:
                                    if (x * 10 + y) * (z * 100 + m * 10 + n) == (x * 100 + m * 10 + y) * (z * 10 + n) :
                                        count += 1
print(count)