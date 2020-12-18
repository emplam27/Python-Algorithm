import sys

# sys.setrecursionlimit(10 * 6)

sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline


def cal_multiple(num):
    if calculated.get(num) is not None:
        return calculated[num]

    number_a = calculated.get(num // 2, cal_multiple(num // 2))
    number_b = calculated.get(num - (num // 2), cal_multiple(num - (num // 2)))
    calculated[num] = number_a * number_b % C

    return number_a * number_b


A, B, C = map(int, read().split())
remainder = A % C
calculated = dict({0: 0, 1: remainder})
cal_multiple(B)
print(calculated[B])
