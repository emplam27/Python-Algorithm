import sys

sys.stdin = open('input.txt', 'r')


T = 1  # int(input())
for t in range(1, T + 1):
    N = 3  # int(input())
    arr = [2, 3, 5]  # list(map(int, input().split()))
    a = sum(arr) + 1
    selected = [0] * a
    selected_list = []
    selected_list.append(0)
    selected[0] = 1

    for i in arr:
        for j in (a - i, -1, -1):
            if selected[j] == 1:
                selected[i + j] = 1

    print('#%d' % t, selected.count(1))