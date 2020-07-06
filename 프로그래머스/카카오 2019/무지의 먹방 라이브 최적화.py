"""
전체 음식을 정렬하여, 음식량이 적은 순서부터 (음식량 * 음식수)의 값과 k를 비교하며 진행한다.
k값이 큰 경우에는 k값에서 해당 값을 빼주고 다음 음식량과 비교를 진행하고,
k값이 작은경우에는 원본배열에서 해당 음식량보다 큰 음식들을 조사하면서 index를 찾아준다.
실패..

한 음식량씩 비교하면서 진행하면 시간초과가 난다. (현재 음식량 - 이전 음식량) * 음식수 처럼
불필요한 계산을 최소화해서 처리해주는 로직이 들어가야만 한다.
"""


def solution(food_times, k):
    # 원본배열을 남겨두고 음식량 정렬배열 생성
    order_food_times = food_times[:]
    order_food_times.sort()

    # 음식량을 순회하면서 해당 음식량을 넘는 음식수를 찾아 k에서 빼준다.
    index, cycle, prev_cycle = 0, 1, 0
    # for cycle in range(1, 1000000000):

    while True:

        # cycle의 값과 같은 음식량을 가지는 음식 찾기
        while index < len(food_times):
            if order_food_times[index] > prev_cycle:
                cycle = order_food_times[index]
                break
            index += 1

        # k값이 모든 음식량의 합을 넘으면 -1 반환
        if index >= len(food_times):
            return -1

        # k에서 (cycle - prev_cycle) * 음식수를 빼주었을 때, k가 양수이면 다음 cycle 진행
        if k - (cycle - prev_cycle) * (len(food_times) - index) >= 0:
            k -= (cycle - prev_cycle) * (len(food_times) - index)
            prev_cycle = cycle
            continue

        # k가 음수이면 해당 cycle에서 멈춤
        else:
            prev_cycle += k // (len(food_times) - index)
            k = k % (len(food_times) - index)

            # 원본배열에서 앞에서부터 음식량이 cycle보다 큰 음식들을 조사
            for order, value in enumerate(food_times):
                if value > prev_cycle:
                    if k == 0:
                        return order + 1
                    k -= 1



print(solution([3, 3, 4, 1], 10))
