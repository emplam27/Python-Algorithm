import sys

sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline


def check(size, R, C):

    if size == 1:
        return board[R][C]

    sum_num = 0
    for r in range(R, R + size):
        for c in range(C, C + size):
            sum_num += board[r][c]
    if sum_num == size ** 2 or sum_num == 0:
        return board[R][C]

    half = size // 2
    return f'({check(half, R, C)}{check(half, R, C + half)}{check(half, R + half, C)}{check(half, R + half, C + half)})'


N = int(read())
board = [list(map(int, read().rstrip())) for _ in range(N)]

print(check(N, 0, 0))