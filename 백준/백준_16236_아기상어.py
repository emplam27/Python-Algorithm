# 1시간 50분
# 문제에서 필요한 부분 꼼꼼히 살피면서 갈 것
# 삼성에서는 BFS 염두 꼭 해둘 것
# 미리 해야할 일들 정리하면서 할것
# 주석 더 꼼꼼히 달 것


import sys
sys.stdin = open('input.txt', 'r')


# <해야할 일>

# 이동하면서 물고기 먹기 => BFS로 가장 가까이 있는 물고기 찾기
# 자신의 크기보다 큰 물고기 칸을 지나갈 수 없고, 자신과 사이즈가 똑같은 물고기는 지나갈수만 있음 => BFS조건
# 거리가 가깝고, 가장 위에, 가장 왼쪽에 있는 물고기 먹기 => 후보군을 만들어서 비교를 해주기
# 이동할 때, 자신보다 큰 물고기는 피해서 가기 => 이동하는 경로를 BFS로 파악하기

# 이동하는 시간재기
# 상어는 arr에 포함시키지않고 좌표로만 관리하고, 먹을 물고기가 결정되면 이동시간을 구해
# 더해주는 방법으로 하기

# 물고기를 size만큼 먹으면 본인 size 하나 올리기 => 먹은 물고기 변수 만들기

# 더이상 이동할 수 없으면 종료하기


# 순서
# BFS => 물고기 찾으면 물고기 위치와 함께 True
# False면 종료
# 먹은 물고기 카운트, 사이즈 업하기
# 이동한 시간 더하기


def find_fishes():
    # 후보군 배열 만들기
    # 후보군 배열이 하나라도 채워지면, 그와 같은거리에 있는 물고기만 탐색한 후 반복문을 종료
    # visited 필요
    global shark_pos

    candidates, min_distance, visited = [], N*N, [[0] * N for _ in range(N)]

    # BFS
    queue = [[shark_pos[0], shark_pos[1], 0]]
    while queue:
        r, c, distance = queue.pop(0)

        # 거리가 최소거리만큼 탐색할 수 있는 경우에만 탐색, 아니면 종료
        if distance >= min_distance:
            break

        visited[r][c] = 1
        for d in range(4):
            nr, nc = r + dy[d], c + dx[d]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] != 1 and arr[nr][nc] <= shark_size:
                # 먹을수 있는 물고기라면
                if arr[nr][nc] != 0 and arr[nr][nc] < shark_size:
                    visited[nr][nc] = 1
                    candidates.append([nr, nc])
                    min_distance = distance + 1  # 최소 거리값 갱신

                # 물고기가 아니거나, 같은 사이즈의 물고기라면
                else:
                    visited[nr][nc] = 1
                    queue.append([nr, nc, distance + 1])

    # 후보군이 존재한다면
    if candidates:
        # 후보군에서 가장 위, 그중 가장 왼쪽에 있는 물고기 고르기
        seleced_fish = [candidates[0][0], candidates[0][1]]
        for i in range(1, len(candidates)):
            if seleced_fish[0] > candidates[i][0]:
                seleced_fish = candidates[i]
            if seleced_fish[0] == candidates[i][0] and seleced_fish[1] > candidates[i][1]:
                seleced_fish = candidates[i]

        # 정해진 물고기 먹기
        arr[seleced_fish[0]][seleced_fish[1]] = 0
        shark_pos = seleced_fish

        # 상어 위치, 거리 반환
        return shark_pos, min_distance

    # 후보군이 존재하지 않는다면, False 반환
    else:
        return False, 0


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]

# 상어, 물고기들 위치 저장해놓기
shark_pos = []
fishes = 0
for i in range(N**2):
    if arr[i // N][i % N] != 0:
        if arr[i // N][i % N] == 9:
            shark_pos = [i // N, i % N]
            arr[i // N][i % N] = 0
        else:
            fishes += 1

# 상어 기본정보
shark_size, eaten_fishes = 2, 0

time = 0
while fishes:  # 남은 물고기가 있으면 반복

    # 물고기 찾고, 걸리는 시간 가지고 오기
    shark_pos, target_time = find_fishes()

    if shark_pos:  # 물고기를 찾았으면

        # 먹은 물고기 카운트, 사이즈 업하기
        eaten_fishes += 1
        if eaten_fishes == shark_size:
            shark_size += 1
            eaten_fishes = 0

        # 이동한 시간 더하기
        time += target_time

    else:  # 물고기를 못찾았으면
        break  # 반복문 종료

print(time)
