import sys
sys.stdin = open('input.txt', 'r')

for t in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
    visited = [[0] * N for _ in range(N)]

    # 2찾기
    start = (0, 0, 0)
    for i in range(N**2):
        if arr[i // N][i % N] == 2:
            start = (i // N, i % N, 0)

    # BFS로 3찾기
    result = 0
    queue = [start]
    while len(queue) > 0:
        r, c, m = queue.pop(0)
        visited[r][c] = 1
        for d in range(4):
            nr, nc = r + dy[d], c + dx[d]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
                if arr[nr][nc] == 0:
                    queue.append((nr, nc, m + 1))
                elif arr[nr][nc] == 3:
                    result = m
        if result != 0:
            break

    print('#%d' %t, result)