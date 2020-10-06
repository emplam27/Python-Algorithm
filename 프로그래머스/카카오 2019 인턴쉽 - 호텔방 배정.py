"""
아이디어
한개의 방을 골랐을때, 들어갈 수 있는 방의 번호를 저장하자.
'dict[들어가려는 방] = 가야하는 방'으로 저장하자
"""

import sys

sys.setrecursionlimit(100000)


def solution(k, room_number):
    answer = []

    def find_empty_room(number, room_dict):
        if room_dict.get(number) is None:
            room_dict[number] = number + 1
            return number

        else:
            next_room = find_empty_room(room_dict[number], room_dict)
            room_dict[number] = next_room + 1
            return next_room

    # 점프할 횟수를 저정하는 dict
    room_dict = dict()
    for number in room_number:
        empty_room = find_empty_room(number, room_dict)
        answer.append(empty_room)

    return answer


print(solution(10, [1, 3, 4, 1, 3, 1]))
