import sys

sys.stdin = open("input.txt", "r")


def dfs(v, sum_num):
    global min_num

    if v == N:
        if sum_num < min_num:
            min_num = sum_num
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] += 1
            sum_num += arr[v][i]
            if sum_num > min_num:
                visited[i] -= 1
                sum_num -= arr[v][i]
                continue
            dfs(v + 1, sum_num)
            visited[i] -= 1
            sum_num -= arr[v][i]
    return


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    min_num = 100000000000

    dfs(0, 0)

    print('#%d' % t, min_num)