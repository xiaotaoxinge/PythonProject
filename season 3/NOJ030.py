def stone_steps(n):
    if n == 1 :
        return 1
    elif n == 2:
        return 2
    else:
        return stone_steps(n-1) + stone_steps(n-2)

if __name__ == '__main__':

    n = int(input())
    print(stone_steps(n))