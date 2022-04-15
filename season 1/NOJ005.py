def parlindromic_number():
    y = input()
    if ''.join(reversed(y)) == y:
        return "True"
    else:
        return "False"


x = int(input())
list1 = []
while x > 0:
    list1.append(parlindromic_number())
    x -= 1

print(','.join(list1))
