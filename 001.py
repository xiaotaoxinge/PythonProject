# try:
#     a = input()
#     b = input()
#     c = input()
#     exec("d= "+ a + c + b)
#     print("{}{}{}={}".format(a,c,b,d))
# except Exception:
#     print("ERROR")

# m = str(bin(int(input())))
# n = int(input())
# m = [x for x in m]
# del m[:2]
# m = [int(x) for x in m]
# y = [0]*n
# if n <= len(m):
#     pass
# else:
#     del y[:len(m)]
#     m= y + m
# for i in range(len(m)):
#     print(m[i],end='')


# x = []
# x +=[int(input(),2),int(input(),8),int(input()),int(input(),16)]
# x = max(x)
# print("{},{},{},{}".format(bin(x),oct(x),x,hex(x)))


#回文数
# n = int(input())
# a = []
# for i in range(n):
#     a.append(input())
# for j in range(n):
#     if a[j] == a[j][::-1]:
#         if j == n-1:
#             print("True")
#         else:
#             print("True",end=',')
#     else:
#         if j == n-1:
#             print('False')
#         else:
#             print("False",end=',')


#加密
# a = int(input())
# b = int(input())
# c = int(input())
# x = '0'*3
# a = (a+b)%c
# print(str(a) + x)



#最长公共字符串
# n = int(input())
# x = []
# for i in range(n):
#     x.append(input())
# min_len = min([len(i) for i in x])
# for j in range(min_len):
#     jud = 0
#     for i in range(n):
#         if x[0][j] != x[i][j]:
#            jud = 1
#            break       
#     if jud == 1:
#         break
#     else:
#         print(x[0][j],end='')

# ##复数
# a = complex(input())
# b = complex(input())
# print(a+b,end=',')
# print(a-b,end=',')
# print(a*b,end=',')
# print(a/b,end=',')
# print(a.conjugate(),end=',')
# print(abs(a),end=',')



##是否全由1组成###
# a = bin(int(input()))
# a = str(a)[2:]
# a = [int(x) for x in a]
# print(all(a))



######罗马数字#########
#    3



#################  判断是否二进制全1   ##############
# n = int(input())
# a = []
# for i in range(n):
#     a.append(str(bin(int(input()))))
#     a[i] = a[i][2:]
#     a[i] = [int(x) for x in a[i]]
# for j in range(n):
#     if all(a[j]):
#         if j != n-1:
#             print('True',end=',')
#         else:
#             print('True')
#     else:
#         if j != n-1:
#             print('False',end=',')
#         else:
#             print('False')





########  立方  #########
# a = []
# for i in range(1,11):
#     a.append(i**3)
# print(a)





# s = input()
# s = s.split(' ')
# sum = 0
# for i in range(len(s)):  
#     y = s[i].split('.')
#     if len(y)== 2 and y[0].isdigit() and y[1].isdigit():
#         sum += float(s[i])
#         s[i] = float(s[i])
#     if len(y)==1 and y[0].isdigit():
#         sum += int(s[i])
#         s[i] = int(s[i])
# print(s)
# print(sum)

########????????  问张臭猪   ######




########    弧长    #######
# from math import pi,sin,cos,tan
# y = float(input())
# x1 = y * pi /180
# x2 = sin(x1) + cos(x1) - (tan(x1/4))**2
# print('%.4f' % x1)
# print('%.4f' % x2)
############################



#######   查找  插入   #####
# s = input()
# x = float(input())
# s = s.split(',')
# s = [float(x) for x in s]
# if x in s:
#     print(s.index(x))
# else:
#     s.append(x)
#     s.sort()
#     print(s.index(x))



########  输出列表    #########
# print([x**3 for x in range(11)])

##############################



##########  列表的内置操作函数    #####

# s = input().split(' ')
# s = [int(x) for x in s]
# s1 = [abs(x) for x in s]
# print('{},{},{},{}'.format(len(s),max(s),min(s),sum(s)))
# print(s1)

###########################




########## 元组 ##########
# a = input().split(' ')
# a = [int(x) for x in a]
# b = [0]*len(a)
# for i in range(len(a)):
#     b[i] = a[i] + a[-(i+1)]
# c = tuple(b)
# print(c)
######################





