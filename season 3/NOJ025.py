import math


def judge(num):
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            return 0
    return 1

if __name__ == '__main__':

    count = 0
    for i in range(100,201):
        if judge(i):
            count += i
    print(count)