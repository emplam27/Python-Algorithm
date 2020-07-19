"""
hash 만들기
"""


def solution(k, room_number):
    answer = []

    candidate_numbers = [i for i in range(1, k + 1)]
    candidate_dict = dict()
    for i in range(1, k + 1):
        candidate_dict[i] = 0

    print(candidate_numbers)
    print(candidate_dict)
    # room_dict = dict()
    # for number in room_number:
    #     while number <= k:
    #         if not room_dict.get(number):
    #             room_dict[number] = 1
    #             answer.append(number)
    #             break
    #         else:
    #             number += 1

    return answer