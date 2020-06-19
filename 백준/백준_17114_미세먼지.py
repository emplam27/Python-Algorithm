import sys

# sys.stdin = open("17114_input.txt", "r")

read = sys.stdin.readline

R, C, T = map(int, read().split())
mat = [list(map(int, read().split())) for _ in range(R)]

# 상 우 하 좌
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for time in range(T):
    stack = list()
    mat_copy = [[0] * C for _ in range(R)]
    # 튜플 리스트로 받아와보자. (r, c, 값)
    for r in range(R):
        for c in range(C):
            # 4방향 검사
            diffusion = 0
            if mat[r][c] >= 5:
                for d in range(4):
                    nr = r + dy[d]
                    nc = c + dx[d]
                    if 0 <= nr < R and 0 <= nc < C and mat[nr][nc] != -1:
                        stack.append([nr, nc, (mat[r][c] // 5)])
                        diffusion += 1
                stack.append([r, c, mat[r][c] - (mat[r][c] // 5) * diffusion])
            else:
                stack.append([r, c, mat[r][c]])

    # 확산한 mat 만들기
    for i, j, k in stack:
        mat_copy[i][j] += k

    # 공기청정기 위치 찾기
    cleaner = 0
    for i in range(R):
        if mat[i][0] == -1:
            cleaner = i
            break

    # 바람방향에 따라 이동시키기
    # 위쪽
    r = cleaner - 1
    c = 0
    direct_u = 0
    while True:
        nr = r + dy[direct_u]
        nc = c + dx[direct_u]
        if 0 > nr or nr >= cleaner + 1 or 0 > nc or nc >= C:
            direct_u = (direct_u + 1) % 4
            nr = r + dy[direct_u]
            nc = c + dx[direct_u]
        if mat_copy[nr][nc] == -1:
            mat_copy[r][c] = 0
            break
        mat_copy[r][c] = mat_copy[nr][nc]
        r = nr
        c = nc

    # 아래쪽
    r = cleaner + 2
    c = 0
    direct_d = 2
    while True:
        nr = r + dy[direct_d]
        nc = c + dx[direct_d]
        if cleaner + 1 > nr or nr >= R or 0 > nc or nc >= C:
            direct_d = (direct_d - 1) % 4
            nr = r + dy[direct_d]
            nc = c + dx[direct_d]
        if mat_copy[nr][nc] == -1:
            mat_copy[r][c] = 0
            break
        mat_copy[r][c] = mat_copy[nr][nc]
        r = nr
        c = nc

    for i in range(R):
        for j in range(C):
            mat[i][j] = mat_copy[i][j]

sum_dust = 0
for i in range(R):
    for j in range(C):
        if mat[i][j] != -1:
            sum_dust += mat[i][j]
print(sum_dust)
