import sys

sys.stdin = open("input.txt", "r")


def dfs(r, c):
    visited[r][c] = '-1'
    for i in range(4):
        nr = r + dy[i]
        nc = c + dx[i]
        if maze[nr][nc] == '3':
            return 1
        if 0 <= nr < 16 and 0 <= nc < 16 and maze[nr][nc] == '0' and visited[nr][nc] == '0':
            if dfs(nr, nc) == 1:
                return 1
    return 0


for t in range(1, 11):
    N = int(input())
    maze = [list(input()) for _ in range(16)]

    # 시작점 찾기
    for i in range(16):
        for j in range(16):
            if maze[i][j] == '2':
                start_r = i
                start_c = j
                break

    # 2차원 visited 배열을 만들어줌
    visited = [[0] * 16 for _ in range(16)]
    for i in range(16):
        for j in range(16):
            visited[i][j] = maze[i][j]

    # 방향 정해주기
    # 0:상, 1:우, 2:하, 3:좌
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    # maze[start_r][start_c] = '0'

    print('#%d' % t, dfs(start_r, start_c))
