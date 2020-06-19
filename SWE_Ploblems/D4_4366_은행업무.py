import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    arr2 = list(map(int, list(input())))
    arr3 = list(map(int, list(input())))
    len_arr2, len_arr3 = len(arr2), len(arr3)

    candidate2 = []
    for i in range(len_arr2):
        arr2[i] = (arr2[i] + 1) % 2
        tmp = 0
        for k in range(len_arr2):
            if arr2[k] == 1:
                tmp += 2**(len_arr2 - k - 1)
        candidate2.append(tmp)
        arr2[i] = (arr2[i] + 1) % 2

    candidate3 = []
    for i in range(len_arr3):
        for j in range(2):
            arr3[i] = (arr3[i] + 1) % 3
            tmp = 0
            for k in range(len_arr3):
                if arr3[k] == 1:
                    tmp += 3 ** (len_arr3 - k - 1)
                elif arr3[k] == 2:
                    tmp += 2 * (3 ** (len_arr3 - k - 1))
            candidate3.append(tmp)
        arr3[i] = (arr3[i] + 1) % 3

    for i in candidate2:
        for j in candidate3:
            if i == j:
                result = i
                break

    print('#%d' %t, result)
