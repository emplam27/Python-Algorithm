import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_num = 0

    for i in range(N - M + 1):
        for j in range(N - M + 1):
            sum_num = 0
            for k in range(M):
                for l in range(M):
                    sum_num += arr[i + k][j + l]
            if sum_num > max_num:
                max_num = sum_num

    print('#%d' %t, max_num)
