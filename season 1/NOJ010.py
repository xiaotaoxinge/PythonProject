def roman_num(num):
    count = 0
    conversion = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in range(len(num)):
        if i < len(num)-1:
            if conversion[num[i]] >= conversion[num[i+1]]:
                count += conversion[num[i]]
            else:
                count -= conversion[num[i]]
                i += 2
        else:
            count += conversion[num[i]]
    return count

if __name__ == '__main__':
    N = int(input())
    lists = []
    for i in range(N):
        lists.append(input())
    for i in range(N):
        if i == N-1:
            print(roman_num(lists[i]))
        else:
            print(roman_num(lists[i]), end=",")
