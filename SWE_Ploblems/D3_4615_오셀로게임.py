import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    board = [[0] * (N+1) for _ in range(N+1)]

    # 가운데 4곳에 돌 놓기
    half_N = N // 2
    board[half_N][half_N], board[half_N + 1][half_N + 1] = 2, 2
    board[half_N + 1][half_N], board[half_N][half_N + 1] = 1, 1

    # 델타 설정하기
    # 상 우상 우 우하 하 좌하 좌 좌상
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]
    dx = [0, 1, 1, 1, 0, -1, -1, -1]

    for i in range(M):
        c, r, color = map(int, input().split())
        # 8 방향으로 오셀로 검사하기
        board[r][c] = color
        for direct in range(8):
            nr = r
            nc = c
            while True:
                nr = nr + dy[direct]
                nc = nc + dx[direct]
                if nr <= 0 or nc <= 0 or nr > N or nc > N:
                    break
                if board[nr][nc] == 0:
                    break
                if board[nr][nc] == color:
                    while not (nr == r and nc == c):
                        nr = nr - dy[direct]
                        nc = nc - dx[direct]
                        board[nr][nc] = color
                    break
    for i in range(N):
        print(*board[i])
