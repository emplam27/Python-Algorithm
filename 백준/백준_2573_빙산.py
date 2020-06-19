import sys

sys.stdin = open("input.txt", "r")

# <해야할 일>
# 빙산을 탐색하면서 사방에 0이 몇개가 있는지 파악한 후, 모든 파악이 끝났으면 빼준다.(중간에 빼면 문제발생)
# BFS를 이용하여 덩어리 수를 계산해준다. 덩어리 수가 2 이상이면 끝

# <주의할 점>
# 빙산이 녹을 때, 얼만큼 녹는지 계산한 후 한번에 빼줘야함
# 덩어리수가 1개로 끝까지가면 0 출력

from collections import deque


def bfs():

    count, visited = 0, [[0] * M for _ in range(N)]
    tmp_melting = dict()  # 녹이고자 하는 좌표와 값을 저장하는 딕셔너리
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            if iceberg[i][j] != 0 and visited[i][j] == 0:
                count += 1
                queue = deque()
                queue.append([i, j])
                visited[i][j] = 1
                while queue:
                    r, c = queue.popleft()
                    for d in range(4):
                        nr, nc = r + dy[d], c + dx[d]
                        if iceberg[nr][nc] != 0 and visited[nr][nc] == 0:
                            visited[nr][nc] = 1
                            queue.append([nr, nc])
                        elif iceberg[nr][nc] == 0:
                            if tmp_melting.get((r, c)) is None:
                                tmp_melting[(r, c)] = 1
                            else:
                                tmp_melting[(r, c)] += 1

    return count, tmp_melting


N, M = map(int, input().split())
iceberg = [list(map(int, input().split())) for _ in range(N)]
dy, dx = [1, 0, -1, 0], [0, 1, 0, -1]

time = 0
while True:

    iceberg_nums, melting = bfs()

    if iceberg_nums > 1:
        print(time)
        break

    elif iceberg_nums == 0:
        print(0)
        break

    # 딕셔러니 순회하며 녹이기
    for key, value in melting.items():
        iceberg[key[0]][key[1]] -= value
        if iceberg[key[0]][key[1]] < 0:
            iceberg[key[0]][key[1]] = 0

    time += 1
