import sys

sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline

'''
점화식
DP[step][speed] = min(DP[step - speed][speed - 1], DP[step - speed][speed], DP[step - speed][speed + 1]) + 1
'''


def solve():
    N, M = map(int, read().rstrip().split())
    max_speed = int((2 * N) ** 0.5) + 1
    DP = [[float('inf')] * (max_speed + 1) for _ in range(N + 1)]
    small_stone = set()
    for _ in range(M):
        small_stone.add(int(read().rstrip()))

    DP[2][1] = 1
    for step in range(3, N + 1):
        if step in small_stone:
            continue
        for speed in range(1, max_speed):
            DP[step][speed] = min(DP[step - speed][speed - 1], DP[step - speed][speed], DP[step - speed][speed + 1]) + 1

    answer = min(DP[N])
    if answer == float('inf'):
        print(-1)
    else:
        print(answer)


solve()

