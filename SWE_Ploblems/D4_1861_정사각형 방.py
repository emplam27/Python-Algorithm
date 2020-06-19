import sys

sys.stdin = open("input.txt", "r")


def check(r, c):
    global max_count, min_index
    count = 1
    index = arr[r][c]
    while True:

        for d in range(4):
            nr = r + dy[d]
            nc = c + dx[d]
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == arr[r][c] + 1:
                r, c = nr, nc
                count += 1
                continue

        if max_count == count:
            if index < min_index:
                min_index = index
                max_count = count
        elif max_count < count:
            min_index = index
            max_count = count
        return


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]

    max_count = 0
    min_index = 1000000
    for i in range(N):
        for j in range(N):
            check(i, j)

    print('#%d' %t, min_index ,max_count)
