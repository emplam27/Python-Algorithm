T = int(input())

for t in range(1, T+1):
    L, U, X = map(int, input().split())

    result = 0
    if X < L:
        result = L - X
    elif X > U:
        result = -1

    print('#%d' %t, result)