s = input()
if len(s) <= 1:
   s = int(s)
   lens = 1
else:
   s = [int(x) for x in s.split(' ')]
   lens = len(s)
position = [0]*lens
i = 1
position[0]=1
x = 0
while(not all(position)):

   if position[x] % 2 == 1:
      x = s[x]
   else:
      x = (x+1)%lens
   position[x] += 1
   i += 1
i -= 1
print(i)
