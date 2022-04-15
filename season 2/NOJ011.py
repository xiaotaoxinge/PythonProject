def judge(num):
    if num % 100 != 0:
        if num % 4 == 0:
            return 366
        else:
            return 365
    else:
        if num % 400 == 0:
            return 366
        else:
            return 365

if __name__ == '__main__':
    year = int(input())
    print(judge(year))