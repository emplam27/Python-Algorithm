import sys

sys.stdin = open('input.txt', 'r')

# 1시간 20분
# 배열 돌리는거 다시 공부하기


# <해야할 일>
# 1. 완전 탐색을 이용하여 푼다.
# 2. 배열을 돌려가며 풀 예정. 움직이는 로직은 하나만 구현하고,
#   배열을 돌렸다가 움직이고 다시 원래대로 돌린다.
# 시간초과가 안날까 걱정


import copy


def move_board(copied_board):

    for i in range(N):
        for j in range(N):
            if copied_board[i][j] != 0:
                value, target = j, j + 1
                break
        else:
            continue

        # 같은 숫자 합치기
        while target < N:
            if copied_board[i][value] == copied_board[i][target]:
                copied_board[i][value] *= 2
                copied_board[i][target] = 0
                value = target + 1
                target = value + 1
            elif copied_board[i][target] == 0:
                target += 1
            else:
                value += 1
                target = value + 1

        # 0 없애기
        tmp_list, tmp_num = [], 0
        for k in range(N):
            if copied_board[i][k] != 0:
                tmp_list.append(copied_board[i][k])
                tmp_num += 1
        tmp_list.extend([0] * (N - tmp_num))
        copied_board[i] = tmp_list


def rotate_board(arr):
    global max_result

    copied_board = copy.deepcopy(board)

    for i in arr:
        if i == 0:    # 좌
            move_board(copied_board)  # 그대로

        elif i == 1:  # 우
            copied_board = list(map(list, zip(*copied_board)))[::-1]  # 좌로 90도
            copied_board = list(map(list, zip(*copied_board)))[::-1]  # 좌로 90도
            move_board(copied_board)
            copied_board = list(map(list, zip(*copied_board[::-1])))  # 우로 90도
            copied_board = list(map(list, zip(*copied_board[::-1])))  # 우로 90도

        elif i == 2:  # 상
            copied_board = list(map(list, zip(*copied_board)))[::-1]  # 좌로 90도
            move_board(copied_board)
            copied_board = list(map(list, zip(*copied_board[::-1])))  # 우로 90도

        elif i == 3:  # 하
            copied_board = list(map(list, zip(*copied_board[::-1])))  # 우로 90도
            move_board(copied_board)
            copied_board = list(map(list, zip(*copied_board)))[::-1]  # 좌로 90도

    # 최고값 구하기
    for i in range(N):
        if max_result < max(copied_board[i]):
            max_result = max(copied_board[i])
    return


def make_order(idx):

    if idx >= 5:
        rotate_board(orders)
        return

    for i in range(4):
        orders[idx] = i
        make_order(idx + 1)


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

max_result = 0
orders = [0] * 5
make_order(0)

print(max_result)


