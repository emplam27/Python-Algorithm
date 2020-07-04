import sys

sys.stdin = open("input.txt", "r")

"""
<해야할 일>
1. 나머지 모양은 모두 DFS로 판별이 가능하나 ㅜ모양은 판별이 불가능하다.
2. 한칸 정하고, 한칸부터 DFS, ㅜ모양 판별 실행하기 실행하기. 반복문 말고 재귀 DFS활용. 이전자리 찍을 수 있게.
3. 반복된 부분은 어떤식으로 배제할것인가? 위로 올라가는 부분을 없엔다면 중복을 많이 줄일 수 있지 않을까?
    우, 하, 좌 방향으로만 실행하면 중복을 꽤 많이 줄일 수 있을 것 같은데
"""


def dfs(r, c, value, result):
    global max_result

    if value == 4:
        if max_result < result:
            max_result = result
        return

    for d in range(3):
        nr, nc = r + dy[d], c + dx[d]
        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
            visited[nr][nc] = 1
            dfs(nr, nc, value + 1, result + board[nr][nc])
            visited[nr][nc] = 0


def t_shape_check(r, c):
    global max_result

    for d in range(4):
        tmp_result = board[r][c]
        for p in range(3):
            nr, nc = r + t_shape[d][p][0], c + t_shape[d][p][1]
            if 0 <= nr < N and 0 <= nc < M:
                tmp_result += board[nr][nc]
            else:
                break
        else:
            if max_result < tmp_result:
                max_result = tmp_result
    return


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dy, dx = [0, 1, 0], [1, 0, -1]  # 우 하 좌
t_shape = [
    [[-1, 0], [0, 1], [1, 0]],  # 상 우 하
    [[0, 1], [1, 0], [0, -1]],  # 우 하 좌
    [[1, 0], [0, -1], [-1, 0]],  # 하 좌 상
    [[0, -1], [-1, 0], [0, 1]]  # 좌 상 우
]

max_result = 0
visited = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(i, j, 1, board[i][j])
        t_shape_check(i, j)
        visited[i][j] = 0

print(max_result)
