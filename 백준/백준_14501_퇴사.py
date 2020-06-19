import sys
sys.stdin = open("input.txt", "r")


def check(idx, selected, result):
    global max_result

    if idx > N:
        return

    if idx == N:
        if max_result < result:
            max_result = result
        return

    selected[idx] = 1
    check(idx + schedule[idx][0], selected, result + schedule[idx][1])
    selected[idx] = 0
    check(idx + 1, selected, result)


N = int(input())
schedule = [list(map(int, input().split())) for _ in range(N)]

max_result = 0
selected = [0] * N
check(0, selected, 0)

print(max_result)