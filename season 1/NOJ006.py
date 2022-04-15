# def encryption(x, y, z):
#     x = str((x + y) % z)
#     x_= x.zfill(4)
#     print(''.join(reversed(x_)))


x = int(input())
y = int(input())
z = int(input())
x = str((x + y) % z)
x_ = x.zfill(4)
print(''.join(reversed(x_)))
# encryption(x, y, z)