import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())

    board = [[0] * (N+1) for _ in range(N+1)]     # 가로세로 1씩 크게하여 인덱스와 입력좌표를 맞춘다.

    # 중간 4개돌 놓기
    half_N = N // 2
    board[half_N][half_N], board[half_N + 1][half_N + 1] = 2, 2
    board[half_N][half_N + 1], board[half_N + 1][half_N] = 1, 1

    # 변화량을 저장하는 델타
    # 상, 우상, 우, 우하, 하, 좌하, 좌, 좌상 순서
    dr = [-1, -1, 0, 1, 1, 1, 0, -1]
    dc = [0, 1, 1, 1, 0, -1, -1, -1]

    for i in range(M):
        c, r, color = map(int, input().split())
        # 8방향에 돌 놓기위한 반복문
        for j in range(8):
            # 각 방향별로 뒤집히는 돌이 있는지 검사하는 반복문
            nc = c
            nr = r
            while True:
                nc = nc + dc[j]
                nr = nr + dr[j]
                # 만약에 판의 범위를 벗어나면 안되므로 조건문 작성, 판을 1칸 늘려줬기 때문에 고려.
                if nr <= 0 or nr > N or nc <= 0 or nc > N:
                    break
                elif board[nr][nc] == 0:  # 0이면 뒤집을 수 없음
                    break
                # 설정한 방향으로 진행하다가 같은색이 나오면, 원래 내자리로 돌아올 때 까지 뒤집기
                elif board[nr][nc] == color:
                    while not (nr == r and nc == c):    # 다시 돌아가는데, 초기좌표랑 다를때까지 색을 바꾸면서 조건문을 반복
                        nr = nr - dr[j]
                        nc = nc - dc[j]
                        board[nr][nc] = color
                    break   # 돌이 있는지 검사하는 while 문 끝내기

    for i in range(N):
        print(*board[i])

    cnt1 = 0
    cnt2 = 0
    for i in range(N+1):
        for j in range(N+1):
            if board[i][j] == 1:
                cnt1 += 1
            elif board[i][j] == 2:
                cnt2 += 1

    print('#%d' % t, cnt1, cnt2)
