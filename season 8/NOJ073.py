import pandas as pd
n = int(input())
obj = [x for x in input().split(' ')]
idx = []
data = []
for i in range(n):
    stu = input().split(' ')
    for i in range(1,len(stu)):
        stu[i] = int(stu[i])
    idx.append(stu[0])
    data.append(stu[1:])
score = pd.DataFrame(data,index=idx,columns=obj)
score.info()
print(score.describe())
