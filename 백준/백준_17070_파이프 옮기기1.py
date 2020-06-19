import sys

# sys.stdin = open('17070_input.txt', 'r')
N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


def move_pipe(r, c, direction):
    global result

    if r >= N or c >= N:
        return

    if (r, c) == (N - 1, N - 1):
        result += 1
        return

    if direction == 0:
        # 우
        if c + 1 < N and arr[r][c + 1] == 0:
            move_pipe(r, c + 1, 0)
        # 우하
        if r + 1 < N and c + 1 < N and arr[r][c + 1] == 0 and arr[r + 1][c + 1] == 0 and arr[r + 1][c] == 0:
            move_pipe(r + 1, c + 1, 1)

    elif direction == 1:
        # 우
        if c + 1 < N and arr[r][c + 1] == 0:
            move_pipe(r, c + 1, 0)
        # 우하
        if r + 1 < N and c + 1 < N and arr[r][c + 1] == 0 and arr[r + 1][c + 1] == 0 and arr[r + 1][c] == 0:
            move_pipe(r + 1, c + 1, 1)
        # 하
        if r + 1 < N and arr[r + 1][c] == 0:
            move_pipe(r + 1, c, 2)

    else:
        # 우하
        if r + 1 < N and c + 1 < N and arr[r][c + 1] == 0 and arr[r + 1][c + 1] == 0 and arr[r + 1][c] == 0:
            move_pipe(r + 1, c + 1, 1)
        # 하
        if r + 1 < N and arr[r + 1][c] == 0:
            move_pipe(r + 1, c, 2)



dy, dx = [0, 1, 1], [1, 1, 0]  # 우, 우하, 하

result = 0
move_pipe(0, 1, 0)
print(result)