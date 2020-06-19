import sys

sys.stdin = open("1244_input.txt", "r")


def check(idx, result):
    global max_result

    if idx == N:
        tmp_number = int(''.join(number))
        if max_result < tmp_number:
            max_result = tmp_number
        return

    for i in range(len(number) - 1):
        for j in range(len(number)-1, i, -1):
            number[i], number[j] = number[j], number[i]
            tmp = int(''.join(number))
            if tmp not in visited[idx]:
                visited[idx].append(tmp)
                check(idx + 1, int(''.join(number)))
            number[i], number[j] = number[j], number[i]


T = int(input())

for t in range(1, T + 1):
    number, N = input().split()
    number, N = list(number), int(N)

    max_result = 0
    visited = [[] for _ in range(N)]
    check(0, 0)
    print('#%d' % t, max_result)
