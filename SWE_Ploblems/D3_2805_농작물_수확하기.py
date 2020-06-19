import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    arr = [str(input()) for _ in range(N)]
    board = [[0] * N for _ in range(N)]

    # board에 arr값을 넣어준다.
    for i in range(N):
        for j in range(N):
            board[i][j] = int(arr[i][j])

    # 마름모꼴로 나가면서 더해준다.
    # r = 0, c =             m
    # r = 1, c =        m-1, m , m+1
    # r = 2, c =   m-2, m-1, m, m+1, m+2
    # r = 3, c =        m-1, m , m+1
    # r = 4, c =             m
    sum = 0
    m = N // 2
    for r in range(N):
        for c in range(N):
            if (abs(m - r)) <= c <= ((N - 1) - abs(m - r)):
                sum += board[r][c]

    print('#%d' %t, sum)