############# 成绩转换   ###########
# a = float(input())
# if a>=90 and a<=100:
#     b='A'
# elif a>=80 and a<90:
#     b='B'
# elif a >=70 and a<80:
#     b='C'
# elif a>=60 and a<70:
#     b='D'
# else:
#     b='E'
# print(b)

##################################




###############  今年多少天  #############
# a = int(input())
# if a%4 == 0:
#     if a%100 == 0:
#         if a%400 == 0:
#             b = 366
#         else:
#             b = 365
#     else:
#         b = 366
# else:
#     b = 365
# print(b)
#########################################




###############  重复数字   #############

# s = input().split(',')
# s1 = list(set(s))
# s1.sort()
# a = {i:s.count(i) for i in s1}
# print(a)
######################################






############  水仙花数  ##############
# for i in range (100,1000):
#     y = map(int,str(i))
#     su = [x**3 for x in y]
#     su = sum(su)
#     if su == i:
#         print(i)
######################################





############  长城凸起  ##############

# s = input().split(' ')
# s = [int(x) for x in s]
# lens = []
# start = 0
# end = 0
# for i in range(1,len(s)-1):
#     jug = 0
#     for j in range(0,i):
#         sub = s[j:i+1]
#         if sub == sorted(sub):
#             jug += 1
#             start = j
#             break
#     if jug == 1:
#         for j in range(i+1,len(s)):
#             sub = s[i:j+1]
#             if sub != sorted(sub,reverse=True):
#                 if j!=i:
#                     jug += 1
#                     end = j
#                     break
#     if jug == 2:
#         lens.append(end-start)
# print(max(lens))

######################################








##############   素数累加求和   ########
# sum=0
# for i in range(100,201):
#     for j in range(2,i):
#         if i%j == 0:
#             sum += i
#             break
# print(sum)

####   ?????????????????????????????????????                          ????????????????
######################






##############  字符统计   ##############
# s1 = input().split(' ')
# s=''
# for i in range(len(s1)):
#     s += s1[i]
# s = list(s)

# s = [ord(x) for x in s]
# for i in range(len(s)):
#     if s[i] < 60:
#         s[i] = 1
#     elif s[i] > 96:
#         s[i] = 2
#     else:
#         s[i] = 3
# for j in range(3):
#     print(s.count(s[0]),end=',')
#     s.remove(s[0])

#########################################








############# 数字规律相加   ################
# n = int(input())
# sum = 2*(n-1) + 1
# for i in range(1,n+1):
#     for j in range(1,i):
#         sum = sum + 10**j
# print(sum)

#####################################





##########  列表中不相邻整数和的最大值 ########
# s = input().split(' ')
# l = [int(x) for x in s]
# m = 0
# for i in range(len(l)):
#     if i == 0:
#         l1 = l[2:]
#     elif i == len(l)-1:
#         l1 = l[:-2]
#     else:
#         l1 = l[:i-1] + l[i+2:]
#     p = l[i] + max(l1)
#     if p > m:
#         m = p
# print(m)
#####################################







###############   水上石阶   ############
# def sss(n):
#     if n == 1 :
#         return 1
#     elif n == 2:
#         return 2 
#     else:
#         return sss(n-1) + sss(n-2)

# n = int(input())
# print(sss(n))
# ####################################






# #############  神奇的计算   #########
# l = [0]*5
# sum = 0
# for h in range(1,10):
#     l[0] = h
#     for i in range(1,10):
#         if i in l:
#             continue
#         else:
#             l[1] = i
#             for j in range(1,10):
#                 if j in l:
#                     continue
#                 else:
#                     l[2] = j
#                     for k in range(1,10):
#                         if k in l:
#                             continue
#                         else:
#                             l[3] = k
#                             for m in range(1,10):
#                                 if m in l:
#                                     continue
#                                 else:
#                                     l[4] = m
                               
#                                 p = (l[0]*100 + l[4]*10 + l[1]) * (l[2]*10 + l[3])
                                
#                                 p1 = (l[0]*10 + l[1]) * (l[2]*100 + l[4]*10 + l[3])
                               
#                                 if p == p1:
#                                     sum = sum+1
#                             l[4] = 0
#                     l[3] = 0
#             l[2] = 0
#     l[1] = 0
# print(sum)
############################################################







