import sys
from itertools import combinations

sys.stdin = open("input.txt", "r")


def choice_res(index, res_comb, house_select):
    global min_result

    if index >= house_num:
        tmp_result, selected_res = 0, [0] * cur_res_num
        for i in range(house_num):
            if not selected_res[house_select[i]]:
                selected_res[house_select[i]] = 1
                tmp_result += board[res_loc[house_select[i]][0]][res_loc[house_select[i]][1]]
            tmp_result += abs(house_loc[i][0] - res_loc[house_select[i]][0]) + abs(house_loc[i][1] - res_loc[house_select[i]][1])
        min_result = min(min_result, tmp_result)
        return

    for cur_res in range(cur_res_num):
        house_select[index] = cur_res
        choice_res(index + 1, res_comb, house_select)
    return


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    # 식당 위치 구하기
    res_num, res_loc, house_num, house_loc = 0, [], 0, []
    for i in range(N ** 2):
        if board[i // N][i % N] >= 2:
            res_num += 1
            res_loc.append([i // N, i % N])
        elif board[i // N][i % N] == 1:
            house_num += 1
            house_loc.append([i // N, i % N])

    # 식당 갯수만큼 순서대로 조합하여 식당 결정
    min_result = 2**31
    for cur_res_num in range(1, res_num + 1):
        res_comb = list(map(list, combinations(range(res_num), cur_res_num)))

        # 각 집에서 가장 가까운 식당을 선정하여 비용 구하기
        for tmp_comb in res_comb:  # 조합중 하나를 고른 후
            choice_res(0, tmp_comb, [0] * house_num)

    print('#%d' % t, min_result)
