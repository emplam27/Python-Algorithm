"""
dictionary를 이용해서 한번에 순회하는 방향으로 해보자.
역시 정확성만 맞고 효율성에서는 틀린다.
"""


def solution(foodtimes, k):
    food_times = dict()
    for index, food in enumerate(foodtimes):
        food_times[index + 1] = food

    while k - len(food_times) >= 0:
        k -= len(food_times)

        tmp_dict = dict()
        for key, value in food_times.items():
            if value > 1:
                tmp_dict[key] = value - 1

        if len(tmp_dict) == 0:
            return -1

        food_times = tmp_dict

    return list(food_times.keys())[k]


print(solution([3, 1, 2], 5))
