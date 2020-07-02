"""
전체 음식을 정렬하여 작은 순서부터 확인한다.
정렬이 제일 복잡한 부분으로 만들어야 한다.
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