############   三个忍者   #############
# s1 = input().split(' ')
# s1 = [int(x) for x in s1]
# s1.sort()
# s2 = input().split(' ')
# s2 = [int(x) for x in s2]
# s2.sort()
# sum = 0
# for i in range(len(s1)-2):  
#     for j in range(i+2,len(s1)):
#         if s1[j] - s1[i] > s2[2] :
#             break
#         else:
#             for k in range(i+1,j):
#                 if s1[k]-s1[i] > s2[1]:
#                     break
#                 else:
#                     if s1[j]-s1[k] <= s2[0]:
#                         sum += 1
#                     elif s1[k]-s1[i] <= s1[0] and s1[j]-s1[k] <= s2[1]:
#                         sum += 1
#                     else:
#                         continue
        
# print(sum)
#####################################




####################   解方程   ################
# n = float(input())   
# x = 1.0   
# m=2   
# s = 0       
# while abs(x**2 - n) > 0.0001:

#     s = s + x**2-n
#     x = x - (x**2 - n)/s
#     m += 1
    
# print('%.4f'% abs(x))

###############################################





###################    旋转矩阵   ############################
# n = int(input())
# m = []
# for i in range(n):
#     s = input().split(' ')
#     s = [int(x) for x in s]
#     m.append(s)

# for i in range(n):
#     for j in range(i+1):
#         p = m[i][j]
#         m[i][j] = m[j][i]
#         m[j][i] = p
# for i in range(n//2):
#     for j in range(n):
#         p = m[i][j]
#         m[i][j] = m[n-1-i][j]
#         m[n-1-i][j] = p
# for i in range(n):
#     for j in range(n):
#         if j == n-1:
#             print(m[i][j])
#         else:
#             print(m[i][j],end=' ')







###################  python的编辑距离  #######################
# def cal_dis(s,s1):
#     l = len(s)
#     str1 = s.split()
#     str2 = s1.split()
#     for i in range(len(s1)):
#         for j in range(s.count(s1[i])):
#             s[s.find(s1[i])] = i

#     m = []
#     for k in range(len(s)):
#         if s[k].isdigit():
#             m.append[[k,s[k]]]
#     a = []
#     b = []





############   数列求和  ######################
# n = int(input())
# sum = 0
# for i in range(n+1):
#     sum += i
# print(sum)






############   n的平方和立方   ###############
# n = int(input())
# print(n**2)
# print(n**3)







#########  斐波那契数  ######
# n = int(input())

# def fbnc(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return (fbnc(n-1) + fbnc(n-2))
    
# print(fbnc(n))



##########   使用lambda 函数    ##############


# f = lambda s: eval(s)
          
# s1 = input()
# print(f(s1))



########## sort 与 lambda 函数  ###########
# import re 
# import functools 

# def print_list(l):
#     for x in l:
#         if x == l[-1]:
#             end = ""
#         else:
#             end= " "
#         print(x, end=end)

# n, x = [int(x) for x in re.split(" ", input())]
# list1 = [int(x) for x in re.split(" ", input())]

# cmp = lambda a, b: -1 if abs(a - x) < abs(b - x) else 1 if abs(a -x )> abs(b - x) else 0

# list1 = sorted(list1, key=functools.cmp_to_key(cmp))

# print_list(list1)



########################### 闭包实现计数器  #########
# def outer(x):
#     def inner():
#         nonlocal x
#         x += 1
#         return x   
#     return inner

# a = outer(0)
# for i in range(5):
#    print(a())



#################    lambda  ####### 
# f = lambda s: eval(s)
# s = input()
# a = f(s)
# print('%d' % a)




######   找下标   #############
# s = input().split(' ')
# x = input()
# try:
#     print(s.index(x))
# except Exception:
#     print(-1)



########       分发水果    #############
# n,m =(int(x) for x in input().split(' '))
# child_hand = [0]*n
# turn_num = 1
# while(m>0):
#     for i in range(n):
#         rem = m
#         m = m-turn_num
#         if m>0:
#             child_hand[i] += turn_num
#             turn_num += 1
#         else:
#             child_hand[i] += rem
#             break
# for i in range(len(child_hand)):
#     if i == len(child_hand)-1:
#         print(child_hand[i])
#     else:
#         print(child_hand[i],end=' ')
        



# n = int(input())
# sum = 0
# for i in range(1,n+1):
#     sum += i
# print(sum)





