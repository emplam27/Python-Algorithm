import sys

sys.stdin = open("input.txt", "r")

"""
40분

제약조건을 2차원 배열로 만들어서 그래프의 연결노드처럼 만들면 편할 듯.
제약조건인 경우에만 1로 표시하고, combination을 수행할 때 1이 들어가있는 경우에는 재료를 추가하지 않기로 하자.
"""


def combination(idx, selected):
    global result

    if idx >= N:
        result += 1
        return

    # 어울리지 않는 재료가 이미 들어가있으면, 이 재료를 선택하지 않는 경우만 수행함
    for i in range(N):
        if i != idx and mismatch[idx][i] and selected[i]:
            selected[idx] = 0
            combination(idx + 1, selected)
            return

    selected[idx] = 1
    combination(idx + 1, selected)
    selected[idx] = 0
    combination(idx + 1, selected)


for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    constraints = [list(map(int, input().split())) for _ in range(M)]
    mismatch = [[0] * N for _ in range(N)]

    for i, j in constraints:
        mismatch[i - 1][j - 1] = mismatch[j - 1][i - 1] = 1

    selected, result = [0] * N, 0
    combination(0, selected)
    print('#{} {}'.format(t, result))
