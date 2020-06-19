import sys

sys.stdin = open("14888_input.txt", "r")


def dfs(cal, idx, plus, minus, multiple, division):
    global max_num, min_num
    if idx == N:
        if max_num < cal:
            max_num = cal
        if min_num > cal:
            min_num = cal
        return
    else:
        if plus != 0:
            dfs(cal + arr[idx], idx + 1, plus - 1, minus, multiple, division)
        if minus != 0:
            dfs(cal - arr[idx], idx + 1, plus, minus - 1, multiple, division)
        if multiple != 0:
            dfs(cal * arr[idx], idx + 1, plus, minus, multiple - 1, division)
        if division != 0:
            # dfs(cal // arr[idx], idx + 1, plus, minus, multiple, division - 1)
            dfs(int(cal / arr[idx]), idx + 1, plus, minus, multiple, division - 1)


N = int(input())
arr = list(map(int, input().split()))
plus, minus, multiple, division = list(map(int, input().split()))
result = []
max_num = -1000000000
min_num = 1000000000

dfs(arr[0], 1, plus, minus, multiple, division)

print(max_num)
print(min_num)