######### 合并区间  ############
# import functools 
# n = int(input())
# s = [int(x) for x in input().split(' ')]
# s_l = []
# for i in range(n):
#     s_l.append(s[2*i:2*i+2])
# s_l.sort(key = functools.cmp_to_key(lambda a,b:-1 if a[0]<b[0] else 0))
# star = 0
# while(star < len(s_l)-1):
#     if max(s_l[star][0],s_l[star+1][0]) <= (min(s_l[star][1],s_l[star+1][1])):
#         s_l[star][0] = min(s_l[star][0],s_l[star+1][0])
#         s_l[star][1] = max(s_l[star][1],s_l[star+1][1])
#         del s_l[star+1]
#     else:
#         star += 1
        
# for i in range(len(s_l)):
#     if i == len(s)-1:
#         print(s_l[i][0],end=' ')
#         print(s_l[i][1])
#     else:
#         print(s_l[i][0],end=' ')
#         print(s_l[i][1],end=' ')




# letter = 1
# while(letter < len(s)-2):
#     letter2 = letter + 2
#     while(letter2 < len(s)):
#         if max(s[letter-1],s[letter2-1]) <= min(s[letter],s[letter2]):
#             s[letter-1] = min(s[letter-1],s[letter2-1])
#             s[letter] = max(s[letter],s[letter2])
#             del s[letter2-1:letter2+1]
#         else:
#             letter2 += 2
#     letter += 2

# for i in range(len(s)):
#     if i == (len(s)- 1):
#         print(s[i])
#     else:
#         print(s[i],end=' ')







###########  转换大小写   #############



# class String_class:
    
#     si = 'no string'
#     def __init__(self) -> None:
#         pass

#     def getstring(self):
#         self.si = input()       
#     def printstring(self):
      
#         print(self.si.upper())

# string = String_class()
# string.getstring()
# string.printstring()


####### 简单计算   ##############
# s = input().split(' ')
# s1 = ''
# for i in range(len(s)):
#     s1 = s1 + s[i]
# b = eval(s1)
# print('%d' % b)


####   实例计数   ##############
# class Person:
#     count = 0

#     def __init__(self):
#         Person.count += 1
# for i in range(5):
#     x = Person()    
# print(Person.count)




#######   重叠面积   #######
# tr1 = [int(x) for x in input().split(' ')]
# tr2 = [int(x) for x in input().split(' ')]
# def isoverlap(x11,x12,x21,x22):
#     if max(x11,x21) < min(x12,x22):
#         return 1
#     else:
#         return 0

# if isoverlap(tr1[0],tr1[2],tr2[0],tr2[2]) and isoverlap(tr1[3],tr1[1],tr2[3],tr2[1]):
#     x = max(tr1[0],tr2[0]) - min(tr1[2],tr2[2])
#     y = max(tr1[3],tr2[3]) - min(tr1[1],tr2[1])
#     sq = x * y
# else:
#     sq = 0
# print(sq)


#### 是否在圆内  #######
# s = [int(x) for x in input().split(' ')]
# dis = (s[2]-s[0])**2 + (s[3]-s[0])**2
# if dis <= s[4]**2:
#     print(1)
# else:
#     print(-1)


######  朋友圈   #######
# n = int(input())
# m = int(input())
# query = [[0]*2]*m
# for i in range(m):
#     query[i] = [int(x) for x in input().split(' ')]
# support = [[0]*n]*n
# for j in range(m):
#     support[query[j][0]][query[j][1]] = 1

# support1 = [[-1]*2]
# for i in range(n):
#     for j in range(n):
#         if support[i][j] == 1:
#             jug = 0
#             link = [0]*2
#             for k in range(len(support1)):
#                 if i in support1[k] or j in support1[k]:
#                     link[jug] = k
#                     jug += 1
#             if jug == 0:
#                 support1.append([i,j])
#             elif jug == 1:
#                 support1[link[0]].extend([i,j])
#             elif jug == 2:
#                 support1[link[0]].extend([i,j,support1[link[1][0]],support1[link[1][1]]])
#                 del support1[link[1]]
#             else:
#                 pass

# print(len(support1))



