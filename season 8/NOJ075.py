import pandas as pd
dic = {'plus':'+','power':'**','minus':'-','multiply':'*','divide':'/'}
n = int(input())
data=[]
idx = [x for x in range(n)]
column = ['Num1','Num2','Op']
for i in range(n):
    li = input().split(' ')
    # for j in range(2):
    #     li[j] = int(li[j])
    data.append(li)

df = pd.DataFrame(data,index=idx,columns=column)

result = []
for index,row in df.iterrows():
    result.append(eval(row['Num1']+dic[row['Op']]+row['Num2']))
df['result'] = result
print(df)