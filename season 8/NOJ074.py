import pandas as pd
column1 = ['Name','Sex','Age']
column2 = ['Name','Weight','Height']
n = int(input())
idx1 = [x for x in range(n)]

data1 = []
for i in range(n):
    data1.append(input().split(' '))
m = int(input())
idx2 = [x for x in range(m)]
data2 = []
for j in range(m):
    data2.append(input().split(' '))

df1 = pd.DataFrame(data1,index=idx1,columns=column1)
df2 = pd.DataFrame(data2,index=idx2,columns=column2)
print(df1)
print(df2)

df = pd.merge(df1,df2,how='outer')
print(df)