######## 朋友圈  2   ###########
# n = int(input())
# m = int(input())
# def find_father(n,s):
#     if s[n] == n:
#         return n
#     else:
#         return find_father(s[n],s)
# s = [i for i in range(n)]
# for i in range(m):
#     link = [int(x) for x in input().split(' ')]
#     if s[link[0]] == link[0]:
#         s[find_father(link[0],s)] = s[find_father(link[1],s)]
#     else:
#         # print(find_father(link[0]),find_father(link[1]))
#         s[find_father(link[1],s)] = s[find_father(link[0],s)]
# print(s)
# sum = 0
# for j in range(n):
#     if s[j] == j:
#         sum+=1
# print(sum)
 ###################################### 




########### 阶乘   ##############
# def jc(n):
#     if n == 1:
#         return 1
#     else:
#         return n*jc(n-1)
    
# n = int(input())
# print(jc(n))



#########  实现栈   ################



# class stack:
#     sta = []
#     stitch = -1
#     def __init__(self):
#         pass
#     def push(self,x):
#         self.sta.append(x)
#         self.stitch += 1
#     def pop(self):
#         if self.stitch == -1:
#             pass
#         else:
#             del self.sta[self.stitch]
#             self.stitch -= 1
    
# stack1 = stack()
# try:
#     jug = 1
#     while(jug):
#         op = input()
#         op1 = op[:]
#         op = op.split(' ')
#         if op[-1] == '':
#             del op[-1]
#         op = [int(x) for x in op]   
#         if op[0] == 1:
#             stack1.push(op[1])
#         elif op[0] == 2:
#             stack1.pop()

    
# except EOFError:
#     if stack1.stitch == -1:
#             print('None')
#     else:
#         for i in range(stack1.stitch+1):
#             if i != stack1.stitch:
#                 print(stack1.sta[i],end=' ')
#             else:
#                 print(stack1.sta[i])
#     pass


########   计算  bmi  #############
# from  math import floor 
# class Person:
#     name = 0
#     weight = 0
#     height = 0
#     gender = 0

#     def __init__(self,name,weight,height,gender):
#         self.name = name
#         self.weight = weight
#         self.height = height
#         self.gender = gender
#     def bmi(self):
#         if self.gender == 'female':
#             b = (self.height-70) * 6//10
#         else:
#             b = (self.height-80) * 7//10
#         print(b)
        

# s = input().split(' ')
# P = Person(s[0],int(s[1]),int(s[2]),s[3])
# P.bmi()      




# # ###########   计算  时间   间隔    ###########
# s1 = [int(x) for x in input().split(' ')]
# s2 = [int(x) for x in input().split(' ')]
# def year(a):
#     if a%4 == 0:
#         if a%100 == 0:
#             if a%400 == 0:
#                 b = 366
#             else:
#                 b = 265
#         else:
#             b = 366
#     else:
#         b = 365
#     return b

# def month(mon,yer):
#     if mon in [1,3,5,7,8,10,12]:
#         return 31
#     elif mon == 2:
#         if year(yer) == 366:
#             return 29
#         else:
#             return 28
#     else:
#         return 30
# d1 = d2 = 0
# for i in range(3):
#     if s1[i] > s2[i]:
#         d1 += (i+1)**2
#     elif s1[i] == s2[i]:
#         pass
#     else:
#         d2 += (i+1)**2
# if d1 >= d2:
#     max = s1
#     min = s2
# else:
#     max = s2
#     min = s1
# sum = 0
# if max[0] - min[0] > 1:
#     if year(min[0]) and (min[1] > 2 and min[2] < 29 or min[1] == 2 and min[0] == 29):
#         if min[0] == 29:
#             min[0] = 28
#         sum -= 1
# for i in range(min[0],max[0]):
#     print(i)
#     sum += year(i)
# min[0] = max[0] -1
# while(min != max):
#     while(1):
#         if min[1] == 13:
#             break
#         else:
#             while(1):
#                 sum += 1
#                 if min[2] >= month(min[1],min[0]):
#                     min[2] = 0
#                     break
#                 else:
#                     min[2] += 1
                    
#                     if max == min:
#                         break                    
#             if max == min:
#                 break
#             min[1] += 1
#     if max == min:
#         break       
#     min[0] += 1
    
# print(sum)




#######   最接近成功的三个人你  #########

# s = [int(x) for x in input().split(' ')]
# n = int(input())
# s.sort()
# sum = 0
# for i in range(len(s)-2):
#     for j in range(i+1,len(s)-1):
#         if s[j]+s[i] > n:
#             break
#         else:
#             for k in range(j+1,len(s)):
#                 if s[i]+s[j]+s[k] >= n:
#                     break
#                 else:
#                     sum += 1
# print(sum)


