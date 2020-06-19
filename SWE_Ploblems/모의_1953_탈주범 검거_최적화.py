pipe = [
    [],
    [0, 1, 2, 3],
    [0, 1],
    [2, 3],
    [0, 3],
    [1, 3],
    [1, 2],
    [0, 2]
]
next_pipe = [
    [1, 2, 5, 6],
    [1, 2, 4, 7],
    [1, 3, 4, 5],
    [1, 3, 6, 7]
]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
for tc in range(1, int(input()) + 1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    q = [(R, C, arr[R][C])]
    visited[R][C] = 1
    cnt = 0
    for _ in range(L):
        for _ in range(len(q)):
            y, x, p = q.pop(0)
            cnt += 1
            for i in pipe[p]:
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < N and 0 <= nx < M and arr[ny][nx] in next_pipe[i] and not visited[ny][nx]:
                    q.append((ny, nx, arr[ny][nx]))
                    visited[ny][nx] = 1

    print('#%d %d' % (tc, cnt))