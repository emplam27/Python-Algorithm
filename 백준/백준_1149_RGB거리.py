import sys

sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline

'''
<점화식>
DP[현재집까지 칠하는 비용] = min(이전 집까지 다른색으로 칠했던 비용) + 현재 집을 칠하는 비용
DP[cur_home][색1] = min(DP[cur_home - 1][색2], DP[cur_home - 1][색3]) + home_RGB[cur_home][색1]
'''


def solve():
    N = int(read().rstrip())
    home_RGB = [list(map(int, read().rstrip().split())) for _ in range(N)]
    DP = [[0] * 3 for _ in range(N)]
    DP[0][0], DP[0][1], DP[0][2] = home_RGB[0][0], home_RGB[0][1], home_RGB[0][2]

    for cur_home in range(1, N):
        DP[cur_home][0] = min(DP[cur_home - 1][1], DP[cur_home - 1][2]) + home_RGB[cur_home][0]
        DP[cur_home][1] = min(DP[cur_home - 1][0], DP[cur_home - 1][2]) + home_RGB[cur_home][1]
        DP[cur_home][2] = min(DP[cur_home - 1][0], DP[cur_home - 1][1]) + home_RGB[cur_home][2]
    print(min(DP[-1]))

solve()