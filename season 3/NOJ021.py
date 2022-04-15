x = input()
uppercase,lowercase,number = 0,0,0
for i in x:
    if(i.isupper()):
        uppercase += 1
        continue
    elif(i.islower()):
        lowercase += 1
        continue
    elif(i.isdigit()):
        number += 1
        continue
print(uppercase,end=' ')
print(lowercase,end=' ')
print(number)