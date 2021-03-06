import sys

sys.stdin = open("input.txt", "r")


N = int(sys.stdin.readline())
RGB = [list(sys.stdin.readline()) for _ in range(N)]
RB = [[0] * N for _ in range(N)]
visited1 = [[0] * N for _ in range(N)]
visited2 = [[0] * N for _ in range(N)]
dy, dx = [1, 0, -1, 0], [0, -1, 0, 1]

for i in range(N):
    for j in range(N):
        if RGB[i][j] == 'G' or RGB[i][j] == 'R':
            RB[i][j] = 'R'
        else:
            RB[i][j] = 'B'

RGB_cnt = 0
RB_cnt = 0
for i in range(N):
    for j in range(N):
        if visited1[i][j] == 0:
            stack = list()
            stack.append((i, j))
            while len(stack) > 0:
                r, c = stack.pop()
                visited1[r][c] = 1
                for d in range(4):
                    nr = r + dy[d]
                    nc = c + dx[d]
                    if 0 <= nr < N and 0 <= nc < N and visited1[nr][nc] == 0:
                        if RGB[nr][nc] == RGB[i][j]:
                            stack.append((nr, nc))
            RGB_cnt += 1

        if visited2[i][j] == 0:
            stack = list()
            stack.append((i, j))
            while len(stack) > 0:
                r, c = stack.pop()
                visited2[r][c] = 1
                for d in range(4):
                    nr = r + dy[d]
                    nc = c + dx[d]
                    if 0 <= nr < N and 0 <= nc < N and visited2[nr][nc] == 0:
                        if RB[nr][nc] == RB[i][j]:
                            stack.append((nr, nc))
            RB_cnt += 1

print(RGB_cnt, RB_cnt)
