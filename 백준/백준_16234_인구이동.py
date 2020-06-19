import sys

sys.stdin = open("16234_input.txt", "r")

# 16234 인구이동

# 순서
# 열수있는 국경은 모두 연다. (평균값 구하기가 가능하도록 모두 다 리스트에 저장해놔야한다.)
# 리스트를 순회하면서 평균값을 다 구한 후, 채워넣는다.
# 여기까지가 1번이다.
# 몇번 하는지 구한다.


def bfs(i, j, union_list, visited):
    tmp_list = [(i, j, arr[i][j])]
    queue = [(i, j, arr[i][j])]
    visited[i][j] = 1

    while len(queue) > 0:
        r, c, m = queue.pop(0)
        for d in range(4):
            nr, nc = r + dy[d], c + dx[d]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and L <= abs(m - arr[nr][nc]) <= R:
                queue.append((nr, nc, arr[nr][nc]))
                visited[nr][nc] = 1
                tmp_list.append((nr, nc, arr[nr][nc]))

    if len(tmp_list) > 1:
        union_list.append(tmp_list)
    return


def move():
    visited = [[0] * N for _ in range(N)]
    union_list = list()
    for i in range(N**2):
        if visited[i // N][i % N] == 0:
            bfs(i // N, i % N, union_list, visited)

    # 연합국이 없다면 False를 리턴해준다.
    if len(union_list) == 0:
        return False

    else:
        # 연합된 국경끼리 평균값을 넣어준다.
        for i in range(len(union_list)):
            tmp = 0
            for j in range(len(union_list[i])):
                tmp += union_list[i][j][2]
            for j in range(len(union_list[i])):
                arr[union_list[i][j][0]][union_list[i][j][1]] = tmp // len(union_list[i])
        return True


N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]  # 상 후 하 좌

result = 0
while True:
    if move():
        result += 1
    else:
        break

print(result)
