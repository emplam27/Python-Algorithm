import sys

sys.stdin = open("input.txt", "r")

"""
깊은 복사때문에 막힘. 깊은복사를 하는 방법들을 알아놔야할 것 같음

<해야할 일>
1. 0, 0 자리에 상어가 들어가야 하고, 그 자리의 물고기의 방향을 갖는다.
2. 물고기의 번호 순서대로 이동시켜야 하며, 이동할 수 없는 경우에는 각도를 반시계 방향으로 45도 돌린다.
3. 이동하게 되면 기존의 자리에 있는 물고기와 방향을 바꾸며, 빈칸과 다른물고기가 있는 칸만 이동 가능하다.
4. 상어는 바라보는 방향의 어느곳으로도 이동이 가능하며, 지나가는 길의 물고기는 먹지 않고 이동할 곳만 먹는다.

<주의할 점>
1. 물고기가 갈 곳이 없다고 판명되면 원래의 방향을 가진 채 그대로 있게 되는가?
2. 물고기들은 공간에 표시할 것인가? 물고기는 적은 번호에서부터 순서대로 움직여야 하기 때문에
    공간배열 만으로는 부족하다. 물고기의 순서대로 위치를 기억하는 배열이 필요하다. 
3. 상어는 이동방향에서 물고기가 있는 어느 칸이던 갈 수 있기 때문에 모든 케이스를 확인하는 
    재귀함수로 이동해야 할 것 같다. 
4. 해당 재귀함수를 사용하려면 인자로 (상어의 위치와 방향, 남은 물고기 배열, 현재 공간 상황)이 필요하다.
"""

from copy import deepcopy


# 먹은 물고기를 인자로 주자.
# (기존 상어 위치, 타겟으로한 물고기, 남아있는 물고기 배열, 현재 공간 배열, 현재까지의 결과값)
def simulation(shark_r, shark_c, target_fish, current_fishes, current_ocean, result):
    global max_result

    fishes = deepcopy(current_fishes)
    ocean = deepcopy(current_ocean)

    ocean[shark_r][shark_c] = 0  # 현재 상어 위치를 빈곳으로 바꾸기
    shark = fishes[target_fish]  # 인자로 받은 타겟 물고기의 위치와 방향 갖기
    fishes[target_fish] = 0  # 먹힌 물고기를 물고기 배열에서 지우기
    ocean[shark[0]][shark[1]] = -1  # 물고기 위치에 상어 놓기(상어의 위치는 -1로 표시)
    result += target_fish  # 먹은 물고기 번호를 결과값에 더해주기

    # 물고기 배열을 순회하면서 물고기 위치 바꿔주기
    for fish_num in range(1, 17):
        if fishes[fish_num]:  # 물고기가 존재한다면

            r, c, d = fishes[fish_num]

            time = 0
            while time < 8:
                nr, nc = r + dy[d], c + dx[d]

                # 이동하고자 하는 곳이 범위 안이고, 상어가 아니면
                if 0 <= nr < 4 and 0 <= nc < 4 and ocean[nr][nc] != -1:
                    if ocean[nr][nc] != 0:
                        # 물고기면 위치 바꿔주기
                        fishes[fish_num][0], fishes[fish_num][1] = nr, nc
                        fishes[ocean[nr][nc]][0], fishes[ocean[nr][nc]][1] = r, c
                        ocean[r][c], ocean[nr][nc] = ocean[nr][nc], ocean[r][c]
                    else:
                        # 빈곳이면 이동하기
                        fishes[fish_num][0], fishes[fish_num][1] = nr, nc
                        ocean[r][c], ocean[nr][nc] = ocean[nr][nc], ocean[r][c]
                    break

                # 이동할 수 없으면 방향 += 1
                else:
                    d += 1
                    if d == 9:  # 방향이 9가되면 1로 바꿔줌
                        d = 1
                time += 1

            # 이동에 성공했다면 방향 갱신해주기
            fishes[fish_num][2] = d

    # 상어가 이동할 수 있는 곳들을 찾기
    move_shark_r, move_shark_c = shark[0], shark[1]
    move_shark_r += dy[shark[2]]
    move_shark_c += dx[shark[2]]

    # 이동할 수 있다면 이동하기
    while 0 <= move_shark_r < 4 and 0 <= move_shark_c < 4:

        # 이동했을 때, 물고기가 있다면 재귀함수 수행
        if ocean[move_shark_r][move_shark_c] != 0:
            simulation(shark[0], shark[1], ocean[move_shark_r][move_shark_c], fishes, ocean, result)

        # 다음칸 이동
        move_shark_r += dy[shark[2]]
        move_shark_c += dx[shark[2]]

    # 결과값 갱신하기
    if max_result < result:
        max_result = result
    return


raw_data = [list(map(int, input().split())) for _ in range(4)]

order_by_fishes = [0] * 17  # 물고기의 순서대로 위치와 방향을 저장하는 배열
origin_ocean = [[0] * 4 for _ in range(4)]  # 공간배열
# 0, 상, 좌상, 좌, 좌하, 하, 우하, 우, 우상
dy, dx = [0, -1, -1, 0, 1, 1, 1, 0, -1], [0, 0, -1, -1, -1, 0, 1, 1, 1]

for i in range(4):
    for j in range(8):
        if not j % 2:
            origin_ocean[i][j // 2] = raw_data[i][j]
            order_by_fishes[raw_data[i][j]] = [i, j // 2, raw_data[i][j + 1]]

max_result = 0
simulation(0, 0, origin_ocean[0][0], order_by_fishes, origin_ocean, 0)

print(max_result)
