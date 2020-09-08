from collections import deque


def solution(stones, k):
    answer = 0

    stones_dict = dict()
    for index, stone in enumerate(stones):
        if not stones_dict.get(stone):
            stones_dict[stone] = [index + 1]
        else:
            stones_dict[stone].append(index + 1)

    print(stones_dict)
    zero_list = []
    # while True:
    #     for key in

    return answer