import sys

sys.stdin = open('input.txt', 'r')


def bfs(depth, list_bfs):
    global max_depth
    if depth >= max_depth:
        for k in list_bfs:
            result.append((depth, k))
        max_depth = depth

    tmp = []
    for i in list_bfs:
        visited[i] = 1

    for i in list_bfs:
        for j in range(max_num + 1):
            if mat[i][j] == 1 and visited[j] == 0:
                tmp.append(j)

    if len(tmp) > 0:
        bfs(depth + 1, tmp)
    else:
        return


T = 10
for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    max_num = max(arr)
    mat = [[0] * (max_num + 1) for _ in range(max_num + 1)]
    visited = [0] * (max_num + 1)

    for i in range(0,  N,  2):
        mat[arr[i]][arr[i + 1]] = 1

    max_depth, max_n = 0, 0
    result = []
    bfs(0, [M])

    tmp = []
    for i, j in result:
        if i == max_depth:
            tmp.append(j)

    print('#%d' %t, max(tmp))

#1 17
#2 96
#3 49
#4 39
#5 49
#6 1
#7 28
#8 45
#9 59
#10 64

