def narcissistic(num):
    if (int(num[0])) ** 3 + (int(num[1])) ** 3 + (int(num[2])) ** 3 == int(num):
        print(int(num))
    else:
        return

if __name__ == '__main__':
    x = 100
    while x < 1000:
        narcissistic(str(x))
        x += 1