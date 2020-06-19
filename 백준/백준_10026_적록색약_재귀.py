# 적록색약
import sys
sys.setrecursionlimit(1000000)

def dfs(r, c):
    visited[r][c] = 1
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
            if colors[nr][nc] == colors[r][c]:
                dfs(nr, nc)
    return

N = int(input())
colors = [list(input()) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
dr = [0, 1, 0, -1]  # 우 하 좌 상
dc = [1, 0, -1, 0]
RGB = 0
same_RG = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            if colors[i][j] == 'R' or colors[i][j] == 'G' or colors[i][j] == 'B':
                RGB += 1
                dfs(i, j)

for i in range(N):
    for j in range(N):
        if colors[i][j] == 'G':
            colors[i][j] = 'R'

visited = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            if colors[i][j] == 'R' or colors[i][j] == 'B':
                same_RG += 1
                dfs(i, j)

print(RGB, same_RG)