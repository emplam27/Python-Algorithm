import sys

sys.stdin = open("2667_input.txt", "r")

N = int(input())

arr = [list(map(int, list(input()))) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
aps = []


def dfs(r, c):
    num.append(1)
    visited[r][c] = 1
    for d in range(4):
        nr = r + dy[d]
        nc = c + dx[d]
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 1 and visited[nr][nc] == 0:
            dfs(nr, nc)
    return len(num)


for i in range(N):
    for j in range(N):
        num = []
        if arr[i][j] == 1 and visited[i][j] == 0:
            aps.append(dfs(i, j))

aps.sort()
print(len(aps))
for i in range(len(aps)):
    print(aps[i])