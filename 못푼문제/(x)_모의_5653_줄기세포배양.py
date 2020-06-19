import sys
sys.stdin = open('../SWE_Ploblems/input.txt', 'r')


# 시간이 각 (생명력 + 1)의 배수가 되면, 번식시키고 기존 배열을 새로운 배열로 대체


def activate(idx):
    active_cell[idx] = inactive_cell[idx]
    inactive_cell[idx] = []


def spread(idx):
    tmp_active = []
    for r, c in active_cell[idx]:
        for d in range(4):
            nr, nc = r + dy[d], c + dx[d]
            if (nr, nc) not in visited:
                tmp_active.append((nr, nc))
                visited.add((nr, nc))

    # 배열 대체
    inactive_cell[idx] = tmp_active
    return


def dead(idx):
    active_cell[idx] = []


for t in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]

    # 검사하면서 가장 큰 생명력을 가진 세포 찾기
    max_val = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] > max_val:
                max_val = arr[i][j]

    # 각 세포들이 가지고 있는 생명력 별로 활성, 비활성 배열 만들기 / 방문 set 만들기
    active_cell = [[] for _ in range(max_val + 1)]
    inactive_cell = [[] for _ in range(max_val + 1)]
    visited = set()
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0:
                inactive_cell[arr[i][j]].append((i, j))
                visited.add((i, j))

    # 시간대로 퍼뜨리는데, 동시에 퍼뜨려야할 경우, 생명력이 큰 순서대로 퍼뜨리기
    count = 0
    while count < K:
        count += 1
        # 배열을 역으로 순회하면서, 각각의 (인덱스(생명력) + 1)가 count를 나누었을때, 0이 될때만 세포를 퍼트린다.
        for idx in range(max_val, 0, -1):
            if len(active_cell[idx]) > 0:
                spread(idx)

        for idx in range(max_val, 0, -1):
            if count % (idx + 1) == idx-1:
                dead(idx)

        for idx in range(max_val, 0, -1):
            if count % (idx + 1) == idx:
                activate(idx)


    # cell에 남아있는 모든 세포들의 갯수 + 아직 활성화 되어있는 세포들 갯수
    result = 0
    for i in range(1, max_val + 1):
        result += len(inactive_cell[i])
        result += len(inactive_cell[i])

    print('#%d' %t, result)


    # 필요한 set(포함을 검사해야하기때문. get 사용): 활성세포, 비활성세포, visited(이미 방문 & 죽은세포)
    # 세포들은 (생명력 + 1)의 배수 시간대에 퍼진다.
    # 큰 세포들부터 퍼져야 하기 때문에,
    # 각 생명력 별로 모을 수 있는 2차원 배열 만들기, 시간이 각 (생명력 + 1)의 배수가 되면, 활성시키고, 기존 배열을 새로운 배열로 대체

    # 두개이상의 세포가 같은곳에 번식하는 경우, visited가 0인 상황에서는 더 큰 세포가 미리 공간을 차지하고,
    # 작은세포는 그곳을 못 오게 만든다.
