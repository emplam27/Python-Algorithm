import sys

# sys.stdin = open("2468_input.txt", "r")
sys.setrecursionlimit(10000)


def dfs(r, c):
    # 4방향으로 돌면서 가능한곳 dfs
    # 결과적으로 안전구역 하나를 다 칠해주는 용도
    visited[r][c] = 1
    for i in range(4):
        nr = r + dy[i]
        nc = c + dx[i]
        if 0 <= nr < N and 0 <= nc < N and mat[nr][nc] > depth and visited[nr][nc] == 0:
            dfs(nr, nc)
    return 1


N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]

# 최대 높이를 구하기
max_depth = 0
min_depth = 0
for i in range(N):
    for j in range(N):
        if mat[i][j] > max_depth:
            max_depth = mat[i][j]
        if mat[i][j] < min_depth:
            min_depth = mat[i][j]

# 우 하 좌 상
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

# 물의 높이가 증가하게 하면서 탐색
max_cnt = 0
for depth in range(min_depth, max_depth + 1):
    cnt = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if mat[i][j] > depth and visited[i][j] == 0:
                if dfs(i, j) == 1:
                    cnt += 1
    if cnt > max_cnt:
        max_cnt = cnt

print(max_cnt)

