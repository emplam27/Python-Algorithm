def solution(n):
    trans, answer = [], 0
    while n > 0:
        i, j = divmod(n, 3)
        trans.append(j)
        n = i
    for order, number in enumerate(trans[::-1]):
        answer += 3**order * number
    return answer