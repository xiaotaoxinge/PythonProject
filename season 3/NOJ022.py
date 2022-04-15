x = input().split(' ')
x = [int(i) for i in x]
y = input().split(' ')
y = [int(i) for i in y]
count = 0
for i in range(len(x)-2):
    for j in range(i+1,len(x)-2):
        for k in range(j+1,len(x)-2):
            if abs(x[i]-x[j]) <= y[0] and abs(x[i]-x[k]) <= y[1] and abs(x[j]-x[k]) <= y[2]:
                print(x[i],x[j],x[k])
                count += 1

print(count)