# 방문에 대한 혁신이 필요함.
# 비트연산을 사용한 방문배열에 대해 공부해봐야겠음


import sys

sys.stdin = open("../백준/input.txt", "r")

# <해야할 일>
# 1. 같은자리를 다시 돌아와야 하는데, BFS로 푸는게 맞는것인가. 완전 탐색이 맞지 않은가
#   이미 지나갔던 지점을 다시 지날 때, 소유한 열쇠에 변화가 없다면 가지 않아도 되지 않을까
#   열쇠는 다시 사용할 수 있는 것이기 때문에, visited배열을 3차원으로 만들어서 열쇠 정보를
#   저장하면서 방문 배열을 표시하면서 진행해보자
# 2. 열쇠와 문의 관계를 어떤식으로 풀 것인가. list를 사용해서 in ?, dict를 사용해서 get?
#   열쇠와 문은 여러개가 있을 수 있다. 또한 문에 대응하는 열쇠는 없을 수도 있다. 여러번 사용 가능하다.

from collections import deque


def game(start):
    visited = [[dict() for _ in range(M)] for _ in range(N)]

    queue = deque()
    queue.append(start)
    while queue:
        r, c, time, keys = queue.popleft()
        for d in range(4):
            nr, nc = r + dy[d], c + dx[d]
            if 0 <= nr < N and 0 <= nc < M and maze[nr][nc] != '#':  # 범위 안에서

                # 이동한 자리의 열쇠 배열보다 현재가 더 크다면 갱신, 아니라면 이동 안함
                if visited[nr][nc].get(''.join(keys)) is None:

                    # 출구를 만난다면 탈출
                    if maze[nr][nc] == '1':
                        return time + 1

                    # 열쇠를 만날 때
                    elif maze[nr][nc] in ['a', 'b', 'c', 'd', 'e', 'f']:
                        # 해당 열쇠가 없다면 추가 및 이동
                        if keys[ord(maze[nr][nc]) - 97] == '0':
                            tmp_keys = [*keys]
                            tmp_keys[ord(maze[nr][nc]) - 97] = '1'
                            visited[nr][nc][''.join(tmp_keys)] = True
                            queue.append([nr, nc, time + 1, tmp_keys])
                        else:
                            # 이미 해당 키가 있다면 추가 안하고 이동
                            queue.append([nr, nc, time + 1, keys])

                    # 문을 만날 때
                    elif maze[nr][nc] in ['A', 'B', 'C', 'D', 'E', 'F']:
                        # 해당 열쇠가 있다면 이동
                        if keys[ord(maze[nr][nc]) + 32 - 97] == '1':
                            queue.append([nr, nc, time + 1, keys])
                            visited[nr][nc][''.join(keys)] = True
                        # 해당 열쇠가 없다면 이동 안함

                    # 빈곳이면 이동
                    elif maze[nr][nc] == '.':
                        queue.append([nr, nc, time + 1, keys])
                        visited[nr][nc][''.join(keys)] = True
    return -1


N, M = map(int, input().split())
maze = [list(input()) for _ in range(N)]
dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]
# .: 빈곳, #: 벽, a~f: 열쇠, A-F: 문, 0: 현재위치, 1: 출구

# 현재위치 찾기
start = []
for i in range(N):
    for j in range(M):
        if maze[i][j] == '0':
            start, maze[i][j] = [i, j, 0, ['0', '0', '0', '0', '0', '0']], '.'

print(game(start))
