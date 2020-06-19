import sys

sys.stdin = open("input.txt", "r")

from collections import deque


def check_line(r, c, count, direct):

    if direct == 0:
        if pipe[r][c] == 1 or pipe[r][c] == 2 or pipe[r][c] == 5 or pipe[r][c] == 6:
            queue.append((r, c, count))
            return

    if direct == 1:
        if pipe[r][c] == 1 or pipe[r][c] == 3 or pipe[r][c] == 6 or pipe[r][c] == 7:
            queue.append((r, c, count))
            return

    if direct == 2:
        if pipe[r][c] == 1 or pipe[r][c] == 2 or pipe[r][c] == 4 or pipe[r][c] == 7:
            queue.append((r, c, count))
            return

    if direct == 3:
        if pipe[r][c] == 1 or pipe[r][c] == 3 or pipe[r][c] == 4 or pipe[r][c] == 5:
            queue.append((r, c, count))
            return


def check():

    while len(queue) > 0:

        r, c, count = queue.popleft()
        visited[r][c] = 1

        if count == L:
            continue

        elif pipe[r][c] == 1:
            for d in range(4):
                nr, nc, direct = r + dy[d], c + dx[d], d
                if 0 <= nr < N and 0 <= nc < M and pipe[nr][nc] != 0 and visited[nr][nc] == 0:
                    check_line(nr, nc, count + 1, direct)

        elif pipe[r][c] == 2 or pipe[r][c] == 3:
            for d in range(4):
                if d % 2 == pipe[r][c] % 2:
                    nr, nc, direct = r + dy[d], c + dx[d], d
                    if 0 <= nr < N and 0 <= nc < M and pipe[nr][nc] != 0 and visited[nr][nc] == 0:
                        check_line(nr, nc, count + 1, direct)

        elif pipe[r][c] == 4 or pipe[r][c] == 5 or pipe[r][c] == 6 or pipe[r][c] == 7:
            for d in range(4):
                if d == pipe[r][c] % 4 or d == (pipe[r][c] + 1) % 4:
                    nr, nc, direct = r + dy[d], c + dx[d], d
                    if 0 <= nr < N and 0 <= nc < M and pipe[nr][nc] != 0 and visited[nr][nc] == 0:
                        check_line(nr, nc, count + 1, direct)


T = int(input())
for t in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    pipe = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    dy, dx = [-1, 0, 1, 0],  [0, 1, 0, -1]

    queue = deque()
    queue.append((R, C, 1))
    check()

    result = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 1:
                result += 1

    print('#%d' % t, result)