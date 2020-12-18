import sys

sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline


def cal_multiple(num):
    if num == 1:
        return A % C

    value = cal_multiple(num // 2)
    if num % 2 == 0:
        return value * value % C
    else:
        return value * value * A % C


A, B, C = map(int, input().split())
print(cal_multiple(B))
