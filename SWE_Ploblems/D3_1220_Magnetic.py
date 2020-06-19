import sys

sys.stdin = open("input.txt", "r")

for t in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for j in range(N):
        if arr[0][j] == 0:
            arr[0][j] = 2
        for i in range(1, N):
            if arr[i][j] == 0:
                arr[i][j] = arr[i-1][j]

    cnt = 0
    for j in range(N):
        for i in range(1, N):
            if arr[i-1][j] == 1 and arr[i][j] == 2:
                cnt += 1

    print('#%d' % t, cnt)