#########  1奇异数   ############
# s = [int(x) for x in input().split(' ')]
# s.sort()
# i = 0
# try:
#     while(1):
#         if s[i] == s[i+1]:
#             del s[i:i+2]
#             i = i-1
#         else:
#             pass
#         i += 1
        
# except Exception:
#     print(s)

########  合并 升序列表  ################
# s1 = [int(x) for x in input().split(' ')]
# s2 = [int(x) for x in input().split(' ')]
# s1.extend(s2)
# s1.sort()
# for i in range(len(s1)):
#     if i != len(s1)-1:
#         print(s1[i],end=' ')
#     else:
#         print(s1[i])



##########  更高  温度    ##############
# s = [int(x) for x in input().split(' ')]
# for i in range(len(s)-1):
#     for j in range(i+1,len(s)+1):
#         if j == len(s):
#             s[i] = 0
#             break
#         else:
#             if s[j] > s[i]:
#                 s[i] = j-i
#                 break
#             else:
#                 pass
# s[-1] = 0
# for i in range(len(s)):
#     if i != len(s)-1:
#         print(s[i],end=' ')
#     else:
#         print(s[i])





########  数组实现队列  ########
# n = int(input())
# m = int(input())
# line = []
# for i in range(m):
#     s = [int(x) for x in input().split(' ')]
#     if s[0] == 1:
#         if len(line) == n:
#             print('False')
#         else:
#             print('True')
#             line.append(s[1])
#     elif s[0] == 2:
#         if len(line) == 0:
#             print(-1)
#         else:
#             print(line[0])
#             del line[0]



#########  和为指定数值的  字数组  #########
# s = [int(x) for x in input().split(' ')]
# x = int(input())
# sum = 0
# for i in range(len(s)-1):
#     for j in range(i,len(s)):
#         sum0 = 0
#         for k in range(i,j+1):
#             sum0 += s[k]
#         if sum0 == x:
#             sum += 1
#         else:
#             pass
# print(sum)


########## 无重复  数组   ############
# s = [int(x) for x in input().split(' ')]
# s = list(set(s))
# print(len(s))





############   矩阵  集群数     ##########

# n,m = (int(x) for x in input().split(' '))
# s = []
# for i in range(n):
#     s.append([int(x) for x in input().split(' ')])    

# for_1 = []
# def find_father(dic,fin):
#     if dic[fin[0]][fin[1]] == fin:
#         return fin
#     else:
#         return find_father(dic,dic[fin[0]][fin[1]])
# for i in range(n):
#     for j in range(m):
#         if s[i][j] == 1:
#             s[i][j] = [i,j]
#             for_1.append(s[i][j])

# for k in range(len(for_1)-1):   
#     for l in range(k+1,len(for_1)):        
#         if abs(for_1[k][0] - for_1[l][0]) + abs(for_1[k][1] - for_1[l][1]) == 1:
#             if find_father(s,for_1[k]) == for_1[k]:
#                 s[for_1[k][0]][for_1[k][1]] = find_father(s,for_1[l])
#             else:
#                 s[for_1[l][0]][for_1[l][1]] = find_father(s,for_1[k])

# sum = 0
# for i in range(len(for_1)):
#     if find_father(s,for_1[i]) == for_1[i]:
#         sum += 1
# print(sum)




###########   计算  字符串  编辑距离   ###########



# s = input()
# s_stand = 'python'

# rout = [[0]*len(s) for x in range(len(s_stand))]
# first = 1 
# if s.find(s_stand[0]) != -1:
#     x = s.find(s_stand[0])
#     for k in range(x,len(s)):
#         rout[0][k] = -1
# if s_stand.find(s[0]) != -1:
#     x = s_stand.find(s[0])
#     for k in range(x,len(s_stand)):
#         rout[k][0] = -1

# for j in range(len(s_stand)):
#     rout[j][0] += j + first 
# for i in range(len(s)):
#     rout[0][i] += i + first
# if s[0] == s_stand[0]:
#     rout[0][0] = 0

