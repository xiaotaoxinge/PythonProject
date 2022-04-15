x = []
x.extend(input().split(' '))
x = [int(i) for i in x]
max_num = x[0]
for i in range(len(x)-2):
    for j in range(i+2,len(x)):
        if x[i] + x[j] > max_num:
            max_num = x[i] + x[j]
print(max_num)
