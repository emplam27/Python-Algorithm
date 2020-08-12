def solution(prices):
    answer = [0] * len(prices)

    for index, price in enumerate(prices):
        cur = index + 1
        while cur < len(prices):
            answer[index] += 1
            if prices[cur] < price:
                break
            cur += 1

    return answer