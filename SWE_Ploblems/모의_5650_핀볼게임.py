import sys

sys.stdin = open("../못푼문제/5650_input.txt", "r")


# 지정한 방향으로 가서 점수를 얻는 함수
def check(start_r, start_c, direct):
    global max_score
    score = 0
    r, c = start_r, start_c
    d = direct
    while True:
        nr = r + dy[d]
        nc = c + dx[d]

        # 벽을 만나 튕기는 조건
        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            score = score * 2 + 1
            break

        # 네모블럭을 만나 반대로 튕겨나가는 조건
        if board[nr][nc] == 5:
            score = score * 2 + 1
            break

        # 자리자리로 돌아와 종료되는 조건
        if nr == start_r and nc == start_c:
            break

        # 블랙홀을 만나 종료되는 조건
        if board[nr][nc] == -1:
            break

        # 빈공간을 지나가는 조건
        if board[nr][nc] == 0:
            r, c = nr, nc
            continue

        # 사선블록을 만나 방향이 꺾이거나 반대로 튕겨나가는 조건
        if board[nr][nc] == 1 or board[nr][nc] == 2 or board[nr][nc] == 3 or board[nr][nc] == 4:
            if d == board[nr][nc] % 4:
                d = (d + 1) % 4
                score += 1
                r, c = nr, nc
                continue
            elif d + 1 == board[nr][nc]:
                d = (d + 3) % 4
                score += 1
                r, c = nr, nc
                continue
            else:
                score = score * 2 + 1
                break

        # 웜홀을 만나 이동하는 조건
        if board[nr][nc] == 6 or board[nr][nc] == 7 or board[nr][nc] == 8 or board[nr][nc] == 9 or board[nr][nc] == 10:
            r, c = wormhole(board[nr][nc], nr, nc)
            continue

    if score > max_score:
        max_score = score


# 웜홀 함수
def wormhole(n, r, c):
    for h, i, j in wormhole_list:
        if h == n and (i, j) != (r, c):
            return i, j


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    dy, dx = [1, 0, -1, 0], [0,-1, 0, 1]  # 하 좌 상 우

    # 빈공간 리스트를 만들어준다.
    wormhole_list = list()
    for i in range(N):
        for j in range(N):
            if board[i][j] == 6 or board[i][j] == 7 or board[i][j] == 8 or board[i][j] == 9 or board[i][j] == 10:
                wormhole_list.append((board[i][j], i, j))

    # 빈공간을 순회하며 사방으로 공을 보낸후, 가장 높은 점수를 갱신시켜준다.
    max_score = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                for d in range(4):
                    check(i, j, d)

    print('#%d' %t, max_score)