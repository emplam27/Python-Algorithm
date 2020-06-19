# 1시간
# 0으로 만들어주면서 기존의 cctv 시야까지 바뀌버리면 안되기 때문에
# 바꿔주는 배열을 따로 만들어서 그 부분만 7, 0 으로 바꿔줘야 한다.


import sys

sys.stdin = open('../못푼문제/17822_input.txt', 'r')


def search_view(r, c, room, d, view):
    nr, nc = r + dy[d], c + dx[d]
    while 0 <= nr < N and 0 <= nc < M:
        if room[nr][nc] == 0:
            view.append([nr, nc])
        elif room[nr][nc] == 6:
            break
        # cctv면 그냥감
        nr, nc = nr + dy[d], nc + dx[d]

def change_7(view):
    for v in range(len(view)):
        room[view[v][0]][view[v][1]] = 7


def change_0(view):
    for v in range(len(view)):
        room[view[v][0]][view[v][1]] = 0


def cctv_1_check(r, c, idx, room, direction):
    view = []
    search_view(r, c, room, direction, view)
    change_7(view)
    check(idx, room)
    change_0(view)
    return


def cctv_2_check(r, c, idx, room, direction):
    view = []
    search_view(r, c, room, (direction + 4) % 4, view)
    search_view(r, c, room, (direction + 2) % 4, view)
    change_7(view)
    check(idx, room)
    change_0(view)
    return


def cctv_3_check(r, c, idx, room, direction):
    view = []
    search_view(r, c, room, (direction + 4) % 4, view)
    search_view(r, c, room, (direction + 5) % 4, view)
    change_7(view)
    check(idx, room)
    change_0(view)
    return


def cctv_4_check(r, c, idx, room, direction):
    view = []
    search_view(r, c, room, (direction + 3) % 4, view)
    search_view(r, c, room, (direction + 4) % 4, view)
    search_view(r, c, room, (direction + 5) % 4, view)
    change_7(view)
    check(idx, room)
    change_0(view)
    return


def cctv_5_check(r, c, idx, room):
    view = []
    search_view(r, c, room, 0, view)
    search_view(r, c, room, 1, view)
    search_view(r, c, room, 2, view)
    search_view(r, c, room, 3, view)
    change_7(view)
    check(idx, room)
    change_0(view)
    return


def check(idx, room):
    global min_result

    if idx >= len(cctv):
        result = 0
        for i in range(N):
            for j in range(M):
                if room[i][j] == 0:
                    result += 1
        if min_result > result:
            min_result = result
        return

    # cctv종류별로 재귀함수 실행
    r, c, m = cctv[idx]
    if m == 1:
        for direction in range(4):
            cctv_1_check(r, c, idx + 1, room, direction)
    elif m == 2:
        for direction in range(4):
            cctv_2_check(r, c, idx + 1, room, direction)
    elif m == 3:
        for direction in range(4):
            cctv_3_check(r, c, idx + 1, room, direction)
    elif m == 4:
        for direction in range(4):
            cctv_4_check(r, c, idx + 1, room, direction)
    else:
        cctv_5_check(r, c, idx + 1, room)


N, M = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]  # 상 우 하 좌


# cctv위치정보 확인 [r, c, 종류]
cctv = list()
for i in range(N):
    for j in range(M):
        if room[i][j] != 0 and room[i][j] != 6:
            cctv.append([i, j, room[i][j]])

min_result = N * M + 1
check(0, room)

print(min_result)


# 어디에 어떤 cctv가 있는지 찾는다.
# cctv순서대로 돌아가면서 사각지대를 확인한다. 재귀함수 활용합시다.
