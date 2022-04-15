x = []
x.extend(input().split())
tuple1 = tuple(x)
list1 = []
for i in range(len(tuple1)):
    list1.append(int(tuple1[i])+int(tuple1[-(i+1)]))
tuple2 = tuple(list1)
print(tuple2)