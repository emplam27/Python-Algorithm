import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))

    S = sum(arr)
    selected = [0] * (S + 1)
    selected[0] = 1
    for i in arr:
        for j in range(S, -1, -1):
            if selected[j] == 1:
                selected[j + i] = 1

    result = 0
    for i in range(S + 1):
        if selected[i] == 1 and i >= B:
            result = i
            break


    print('#%d' % t, result - B)

    # 1 1
    # 2 4
    # 3 27
    # 4 11
    # 5 42
    # 6 32
    # 7 2
    # 8 3
    # 9 25
    # 10 0
