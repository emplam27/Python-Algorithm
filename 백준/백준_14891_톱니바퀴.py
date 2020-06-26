import sys

sys.stdin = open("input.txt", "r")

"""
50분

<주의할 점>
1. 톱니바퀴가 돌 때 주변 말고 다른 톱니바퀴까지 어떻게 돌릴까. 돌아야 할 톱니바퀴를 모두 결정한 후에
    일괄적으로 이동시키는게 좋지 않을까. 모아놓고 한번에 돌리도록 하자.
"""

gears = [list(map(int, input())) for _ in range(4)]
K = int(input())
moves = [list(map(int, input().split())) for _ in range(K)]

# 1: 시계방향, -1: 반시계방향 / 0: N극, 1: S극
for gear, move in moves:
    clockwise, counterclockwise = [], []

    # 움직이는 기어
    if move == 1:
        clockwise.append(gear - 1)
    else:
        counterclockwise.append(gear - 1)

    queue = [[gear - 1, move]]
    while queue:
        cur_gear, cur_move = queue.pop(0)

        # 오른쪽 기어 검증
        if (cur_gear + 1 < 4) and (cur_gear + 1 not in clockwise) and (cur_gear + 1 not in counterclockwise):
            if gears[cur_gear][2] != gears[cur_gear + 1][6]:
                if cur_move == 1:
                    queue.append([cur_gear + 1, -1])
                    counterclockwise.append(cur_gear + 1)
                else:
                    queue.append([cur_gear + 1, 1])
                    clockwise.append(cur_gear + 1)

        # 왼쪽기어 검증
        if (0 <= cur_gear - 1) and (cur_gear - 1 not in clockwise) and (cur_gear - 1 not in counterclockwise):
            if gears[cur_gear][6] != gears[cur_gear - 1][2]:
                if cur_move == 1:
                    queue.append([cur_gear - 1, -1])
                    counterclockwise.append(cur_gear - 1)
                else:
                    queue.append([cur_gear - 1, 1])
                    clockwise.append(cur_gear - 1)

    # 모든 이동 검증이 끝난 후 이동시작
    for i in clockwise:
        gears[i] = [gears[i][-1]] + gears[i][:-1]
    for i in counterclockwise:
        gears[i] = gears[i][1:] + [gears[i][0]]

# 결과값 구하기
result = 0
for i in range(4):
    if gears[i][0] == 1:
        result += 2 ** i

print(result)
