s = list(input())
n = int(input())
s_re = [s[-i] for i in range(1,len(s)+1)]
def ED(a_str, b_str):
    lea = []
    lea_0 = list(range(len(b_str) + 1))

    lea.append(lea_0)
    for i in range(1, len(a_str) + 1):
        lea_i = [i if x == 0 else 0 for x in range(len(b_str) + 1)]
        lea.append(lea_i)

    for i in range(1, len(a_str) + 1):
        for j in range(1, len(b_str) + 1):
            dist_1 = lea[i - 1][j] + 1
            dist_2 = lea[i][j - 1] + 1
            dist_3 = lea[i - 1][j - 1] + (1 if a_str[i - 1] != b_str[j - 1] else 0)
            lea[i][j] = min(dist_1, dist_2, dist_3)

    return lea[-1][-1]

# print(s,s_re)
# print(ED(s,s_re))
# print(ED(s_re,s))
if ED(s,s_re) <= n:
    print('True')
else:
    print('False')
