str1=[int(x) for x in input().split()]
len1=len(str1)
flag=0
for len2 in range(3,len1+2)[::-1]:
    #l2起始点
    for i in range(len1-len2+1):
        #l2终点
        j=i+len2
        str2=str1[i:j]
        for k in range(len2-1):
            if str2[k]>=str2[k+1]:
                flag1=k
                break
        for k in range(1,len2)[::-1]:
            if str2[k]>=str2[k-1]:
                flag2=k
                break
        if flag1 == flag2:
            print(len2)
            flag=1
            break
    else:
        continue
    break
if flag==0:
    print('0')
