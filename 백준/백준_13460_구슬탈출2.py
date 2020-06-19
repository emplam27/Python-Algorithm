import sys
sys.stdin = open('input.txt', 'r')

# <주의할 점>
# 1. 파랑구슬이 들어가면 게임 종료. 파란구슬만 들어가야함
# 2. 빨간구슬이 항상 동시에 움직인다고 생각하면 안됨. 빨강구슬은 이동하나 파랑은 가만히 있을수도 있고..
# 3. 이동 방향에 따라 먼저 움직이는 공이 다를 수 있다.
# 4. bfs를 이용해서 풀어야 할 것 같다. 최소 경우이기 때문에. 4(상하좌우)의 10승번까지 연산한다.
# 5. visited를 만들어서 이미 들른 곳이라면 그곳은 연산을 하지 않게 하고싶은데..
# 6. visited를 [빨간공r, 빨간공c, 파란공r, 파란공c] ..? 이걸 하나의 요소로..? [] in visited?
#   dict로 하지 않으면 너무 느리다.. 4차원 배열을 만들어보자. 인덱싱은 빠르니까

# <해야할 일>
# 1. 현재의 빨강공, 파란공의 위치를 기반으로 상, 우, 하, 좌 움직이는 bfs를 꾸민다.
# 2. 특정 방향으로 움직일 때, 해당 방향이랑 가까운쪽 공부터 움직인다.
# 3. 공을 움직인 후 그 위치를 visited에 기록하고, queue에 집어넣는다.
# 4. 빨간공만 탈출하면 끝, 같이 탈출하면 queue에 넣지않고 continue

from collections import deque


def red_ball_move(d, rr, rc, br, bc):
    while True:
        if board[rr + dy[d]][rc + dx[d]] == '#':
            return False, rr, rc
        if board[rr + dy[d]][rc + dx[d]] == 'O':
            return True, rr + dy[d], rc + dx[d]
        if br == rr + dy[d] and  bc == rc + dx[d]:
            return False, rr, rc
        rr, rc = rr + dy[d], rc + dx[d]


def blue_ball_move(d, rr, rc, br, bc):
    while True:
        if board[br + dy[d]][bc + dx[d]] == '#':
            return False, br, bc
        if board[br + dy[d]][bc + dx[d]] == 'O':
            return True, br + dy[d], bc + dx[d]
        if rr == br + dy[d] and rc == bc + dx[d]:
            return False, br, bc
        br, bc = br + dy[d], bc + dx[d]


def move_ball(d, rr, rc, br, bc):

    red_ball_in, blue_ball_in = False, False
    if d == 0:  # 상
        if rr <= br:
            red_ball_in, rr, rc = red_ball_move(d, rr, rc, br, bc)
            blue_ball_in, br, bc = blue_ball_move(d, rr, rc, br, bc)
        else:
            blue_ball_in, br, bc = blue_ball_move(d, rr, rc, br, bc)
            red_ball_in, rr, rc = red_ball_move(d, rr, rc, br, bc)
    elif d == 2:  # 하
        if rr <= br:
            blue_ball_in, br, bc = blue_ball_move(d, rr, rc, br, bc)
            red_ball_in, rr, rc = red_ball_move(d, rr, rc, br, bc)
        else:
            red_ball_in, rr, rc = red_ball_move(d, rr, rc, br, bc)
            blue_ball_in, br, bc = blue_ball_move(d, rr, rc, br, bc)
    elif d == 1:  # 우
        if rc <= bc:
            blue_ball_in, br, bc = blue_ball_move(d, rr, rc, br, bc)
            red_ball_in, rr, rc = red_ball_move(d, rr, rc, br, bc)
        else:
            red_ball_in, rr, rc = red_ball_move(d, rr, rc, br, bc)
            blue_ball_in, br, bc = blue_ball_move(d, rr, rc, br, bc)
    elif d == 3:  # 좌
        if rc <= bc:
            red_ball_in, rr, rc = red_ball_move(d, rr, rc, br, bc)
            blue_ball_in, br, bc = blue_ball_move(d, rr, rc, br, bc)
        else:
            blue_ball_in, br, bc = blue_ball_move(d, rr, rc, br, bc)
            red_ball_in, rr, rc = red_ball_move(d, rr, rc, br, bc)

    return red_ball_in, blue_ball_in, rr, rc, br, bc


def simulation(red_ball, blue_ball, visited):
    global result

    queue = deque()
    queue.append([red_ball[0], red_ball[1], blue_ball[0], blue_ball[1], 0])

    while queue:
        red_r, red_c, blue_r, blue_c, count = queue.popleft()
        visited[red_r][red_c][blue_r][blue_c] = 1
        count += 1
        for direction in range(4):
            red_ball_in, blue_ball_in, red_nr, red_nc, blue_nr, blue_nc = move_ball(direction, red_r, red_c, blue_r, blue_c)
            if blue_ball_in:
                continue
            if red_ball_in:
                result = count
                return
            else:
                if visited[red_nr][red_nc][blue_nr][blue_nc] == 0 and count < 10:
                    queue.append([red_nr, red_nc, blue_nr, blue_nc, count])


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1] # 상 우 하 좌

# 공 위치찾기
red_ball, blue_ball = [], []
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            red_ball = [i, j]
        elif board[i][j] == 'B':
            blue_ball = [i, j]

# BFS 시작
visited = [[[[0] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]  # 빨간공_r, 빨간공_c, 파란공_r, 파란공_c
result = 11
simulation(red_ball, blue_ball, visited)
if result == 11:
    print(-1)
else:
    print(result)