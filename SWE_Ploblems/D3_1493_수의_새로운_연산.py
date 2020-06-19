import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T + 1):
    M, N = map(int, input().split())

    board = [[0] * 300 for _ in range(300)]
    cnt = 1

    # k값을 설정해놔야한다.
    for k in range(1, 300):
        # j는 1부터 시작해서 x값으로 끝나야 하고, i는 x부터 시작해서 1로 끝나야한다.
        for x in range(1, k + 1):
            i = k - x + 1
            j = x
            board[i][j] = cnt

            cnt += 1
    for i in range(300):
        print(*board[i])

    # 좌표구하기
    for i in range(1, 300):
        for j in range(1, 300):
            if board[i][j] == M:
                M_d = (j, i)
            if board[i][j] == N:
                N_d = (j, i)

    # 숫자구하기



    # print('#%d' %t, )


