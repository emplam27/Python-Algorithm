# 3시간..
# 너무 힘든문제..
# visited는 길이로 판단하지 말 것.. [0] * N 배열로 사용할것
# 최소신장트리 공부할 것


import sys
sys.stdin = open('input.txt', 'r')


# <주의할 점>
# 다리의 양 끝점은 섬과 인접한 바다위에 있어야 하며, 다리의 옆으로 붙어있으면 안됨. 인정x
# 다리의 방향이 중간에 바뀌면 안됨
# 다리의 길이는 2 이상
# 다리는 교차할 수 있음, 길이네는 각각 포함


# <해야할 일>
# 1. 어떻게 풀까?
# 사실 놓을 수 있는 다리의 종류만 미리 알 수 있다면, 그중에서 골라가면서 최소길이 찾는것은 어렵지 않은데.
# 그렇다면 그래프로 풀 수 있을 것 같은 느낌이다. 최소신장트리? 공부하고 풀어볼 수 있도록 하자..

# 2. 모든 다리가 연결되었다는 정보는 어떻게 찾을것인가?
# 다리를 선택한 후, 모든 것이 연결되어있다는 확인만 하면 됨. 그래프로. 게리멘더링이랑 비슷하게 생각하면 될까
# 놓을 수 있는 다리를 모두 구해서 하나의 배열에 저장해놓자. [노드, 노드, 다리길이]

# 3. 다리는 어떤식으로 찾을것이냐?
# 각 섬에서 상 하 좌 우로 다리를 뻣어본다. 닿는곳이 있다면 연결됐다고 한다.
# 한 섬에서 다른섬까지 길이가 짧은 다리가 생긴다면 갱신한다. 이미 같은길이 다리가 있다면 추가하지 않아도된다.
# 이 정보는 2차원 그래프를 이용하여 정리하자.
# 1 -> 2, 3, 4 / 2-> 3, 4 / 3 -> 4... 등으로 정리를 끝낸 후, 1차원 배열에 다리를 옮겨담는다.
# 이후 완전탐색


# <순서>
# 각 섬에서 다른 섬으로 연결될 수 있는 다리 정보를 모두 받는다.
#       1 -> 2, 3, 4 / 2-> 3, 4 / 3 -> 4... 등으로 정리
#       한 지점에서 4방에 0이 있는 부분을 확인하고, 그 방향으로 다리를 쏜다.
#       어떤 숫자에 닿으면 다리를 연결할 수 있는 것이다.
# 이때 2차원 배열을 이용해서 연결정보와 다리의 길이를 저장해놓는다.
# 모두 찾게되면 1차원 배열에 옮겨담고 완전탐색에 들어간다.
# 완탐을 이용해 다리를 선택해서 모두 연결되어있는지 확인하고 최소값을 갱신한다.

from collections import deque


def find_islands(r, c):
    global islands

    queue = deque()
    queue.append([r, c])
    while len(queue):
        r, c = queue.popleft()
        visited[r][c] = 1
        board[r][c] = islands + 1
        for d in range(4):
            nr, nc = r + dy[d], c + dx[d]
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and board[nr][nc] == 1:
                queue.append([nr, nc])

    islands += 1  # bfs끝내고 섬 갯수 하나 늘리기
    return


def make_bridge(r, c):

    start_island, end_island = board[r][c], 0
    for d in range(4):
        nr, nc = r + dy[d], c + dx[d]
        if 0 <= nr < N and 0 <= nc < M and board[nr][nc] == 0:  # 바다면
            length = 0
            while 0 <= nr < N and 0 <= nc < M:
                if board[nr][nc] != 0:  # 섬을 만났다면
                    if length < 2:  # 길이가 2 미만이면
                        break
                    else:  # 길이가 2 이상이면
                        end_island = board[nr][nc]  # 도착섬 지정하고
                        if bridges_graph[start_island][end_island] == 0:
                            bridges_graph[start_island][end_island] = length
                        elif bridges_graph[start_island][end_island] > length: # 길이가 더짧다면 갱신
                            bridges_graph[start_island][end_island] = length
                        break

                else:  # 섬을 못만나면
                    nr, nc = nr + dy[d], nc + dx[d]
                    length += 1
                    continue
    return


def check_link(bridges):
    global bridges_array, islands

    # 연결정보 만들기
    result = 0
    tmp_graph = [[0] * (islands + 1) for _ in range(islands + 1)]
    for bridge in bridges:
        tmp_graph[bridges_array[bridge][0]][bridges_array[bridge][1]] = bridges_array[bridge][2]
        tmp_graph[bridges_array[bridge][1]][bridges_array[bridge][0]] = bridges_array[bridge][2]
        result += bridges_array[bridge][2]

    # bfs
    queue = deque()
    queue.append(1)
    visited = [0] * islands
    while len(queue):
        m = queue.popleft()
        visited[m-1] = 1
        for i in range(1, islands + 1):
            if tmp_graph[m][i] != 0 and visited[i-1] == 0:
                queue.append(i)
    if 0 not in visited:
        return result
    else:
        return None


def combination(idx, selected, max_idx):
    global min_result

    if idx >= max_idx:
        tmp = []
        for i in range(max_idx):
            if selected[i] == 1:
                tmp.append(i)
        result = check_link(tmp)
        if result:
            if min_result > result:
                min_result = result
        return

    selected[idx] = 1
    combination(idx + 1, selected, max_idx)
    selected[idx] = 0
    combination(idx + 1, selected, max_idx)


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]


# 섬의 갯수를 먼저 찾는것이 필요하다. bfs를 사용하면서 지도까지 번호를 바꿔놓는것이 좋다.
islands = 0
visited = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if visited[i][j] == 0 and board[i][j] == 1:
            find_islands(i, j)

# 지도를 순회하면서 각 섬을 연결하는 최소길이의 다리를 찾는다.
bridges_graph = [[0] * (islands + 1) for _ in range(islands + 1)]
for i in range(N):
    for j in range(M):
        if board[i][j] != 0:  # 섬이면
            make_bridge(i, j)

# 찾은 다리를 조합을 사용하기 위해 1차원 배열에 저장하기
bridges_array = []
for i in range(islands + 1):
    for j in range(i + 1, islands + 1):
        if bridges_graph[i][j] != 0:
            bridges_array.append([i, j, bridges_graph[i][j]])

if len(bridges_array):
    # 다리를 모두 찾았다면 그래프 완전탐색
    selected = [0] * len(bridges_array)
    min_result = N * M
    combination(0, selected, len(bridges_array))

    if min_result != N * M:
        print(min_result)
    else:
        print(-1)
else:
    print(-1)
