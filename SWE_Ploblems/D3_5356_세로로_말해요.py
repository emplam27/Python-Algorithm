import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T + 1):
    arr = [str(input()) for _ in range(5)]

    max_len = 0
    for i in range(5):
        if len(arr[i]) > max_len:
            max_len = len(arr[i])

    board = [[0] * max_len for _ in range(5)]

    for i in range(5):
        L = len(arr[i])
        for j in range(L):
            board[i][j] = arr[i][j]

    result = ''
    for c in range(max_len):
        for r in range(5):
            if board[r][c] != 0:
                result += board[r][c]

    print('#%d' %t, result)
