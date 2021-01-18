import sys
from collections import deque

sys.stdin = open("input.txt", "r")
read = sys.stdin.readline


def solve():
    M, N = map(int, read().rstrip().split())
    board = [list(map(int, read().rstrip().split())) for _ in range(M)]
    dy, dx = [-1, 0, 1, 0], [0, -1, 0, 1]
    DP = [[0] * N for _ in range(M)]

    queue = deque()
    queue.append((0, 0, 1))
    result = 0
    while queue:
        print(queue)
        r, c, value = queue.popleft()
        for d in range(4):
            nr, nc = r + dy[d], c + dx[d]
            if 0 <= nr < M and 0 <= nc < N and board[r][c] > board[nr][nc]:
                if nr == M - 1 and nc == N - 1:
                    result += 1
                    continue
                queue.append((nr, nc))

    print(result)


solve()
