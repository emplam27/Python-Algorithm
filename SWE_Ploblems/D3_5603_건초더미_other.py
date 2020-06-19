import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [int(input()) for _ in range(N)]
    cnt = 0
    avg = 0

    for i in range(N):
        avg += arr[i]
    avg = avg // N

    for i in range(N):
        if arr[i] > avg:
            cnt = cnt + arr[i] - avg

    print('#%d' % t, cnt)




    # while arr[N-1] != avg:
    #     for i in range(N):
    #         if arr[i] < avg:
    #             arr[i] += 1
    #             break
    #     for i in range(N):
    #         if arr[i] > avg:
    #             arr[i] -= 1
    #             break
    #     cnt += 1



