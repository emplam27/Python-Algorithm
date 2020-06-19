import sys

# sys.stdin = open("14503_input.txt", "r")

N, M = map(int, input().split())
r, c, d = map(int, input().split())
# d = 0: 북, 1: 동, 2: 남, 3: 서
arr = [list(map(int, input().split())) for _ in range(N)]
arr2 = [[0]*M for _ in range(N)]
# 0: 청소안한 곳, 1: 벽, 2: 청소한 곳

# 비교용 복제배열 만들어주기
for i in range(N):
    for j in range(M):
        arr2[i][j] = arr[i][j]

# 초기 방향
direct = d
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
power = 1

while power == 1:
    arr[r][c] = 2

    if arr[r + 1][c] != 0 and arr[r - 1][c] != 0 and arr[r][c + 1] != 0 and arr[r][c - 1] != 0:
        if arr[r - dy[direct]][c - dx[direct]] == 1:
            power = 0
            break
        else:
            r -= dy[direct]
            c -= dx[direct]
            continue

    # 왼쪽 방향으로 탐색, 청소안한 공간이 있으면 왼쪽으로 회전 후 1칸 전진
    if arr[r + dy[(direct + 3) % 4]][c + dx[(direct + 3) % 4]] == 0:
        direct = (direct + 3) % 4
        r += dy[direct]
        c += dx[direct]
        continue

    elif arr[r + dy[(direct + 3) % 4]][c + dx[(direct + 3) % 4]] != 0:
        direct = (direct + 3) % 4
        continue

cnt = 0
for i in range(N):
    for j in range(M):
        if arr2[i][j] != arr[i][j]:
            cnt += 1

print(cnt)
