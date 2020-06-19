import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]


    # 1
    arr1 = list(zip(*arr[::-1]))
    arr2 = list(zip(*arr1[::-1]))
    arr3 = list(zip(*arr2[::-1]))

    print(arr1)
    print(arr2)
    print(arr3)



    # 2
    arr90 = [[0]*N for _ in range(N)]
    arr180 = [[0] * N for _ in range(N)]
    arr270 = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            arr90[i][j] = arr[(N - 1) - j][i]
            arr180[i][j] = arr[(N - 1) - i][(N - 1) - j]
            arr270[i][j] = arr[j][(N - 1) - i]

    print('#%d' % t)
    for i in range(N):
        for j in range(N):
            print(arr90[i][j], end='')
        print(' ', end='')
        for j in range(N):
            print(arr180[i][j], end='')
        print(' ', end='')
        for j in range(N):
            print(arr270[i][j], end='')
        print()