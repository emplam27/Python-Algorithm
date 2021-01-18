import sys

sys.stdin = open("input.txt", "r")
read = sys.stdin.readline

'''
DP는 해당 구간까지 마실 수 있는 와인의 최댓값
<점화식>
현재 구간 i에서 마시지 않았을 때 => 이전까지의 최대값을 그대로 가져온다.
                               => DP[i] = DP[i - 1]
현재 구간 i에서 1잔을 연속으로 마신 상태일 때 => i번째 포도주는 마시고, i-1번째 포도주는 마시지 않고, i-2번째 최대값을 가져온다.
                                           => DP[i] = DP[i - 2] + wines[i]
현재 구간 i에서 2잔을 연속으로 마신 상태일 때 => i, i-1번째 포도주는 마시고, i-2번째 포도주는 마시지 않고, i-3번째 최대값을 가져온다.
                                           => DP[i] = DP[i - 3] + wines[i] + wines[i - 1]
'''


def solve():
    N = int(read())
    wines = [0] + [int(read()) for _ in range(N)]
    if N == 1:
        print(wines[1])
        exit()

    DP = [0] * (N + 1)
    DP[1], DP[2] = wines[1], wines[1] + wines[2]

    for i in range(3, N + 1):
        DP[i] = max(DP[i - 2] + wines[i], DP[i - 3] + wines[i] + wines[i - 1])
        DP[i] = max(DP[i - 1], DP[i])

    print(DP[-1])


solve()
