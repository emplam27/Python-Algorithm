import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T + 1):
    arr = [list(map(int, input().split())) for i in range(9)]
    result1 = 1
    result2 = 1

    # 가로, 세로의 모든 합을 조사한다.
    for r in range(9):
        sum_r = 0
        sum_c = 0
        for c in range(9):
            sum_r += arr[r][c]
            sum_c += arr[c][r]
        if sum_r != 45 or sum_c != 45:
            result1 = 0

    # 사각형 안의 수를 조사한다.
    sum_s = 0
    for i in range(3):
        for j in range(3):
            sum_s = 0
            for k in range(3):
                for l in range(3):
                    # 3i+k, 3j+l을 이용하여 격자를 구성한다.
                    sum_s += arr[3*i + k][3*j + l]

            # 사각형 안의 수의 합이 45가 아니면 종료한다.
            if sum_s != 45:
                result2 = 0
                break

    if result1 and result2:
        print('#%d' % t, 1)
    else:
        print('#%d' % t, 0)