# def fc(i,j,dic):
#     if (i<len(s_stand)) and (j<len(s)):   
#         if s_stand[i] == s[j]:
#             dic[i][j]=min(dic[i-1][j-1],dic[i-1][j],dic[i][j-1])
#         else:
#             dic[i][j]=min(dic[i-1][j-1],dic[i-1][j],dic[i][j-1])+1
# # for i in range(1,len(s_stand)):
# #     for j in range(1,len(s)):
# #         fc(i,j,rout)

# b = rout[len(s_stand)-1][len(s)-1]
# print(b)


# s = input()
# s0 = 'python'

# def fc(i,j,rout,s0,s):
#     if i == 0 and j == 0:
#         rout[i][j] == 0
        
#     elif (i == 0 and j>0) or (j == 0 and i>0):
#         rout[i][j] = max([i,j])
#     else:
#         if s0[i-1] == s[j-1]:
#             rout[i][j] = min([fc(i-1,j,rout,s0,s),fc(i,j-1,rout,s0,s),fc(i-1,j-1,rout,s0,s)])
#         else:
#             rout[i][j] = min([fc(i-1,j,rout,s0,s),fc(i,j-1,rout,s0,s),fc(i-1,j-1,rout,s0,s)]) + 1
#     return rout[i][j]
# rout = [[0]*(len(s)+1) for x in range(len(s0)+1)]

# fc(len(s0),len(s),rout,s0,s)

# print(rout)
# print(rout[len(s0)][len(s)])


#########  回文字符串   ########
# s = list(input())
# n = int(input())
# s_re = [s[-i] for i in range(1,len(s)+1)]
# def ED(a_str, b_str):
#     lea = []
#     lea_0 = list(range(len(b_str) + 1))

#     lea.append(lea_0)
#     for i in range(1, len(a_str) + 1):
#         lea_i = [i if x == 0 else 0 for x in range(len(b_str) + 1)]
#         lea.append(lea_i)

#     for i in range(1, len(a_str) + 1):
#         for j in range(1, len(b_str) + 1):
#             dist_1 = lea[i - 1][j] + 1
#             dist_2 = lea[i][j - 1] + 1
#             dist_3 = lea[i - 1][j - 1] + (1 if a_str[i - 1] != b_str[j - 1] else 0)
#             lea[i][j] = min(dist_1, dist_2, dist_3)

#     return lea[-1][-1]

# print(s,s_re)
# print(ED(s,s_re))
# print(ED(s_re,s))
# if ED(s,s_re) <= n:
#     print('True')
# else:
#     print('False')




   # 编辑距离  ####
# def ED(a_str, b_str="acedcba"):
#     lea = []
#     lea_0 = list(range(len(b_str) + 1))

#     lea.append(lea_0)
#     for i in range(1, len(a_str) + 1):
#         lea_i = [i if x == 0 else 0 for x in range(len(b_str) + 1)]
#         lea.append(lea_i)

#     for i in range(1, len(a_str) + 1):
#         for j in range(1, len(b_str) + 1):
#             dist_1 = lea[i - 1][j] + 1
#             dist_2 = lea[i][j - 1] + 1
#             dist_3 = lea[i - 1][j - 1] + (1 if a_str[i - 1] != b_str[j - 1] else 0)
#             lea[i][j] = min(dist_1, dist_2, dist_3)

#     return lea[-1][-1]


# s = input()
# print(ED(s))


# s = list(input())
# n = int(input())
# s_re = [s[-i] for i in range(1,len(s)+1)]

# def fc(i,j,rout,s0,s):
#     if i == 0 and j == 0:
#         rout[i][j] == 0
        
#     elif (i == 0 and j>0) or (j == 0 and i>0):
#         rout[i][j] = max([i,j])
#     else:
#         if s0[i-1] == s[j-1]:
#             rout[i][j] = min([fc(i-1,j,rout,s0,s),fc(i,j-1,rout,s0,s),fc(i-1,j-1,rout,s0,s)])
#         else:
#             rout[i][j] = min([fc(i-1,j,rout,s0,s),fc(i,j-1,rout,s0,s),fc(i-1,j-1,rout,s0,s)]) + 1
#     return rout[i][j]
# rout = [[0]*(len(s)+1) for x in range(len(s)+1)]

# fc(len(s),len(s),rout,s_re,s)

# print(rout)
# print(rout[len(s)][len(s)])



# s = list(input())
# s1 = [[0] for i in range(1,len(s)+1)]


# import random
# s = [i for i in range(0,5)]

# random.shuffle(s)
# print(s)




   #####    环球旅行   ####s
