import sys

sys.stdin = open("input.txt", "r")


def check(num, idx, arr, pl, mi, mu, di):
    global max_num, min_num
    if idx == N:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
        return

    if pl > 0:
        check(num + arr[idx], idx + 1, arr, pl - 1, mi, mu, di)
    if mi > 0:
        check(num - arr[idx], idx + 1, arr, pl, mi - 1, mu, di)
    if mu > 0:
        check(num * arr[idx], idx + 1, arr, pl, mi, mu - 1, di)
    if di > 0:
        check(int(num / arr[idx]), idx + 1, arr, pl, mi, mu, di - 1)


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    pl, mi, mu, di = map(int, input().split())
    arr = list(map(int, input().split()))

    max_num = -100000000
    min_num = 100000000
    check(arr[0], 1, arr, pl, mi, mu, di)

    result = max_num - min_num
    print('#{} {}'.format(t, result))