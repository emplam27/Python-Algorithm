import sys
sys.stdin = open("input.txt", "r")

# 2시간..
# 50분만에 풀고 1시간 넘게 해맸음
# 문제 설명 그지같이 해놓네..


# <해야할 일>
# 1. 바이러스를 놓을 수 있는 자리중에 M개를 선택하여 조합을 구한다
# 2. 조합의 요소들을 BFS에 추가하여 BFS한다.
# 3. BFS에서 value 값이 가장 큰 값이 퍼지는데 걸리는 시간

# <주의할 점>
# 1. 모든칸에 바이러스가 전파 되었는지 확인해야 함
# 2. 활성 바이러스가 비활성 바이러스에게 가면 활성바이러스가 됨

from collections import deque


def spread_virus(points):
    global min_result

    visited = [[0] * N for _ in range(N)]
    copied_laboratory = [[0] * N for _ in range(N)]
    for i in range(N ** 2):
        copied_laboratory[i // N][i % N] = laboratory[i // N][i % N]

    queue = deque()
    for point in points:
        queue.append(available_point[point] + [0])

    max_value = 0
    while queue:
        r, c, value = queue.popleft()
        for d in range(4):
            nr, nc = r + dy[d], c + dx[d]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                if copied_laboratory[nr][nc] == 0:
                    copied_laboratory[nr][nc] = value + 1
                    queue.append([nr, nc, value + 1])
                    if max_value < value + 1:
                        max_value = value + 1
                elif copied_laboratory[nr][nc] == 2:
                    queue.append([nr, nc, value + 1])

    # 바이러스 전파가 완료되었는지
    for i in range(N):
        if 0 in copied_laboratory[i]:
            return

    if min_result > max_value:
        min_result = max_value
    return


def combination(idx, selected, count):

    if count > M:
        return

    if idx >= len(selected):
        if count == M:
            tmp_point = []
            for point in range(len(selected)):
                if selected[point] == 1:
                    tmp_point.append(point)
            spread_virus(tmp_point)
        return

    selected[idx] = 1
    combination(idx + 1, selected, count + 1)
    selected[idx] = 0
    combination(idx + 1, selected, count)


N, M = map(int, input().split())
laboratory = [list(map(int, input().split())) for _ in range(N)]
dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]

# 바이러스 놓을 수 있는 위치 정하기
available_point = []
for i in range(N**2):
    if laboratory[i // N][i % N] == 2:
        available_point.append([i // N, i % N])

# 조합구하기
min_result = N**2
selected = [0] * len(available_point)
combination(0, selected, 0)

if min_result == N**2:
    min_result = -1

print(min_result)
