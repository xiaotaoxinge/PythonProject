n = int(input())
count = 2 * (n - 1) + 1
for i in range(1,n+1):
    for j in range(1,i):
        count = count + 10 ** j
print(count)