import sys

sys.stdin = open('input.txt', 'r')


def n_queen(r_index):
    global result

    if r_index == N:
        result += 1
        return

    for c_index in range(N):
        if not c_selected[c_index]:
            is_posible = True
            for direction in range(8):
                nr, nc = r_index + dy[direction], c_index + dx[direction]
                while 0 <= nr < N and 0 <= nc < N:
                    if board[nr][nc] == 1:
                        is_posible = False
                        break
                    nr, nc = nr + dy[direction], nc + dx[direction]
                if not is_posible:
                    break
            else:
                board[r_index][c_index] = 1
                c_selected[c_index] = 1
                n_queen(r_index + 1)
                board[r_index][c_index] = 0
                c_selected[c_index] = 0


N = int(input())
board = [[0] * N for _ in range(N)]
dy, dx = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]
c_selected, result = [0] * N, 0
n_queen(0)
print(result)
