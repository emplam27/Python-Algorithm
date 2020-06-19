import sys

sys.stdin = open('input.txt', 'r')


def rule(arr):
    while True:
        for i in range(1, 6):
            tmp = arr.pop(0)
            tmp -= i
            if tmp <= 0:
                tmp = 0
                arr.append(tmp)
                return arr
            else:
                arr.append(tmp)


T = 10
for t in range(1, T + 1):
    N = map(int, input().split())
    arr = list(map(int, input().split()))
    print('#%d' %t, *rule(arr))

