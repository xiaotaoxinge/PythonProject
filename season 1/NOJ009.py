def judge(substr):
    strs = []
    for i in range(len(substr)):
        strs.append(int(substr[i]))
    return all(strs)


if __name__ == '__main__':
    N = int(input())
    lists = []
    for i in range(N):
        lists.append(bin(int(input()))[2:])
    for i, substr in enumerate(lists):
        if i == len(lists)-1:
            print(judge(substr), end="")
        else:
            print(judge(substr), end=",")
