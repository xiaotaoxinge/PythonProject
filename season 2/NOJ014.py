import math

x = int(input())
y = math.radians(x)
count = math.sin(y) + math.cos(y) - math.tan(y/4.)**2
print("%.4f"%y)
print("%.4f"%count)