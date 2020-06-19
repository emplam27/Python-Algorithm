import sys
sys.stdin = open('input.txt', 'r')


def check(arr):

    value = 0
    for i in range(N//2 - 1):
        for j in range(i + 1, N // 2):
            value += (S[arr[i-1]][arr[j-1]] + S[arr[j-1]][arr[i-1]])
    return value


def combination(idx, count):
    global min_result

    if count > N//2:
        return

    if idx >= N:
        if count == N//2:
            tmp1, tmp2 = [], []
            for i in range(N):
                if selected[i] == 1:
                    tmp1.append(i)
                else:
                    tmp2.append(i)
            tmp_result = abs(check(tmp1) - check(tmp2))
            if min_result > tmp_result:
                min_result = tmp_result
        return

    selected[idx] = 1
    combination(idx + 1, count + 1)
    selected[idx] = 0
    combination(idx + 1, count)


N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

min_result = 2**31
selected = [0] * N
combination(0, 0)

print(min_result)
