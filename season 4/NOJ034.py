def dist(str1, str2):
    dist = [[i+j for j in range(len(str2)+1)]for i in range(len(str1)+1)]
    for i in range(1, len(str1)+1):
        for j in range(1, len(str2)+1):
            if str1[i-1] == str2[j-1]:
                d = 0
            else:
                d = 1
            dist[i][j] = min(dist[i-1][j]+1, dist[i][j-1]+1, dist[i-1][j-1]+d)
    return dist[len(str1)][len(str2)]
x = "python"
y = input()
print(dist(x, y))

