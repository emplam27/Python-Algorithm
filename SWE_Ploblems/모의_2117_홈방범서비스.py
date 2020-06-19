import sys

sys.stdin = open("input2.txt", "r")

# 마름모 문제같은 경우는 각 격자간의 거리로 풀 수도 있다.
def check(r, c):
    global result

    # 퍼질 크기 정하고, 요금 미리 산정
    for K in range(1, N + 2):
        fee = K * K + (K - 1) * (K - 1)
        house = 0
        for dr in range(-(K - 1), (K - 1) + 1):
            nr = r + dr
            if 0 <= nr < N:
                for dc in range(-(K - 1) + abs(dr), (K - 1) + 1 - abs(dr)):
                    nc = c + dc
                    if 0 <= nc < N:
                        if town[nr][nc] == 1:
                            house += 1
        # 손해가 안나기만 하면 되므로 등호가 들어가야 함
        if house * M >= fee and result < house:
            result = house
    return


for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    town = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(N * N):
        check(i // N, i % N)

    print('#%d' %t, result)
