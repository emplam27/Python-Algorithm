import sys

sys.stdin = open("input.txt", "r")


def check(idx, selected, count1):

    if idx >= N:
        if count1 == N // 2:
            tmp1, tmp2 = list(), list()
            for i in range(N):
                if selected[i] == 1:
                    tmp1.append(nums[i])
                elif selected[i] == 0:
                    tmp2.append(nums[i])
            com1.append(tmp1)
            com2.append(tmp2)
        return

    if count1 > N // 2:
        return

    selected[idx] = 1
    check(idx + 1, selected, count1 + 1)
    selected[idx] = 0
    check(idx + 1, selected, count1)


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    nums = [a for a in range(N)]
    selected = [0] * N

    com1, com2 = list(), list()
    check(0, selected, 0)

    result = 10000
    for k in range(len(com1)):
        synergy1, synergy2 = 0, 0
        for i in range(N // 2):
            for j in range(i + 1, N // 2):
                synergy1 = synergy1 + arr[com1[k][i]][com1[k][j]] + arr[com1[k][j]][com1[k][i]]
                synergy2 = synergy2 + arr[com2[k][i]][com2[k][j]] + arr[com2[k][j]][com2[k][i]]
        if abs(synergy1 - synergy2) < result:
            result = abs(synergy1 - synergy2)

    print('#%d' % t, result)