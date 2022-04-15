from datetime import datetime, timedelta
y1, m1, d1 = input().split(' ')
y2, m2, d2 = input().split(' ')
print(abs((datetime(int(y1), int(m1), int(d1)) - datetime(int(y2), int(m2), int(d2))).days))
