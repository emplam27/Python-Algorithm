import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    nums = input()
    result = set()

    circle = nums
    for k in range(N//4):
        tmp_cnt = 0
        tmp = ''
        for j in range(N):
            tmp += circle[j:j+1]
            if j % (N//4) == (N//4) - 1:
                tmp_sum = 0
                for i in range(N//4):
                    if tmp[N//4 - i - 1] == 'A':
                        tmp_sum += 10 * (16 ** i)
                    elif tmp[N//4 - i - 1] == 'B':
                        tmp_sum += 11 * (16 ** i)
                    elif tmp[N//4 - i - 1] == 'C':
                        tmp_sum += 12 * (16 ** i)
                    elif tmp[N//4 - i - 1] == 'D':
                        tmp_sum += 13 * (16 ** i)
                    elif tmp[N//4 - i - 1] == 'E':
                        tmp_sum += 14 * (16 ** i)
                    elif tmp[N//4 - i - 1] == 'F':
                        tmp_sum += 15 * (16 ** i)
                    else:
                        tmp_sum += int(tmp[N//4 - i - 1]) * (16 ** i)
                result.add(tmp_sum)
                tmp = ''
        circle = circle[1:] + circle[0]

    result = list(result)
    result.sort(reverse=True)

    print('#%d' %t, result[K - 1])