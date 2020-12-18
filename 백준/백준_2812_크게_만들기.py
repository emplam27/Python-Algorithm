import sys

sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**6)
read = sys.stdin.readline


def make_number(index, value):
    global max_result

    if len(value) == N - K:
        tmp_result = 0
        for index, num in enumerate(value):
            tmp_result += 10**(N - K - index - 1) * num
        max_result = max(max_result, tmp_result)
        return

    if index == N:
        return

    make_number(index + 1, value + [number[index]])
    make_number(index + 1, value)


N, K = map(int, read().split())
number = list(map(int, list(read())))
max_result = 0
make_number(0, [])
print(max_result)
