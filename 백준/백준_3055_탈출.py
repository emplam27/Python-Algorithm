import sys

sys.stdin = open('input.txt', 'r')

from collections import deque


def hedgehog_move(start):
    hedgehog_path = [[0] * C for _ in range(R)]
    queue = deque()
    queue.append(start)
    hedgehog_path[start[0]][start[1]] = 1
    while queue:
        r, c, value = queue.popleft()
        for d in range(4):
            nr, nc = r + dy[d], c + dx[d]
            if 0 <= nr < R and 0 <= nc < C and hedgehog_path[nr][nc] == 0 and ground[nr][nc] != 'X':
                if ground[nr][nc] == 'D':
                    return value + 1
                elif ground[nr][nc] == '.':
                    queue.append([nr, nc, value + 1])
                    hedgehog_path[nr][nc] = 1
                    continue
                elif ground[nr][nc] > value + 1:
                    queue.append([nr, nc, value + 1])
                    hedgehog_path[nr][nc] = 1
    return 'KAKTUS'


def water_move(water):
    water_path = [[0] * C for _ in range(R)]
    queue = deque(water)
    for i, j, k in water:
        water_path[i][j] = 1
    while queue:
        r, c, value = queue.popleft()
        water_path[r][c] = 1
        for d in range(4):
            nr, nc = r + dy[d], c + dx[d]
            if 0 <= nr < R and 0 <= nc < C and water_path[nr][nc] == 0 and ground[nr][nc] == '.':
                queue.append([nr, nc, value + 1])
                ground[nr][nc] = value + 1
                water_path[nr][nc] = 1


R, C = map(int, input().split())
ground = [list(input()) for _ in range(R)]
dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]
# . : 비어있는곳, * : 물이 차있는곳, S : 고슴도치 위치, X : 돌, D : 비버굴,


# 시작 위치, 끝위치, 물 위치찾기 찾기
start, end, water = None, None, []
for r in range(R):
    for c in range(C):
        if ground[r][c] == 'S':
            start, ground[r][c] = [r, c, 0], '.'
        elif ground[r][c] == '*':
            water.append([r, c, 0])
            ground[r][c] = 0

# 함수실행
water_move(water)
print(hedgehog_move(start))
