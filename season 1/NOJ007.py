def manipulation(strs):
   minsubstr = strs[0]
   for subStr in strs:
       if len(subStr) < len(minsubstr):
           minsubstr = subStr
   for subStr in strs:
       if subStr == minsubstr:
           continue
       for i in range(len(minsubstr)):
           if subStr[i] == minsubstr[i]:
               i = i + 1
           elif i == 0:
               return 0
           else:
               minsubstr = minsubstr[:i]
               break
   return minsubstr


x = int(input())
a = []
for i in range(x):
    a.append(input())
if manipulation(a) == 0:
    print("None")
else:
    print(manipulation(a))
