import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline


def BFS(start_r, start_c):
    queue, result = deque(), list()
    queue.append([start_r, start_c, 1])
    visited = [[0] * M for _ in range(N)]
    dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]
    visited[0][0] = 1

    while queue:
        r, c, value = queue.popleft()
        for direction in range(4):
            nr, nc = r + dy[direction], c + dx[direction]
            if 0 <= nr < N and 0 <= nc < M and board[nr][nc] == '1' and not visited[nr][nc]:
                if nr == N - 1 and nc == M - 1:
                    return value + 1
                visited[nr][nc] = 1
                queue.append([nr, nc, value + 1])


N, M = map(int, read().rstrip().split())
board = [list(read().rstrip()) for _ in range(N)]
print(BFS(0, 0))
