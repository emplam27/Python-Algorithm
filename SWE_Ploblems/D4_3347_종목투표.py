import sys

sys.stdin = open("input.txt", "r")

for t in range(1, int(input()) + 1):
    N, M = map(int,input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    selected = [0] * N
    for i in range(len(arr2)):  # 위원회
        for j in range(len(arr1)):  # 종목
            if arr1[j] <= arr2[i]:
                selected[j] += 1
                break

    print('#%d' %t, selected.index(max(selected)) + 1)