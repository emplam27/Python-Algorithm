import sys

sys.stdin = open("input.txt", "r")


def check(idx, result):
    global max_result

    if result <= max_result:
        return

    if idx == N:
        if result > max_result:
            max_result = result
        return

    else:
        for i in range(N):
            if visited[i] == 0:
                visited[i] = 1
                check(idx + 1, result * (arr[idx][i] / 100))
                visited[i] = 0


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N

    max_result = 0
    check(0, 1)

    print('#{} {:0.6f}'.format(t, max_result * 100))