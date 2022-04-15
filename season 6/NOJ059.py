s = [int(x) for x in input().split(' ')]
s.sort()
i = 0
try:
    while (1):
        if s[i] == s[i + 1]:
            del s[i:i + 2]
            i = i - 1
        else:
            pass
        i += 1

except Exception:
    print(s)
