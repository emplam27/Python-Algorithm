for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    count = 0
    cnt = 0
    while count < M:
        count += 1
        cnt += 1
        if cnt == N:
            cnt = 0

    print('#%d' %t, arr[cnt])