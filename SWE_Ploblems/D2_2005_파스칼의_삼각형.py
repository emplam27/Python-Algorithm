import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T + 1):
    N = int(input())

    board = [[0] * N for _ in range(N)]

    # 1, 2 번째 케이스 구현하기
    board[0][0] = 1

    if N >= 2:
        board[1][0], board[1][1] = 1, 1

    # 3번째 이상 파스칼 삼각형 구현하기
    for i in range(2, N):
        board[i][0], board[i][i] = 1, 1
        for j in range(N-1):
            board[i][j + 1] = board[i-1][j] + board[i-1][j+1]

    # 문자열로 변경하기
    print('#%d' % t)
    for i in range(N):
        for j in range(N):
            if board[i][j] != 0:
                print(board[i][j], end=' ')
            if j % N == N -1:
                print()

