def dfs(r, c):
    visited = [[0] * 16 for _ in range(16)]
    stack = list()
    # visited[r][c] = 1
    stack.append((r, c))
    while len(stack) > 0:
        r = stack[-1][0]
        c = stack[-1][1]
        visited[r][c] = 1
        for k in range(4):
            dr = [0, 1, 0, -1]  # (우, 하, 좌, 상)
            dc = [1, 0, -1, 0]
            nr = r + dr[k]
            nc = c + dc[k]
            if board[nr][nc] == 3:
                return 1
            if 0 <= nr < 16 and 0 <= nc < 16:
                if visited[nr][nc] == 0 and board[nr][nc] == 0:
                    stack.append((nr, nc))
                    break
        else:
            stack.pop()
    return 0


T = 10
for t in range(1, T + 1):
    tn = int(input())
    board = [list(map(int, list(input()))) for _ in range(16)]
    # 시작점 찾기
    for i in range(16):
        for j in range(16):
            if board[i][j] == 2:
                print('#%d' % t, dfs(i, j))
