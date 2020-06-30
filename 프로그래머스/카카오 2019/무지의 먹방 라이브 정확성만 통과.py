def find_index(index, food_times):
    tmp_time = 0
    while tmp_time <= len(food_times):
        index += 1
        tmp_time += 1
        if index >= len(food_times):
            index = 0
        if food_times[index]:
            # print('index:', index)
            return index, food_times
    return -1, food_times


def solution(food_times, k):
    time, index = 0, len(food_times)
    index, foodtimes = find_index(index, food_times)

    while time < k:

        # 해당 index의 음식을 하나씩 빼기
        food_times[index] -= 1
        # print(food_times)

        # 배열을 순회하면서 index 정하기
        index, food_times = find_index(index, food_times)
        if index == -1:
            return -1

        time += 1

    return index + 1


print(solution([3, 1, 2], 5))
