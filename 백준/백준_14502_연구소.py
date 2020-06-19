import sys

sys.stdin = open("14502_input.txt", "r")

# 14502 연구소

# 조합을 이용하여 빈공간(empty) 중 벽을 놓을 3곳 선정하기
def combination(selected, idx, count1):
    if idx == cnt_empty:
        if count1 == 3:
            for i in range(cnt_empty):
                if selected[i] == 1:
                    wall_list.append(empty[i])
        return

    if count1 > 3:
        return

    selected[idx] = 1
    count1 += 1
    combination(selected, idx + 1, count1)
    selected[idx] = 0
    count1 -= 1
    combination(selected, idx + 1, count1)


# BFS를 이용하여 바이러스 퍼트리기
def bfs(r, c):
    visited = [[0] * M for _ in range(N)]
    dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1] # 상 우 하 좌
    queue = list()
    queue.append((r, c))
    while len(queue) > 0:
        r, c = queue.pop(0)
        visited[r][c] = 1
        for d in range(4):
            nr = r + dy[d]
            nc = c + dx[d]
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and lab_copy[nr][nc] == 0:
                lab_copy[nr][nc] = 2
                queue.append((nr, nc))
    return


N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
lab_copy = [[0] * M for _ in range(N)]

# 바이러스 위치리스트(virus), 빈공간 위치리스트(empty) 만들기
empty = []
cnt_empty = 0
virus = []
for i in range(N):
    for j in range(M):
        lab_copy[i][j] = lab[i][j]
        if lab[i][j] == 0:
            cnt_empty += 1
            empty.append((i, j))
        elif lab[i][j] == 2:
            virus.append((i, j))


# 벽 세울 공간 리스트 만들기
selected = [0] * cnt_empty
wall_list = []
count1 = 0
combination(selected, 0, 0)


# 3개씩 끊어 벽을 세워주면서 바이러스 퍼트리고, 안전영역 갯수 확인하기
max_safe = 0
while len(wall_list) > 0:

    for _ in range(3):
        r, c = wall_list.pop(0); lab_copy[r][c] = 1

    for r, c in virus:
        bfs(r, c)

    safe = 0
    for i in range(N):
        for j in range(M):
            if lab_copy[i][j] == 0:
                safe += 1
            lab_copy[i][j] = lab[i][j]

    if safe > max_safe:
        max_safe = safe

print(max_safe)

