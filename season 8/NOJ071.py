import pandas as pd
import numpy as np
n = int(input())
idx = [x for x in range(n*5)]
column = ['Mon','Part','Num','Price']
data = []
for i in range(n*5):
    li = input().split(' ')
    for i in range(2,4):
        li[i] = int(li[i])
    data.append(li)
df = pd.DataFrame(data,index=idx,columns=column)
print(df)
table1 = pd.pivot_table(df, values='Price', index='Mon',
                        columns='Part', aggfunc=np.sum)
table2 = pd.pivot_table(df,values='Price',index='Mon',columns='Part',aggfunc=np.sum)
print(table1)
print(table2)