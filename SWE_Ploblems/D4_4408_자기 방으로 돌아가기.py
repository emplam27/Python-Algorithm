import sys

sys.stdin = open("input.txt", "r")

for t in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for i in range(len(arr)):
        if arr[i][0] > arr[i][1]:
            arr[i][0], arr[i][1] = arr[i][1], arr[i][0]

    count = 0
    while arr:
        m = 1
        while m < 400:
            for i in range(len(arr)):
                if arr[i][0] == m:
                    if arr[i][1] % 2 == 0:
                        m = arr[i][1]
                    if arr[i][1] % 2 == 1:
                        m = arr[i][1] + 1
                    del arr[i]
                    break
            m += 1
        count += 1

    print('#%d' %t, count)