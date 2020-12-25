import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline


def BFS():
    global unripe_count

    max_result = 0
    while ripe_tomato:
        h, n, m, value = ripe_tomato.popleft()
        visited[h][n][m] = 1
        for direction in range(6):
            dh, dn, dm = h + dz[direction], n + dy[direction], m + dx[direction]
            if 0 <= dh < H and 0 <= dm < M and 0 <= dn < N and visited[dh][dn][dm] == 0 and boxes[dh][dn][dm] == 0:
                visited[dh][dn][dm] = 1
                ripe_tomato.append((dh, dn, dm, value + 1))
                max_result = max(max_result, value + 1)
                unripe_count -= 1
                if unripe_count == 0:
                    print(max_result)
                    exit()
    print(-1)


M, N, H = map(int, read().rstrip().split())
boxes = []
for _ in range(H):
    boxes.append([list(map(int, read().rstrip().split())) for _ in range(N)])
dz, dy, dx = [-1, 1, 0, 0, 0, 0], [0, 0, -1, 0, 1, 0], [0, 0, 0, 1, 0, -1]  # 상, 하, 북, 동, 남, 서
visited = [[[0] * M for _ in range(N)] for _ in range(H)]  # 검사를 완료한 익은 토마토를 표시

unripe_count = 0  # 익지않은 토마토의 수
ripe_tomato = deque()  # 익은 토마토의 좌표를 저장
for h in range(H):
    for n in range(N):
        for m in range(M):
            if boxes[h][n][m] == 1:
                ripe_tomato.append((h, n, m, 0))
            elif boxes[h][n][m] == 0:
                unripe_count += 1

if unripe_count == 0:
    print(0)
    exit()

BFS()
