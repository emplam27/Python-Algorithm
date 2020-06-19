import sys
sys.stdin = open("input.txt", "r")

from collections import deque


for t in range(1, int(input()) + 1):
    N = int(input())
    field = [list(map(int, input())) for _ in range(N)]
    dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]

    INF = float('inf')
    visited = [[INF] * N for _ in range(N)]
    visited[0][0] = 0

    queue = deque()
    queue.append([0, 0, 0])
    while queue:
        r, c, value = queue.popleft()
        for d in range(4):
            nr, nc = r + dy[d], c + dx[d]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] > value + field[nr][nc]:
                visited[nr][nc] = value + field[nr][nc]
                queue.append([nr, nc, value + field[nr][nc]])


    print('#%d' %t, visited[N-1][N-1])