import sys

sys.stdin = open("input.txt", "r")


def dfs(num, idx):
    if num == 1:
        tmp = arr.pop(0)
        idx = s_idx.pop(0)
        return tmp, idx

    elif num % 2 == 1:
        tmp1, idx1 = dfs(num // 2 + 1, idx)
        tmp2, idx2 = dfs(num // 2, idx)

        if tmp1 == tmp2:
            return tmp1, idx1
        elif tmp1 == 3 and tmp2 == 1:
            return tmp2, idx2
        elif tmp1 == 1 and tmp2 == 3:
            return tmp1, idx1
        elif tmp1 < tmp2:
            return tmp2, idx2
        elif tmp1 > tmp2:
            return tmp1, idx1

    elif num % 2 == 0:
        tmp3, idx3 = dfs(num // 2, idx)
        tmp4, idx4 = dfs(num // 2, idx)

        if tmp3 == tmp4:
            return tmp3, idx3
        elif tmp3 == 3 and tmp4 == 1:
            return tmp4, idx4
        elif tmp3 == 1 and tmp4 == 3:
            return tmp3, idx3
        elif tmp3 < tmp4:
            return tmp4, idx4
        elif tmp3 > tmp4:
            return tmp3, idx3


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    s_idx = []
    for i in range(1, N + 1):
        s_idx += [i]

    print('#%d' % t, dfs(N, N)[1])

