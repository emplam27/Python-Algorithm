import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    New_board = [[0] * N for _ in range(N)]

    cnt = 0

    for i in range(N):
        sum_num = 0
        for j in range(N):
            if board[i][j] == 1:
                sum_num += 1
            if board[i][j] == 0:
                if sum_num == K:
                    cnt += 1
                sum_num = 0
        if sum_num == K:
            cnt += 1
        sum_num = 0

    for i in range(N):
        sum_num = 0
        for j in range(N):
            if board[j][i] == 1:
                sum_num += 1
            if board[j][i] == 0:
                if sum_num == K:
                    cnt += 1
                sum_num = 0
        if sum_num == K:
            cnt += 1
        sum_num = 0

    print('#%d' %t, cnt)