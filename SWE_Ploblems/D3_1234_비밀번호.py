import sys

sys.stdin = open("input.txt", "r")

T = 10
for t in range(1, T + 1):
    N, num = map(str, input().split())
    N = int(N)
    arr = [num[i] for i in range(N)]

    while True:
        for i in range(1, len(arr)):
            if arr[i-1] == arr[i]:
                arr.pop(i-1)
                arr.pop(i-1)
                break
        else:
            break

    result = ''
    for i in arr:
        result += i
    print('#%d' %t, result)