# s = input()
# if len(s) <= 1:
#    s = int(s)
#    lens = 1
# else:
#    s = [int(x) for x in s.split(' ')]
#    lens = len(s)
# position = [0]*lens
# i = 1
# position[0]=1
# x = 0
# while(not all(position)):

#    if position[x] % 2 == 1:
#       x = s[x]
#    else:
#       x = (i+1)//lens
#    position[x] += 1
#    i += 1
# i -= 1
# print(i)



# s = [int(x) for x in input().split(' ')]
# position = [0]*len(s)
# i = 0
# x = 0
# while(not all(position)):
#    position[x] += 1
#    if position[x] % 2 == 1:
#       x = s[x]
#    else:
#       x = (i+1)//len(s)
#    i += 1
# i -= 1
# print(i)



# from datetime import date
# x = [int(x) for x in input().split(' ')]
# y = [int(x) for x in input().split(' ')]
# x = date(x[0],x[1],x[2])
# y = date(y[0],y[1],y[2])

# if x.__ge__(y):
#    sub = x.__sub__(y).days
# else:
#    sub = y.__sub__(x).days

# print(sub)





# s1 = input().split(' ')
# s=''
# for i in range(len(s1)):
#     s += s1[i]
# s = list(s)

# s = [ord(x) for x in s]
# for i in range(len(s)):
#     if s[i] < 60:
#         s[i] = 1
#     elif s[i] > 96:
#         s[i] = 2
#     else:
#         s[i] = 3
# for j in range(3):
#     print(s.count(s[0]),end=',')
#     s.remove(s[0])

# s = list(input())
# l = [0]*3
# for i in range(len(s)):
#    if ord(s[i]) == 32:
#       del s[i]
#    elif ord(s[i]) >= 48 and ord(s[i]) <= 57:
#       s[i] = 0
#    elif ord(s[i]) >= 65 and ord(s[i]) <= 90:
#       s[i] = 1
#    else:
#       s[i] = 2
   
# sort = [0]*3
# for i in range(3):
#    sort[i] = s.index(i)
# sort.sort()
# for i in range():
#    print()


# s = [int(x) for x in input().split(',')]
# s1 = s[:]
# s1 = list(set(s1))
# s1.sort()
# a = {i:s.count(i) for i in s1}
# print(a)
# try:
#    b = 'data error!'
#    a = float(input())
   
#    if a>=90 and a<=100:
#       b='A'
#    elif a>=80 and a<90:
#       b='B'
#    elif a >=70 and a<80:
#       b='C'
#    elif a>=60 and a<70:
#       b='D'
#    elif a>=0 and a<60:
#       b='E'
#    else:
#       pass
#    print(b)

# except Exception:
#    print(b)



# sum=0
# for i in range(100,201):
#    jud = 0
#    for j in range(2,i):
#       if i%j == 0:
#          jud = 1
#          break
#    if jud ==0:
#       sum += i
# print(sum)
# s1 = [0]*3
# s = input().split(' ')
# s = [ord(x) for x in s]
# for i in range(len(s)):
#     if s[i] < 60:
#         s[i] = 1
#     elif s[i] > 96:
#         s[i] = 2
#     else:
#         s[i] = 3
# for j in range(3):
#     print(s.count(s[0]),end=' ')
#     s.remove(s[0])

# s1 = [0]*3
# s = [ord(x) for x in input()]
# for i in range(len(s)):
#    if s[i] in range(65,91):
#       s1[0]+=1
#    elif s[i] in range(97,123):
#       s1[1]+=1
#    elif s[i] in range(48,58):
#       s1[2]+=1
# print(s1[0],end=' ')
# print(s1[1],end=' ')
# print(s1[2])

try:
   s = input().split(' ')
   s = [int(x) for x in s]
   lens = []
   start = 0
   end = 0
   for i in range(1,len(s)-1):
      jug = 0
      for j in range(0,i):
         sub = s[j:i+1]
         if sub == sorted(sub):
               jug += 1
               start = j
               break
      if jug == 1:
         for j in range(i+1,len(s)):
               sub = s[i:j+1]
               if sub != sorted(sub,reverse=True):
                  if j!=i:
                     jug += 1
                     end = j
                     break
      if jug == 2:
         lens.append(end-start)
   print(max(lens))

except Exception:
   print(0)
