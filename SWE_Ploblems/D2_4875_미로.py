import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, list(input()))) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                start = (i, j)

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    stack = []
    stack.append(start)

    def dfs(r, c):
        while len(stack) > 0:
            r, c = stack.pop()
            visited[r][c] = 1
            for direct in range(4):
                nr = r + dy[direct]
                nc = c + dx[direct]
                if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
                    if arr[nr][nc] == 0:
                        stack.append((nr, nc))
                    elif arr[nr][nc] == 3:
                        return 1
        return 0


    print('#%d' % t, dfs(i, j))



