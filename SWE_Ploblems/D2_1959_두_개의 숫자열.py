import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    Ai = list(map(int, input().split()))
    Bj = list(map(int, input().split()))
    sum_num = 0
    max_num = 0

    if len(Ai) > len(Bj):
        for i in range(len(Ai)-len(Bj)+1):
            sum_num = 0
            for j in range(len(Bj)):
                sum_num += Ai[i + j] * Bj[j]
            if sum_num > max_num:
                max_num = sum_num

    if len(Ai) < len(Bj):
        for i in range(len(Bj)-len(Ai)+1):
            sum_num = 0
            for j in range(len(Ai)):
                sum_num += Ai[j] * Bj[i + j]
            if sum_num > max_num:
                max_num = sum_num

    print('#%d' %t, max_num)
