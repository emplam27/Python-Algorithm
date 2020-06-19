import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr_i = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    arr_j = [list(map(int, input().split())) for _ in range(P)]
    selected = [0] * len(arr_j)
    for l, r in arr_i:
        for m, n in enumerate(arr_j):
            if l <= n[0] <= r:
                selected[m] += 1

    print('#%d' %t, *selected)