import sys

sys.stdin = open("input.txt", "r")
read = sys.stdin.readline


def solve():
    N = int(read())
    stairs = [0] + [int(read()) for _ in range(N)]
    if N == 1:
        print(stairs[1])
        exit()

    DP = [0] * (N + 1)
    DP[1], DP[2] = stairs[1], stairs[1] + stairs[2]
    for i in range(3, N + 1):
        DP[i] = max(DP[i - 2] + stairs[i], DP[i - 3] + stairs[i] + stairs[i - 1])

    print(DP[-1])


solve()
