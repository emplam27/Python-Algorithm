def solution(m, n, board):
    answer = 0
    board = list(map(list, zip(*board[::-1])))

    while True:
        delete_block = []
        for i in range(n - 1):
            for j in range(m - 1):
                if board[i][j] and board[i][j] == board[i + 1][j] == board[i][j + 1] == board[i + 1][j + 1]:
                    delete_block.extend([[i, j], [i + 1, j], [i, j + 1], [i + 1, j + 1]])

        if not delete_block:
            break

        for i, j in delete_block:
            board[i][j] = 0

        for i in range(n):
            tmp_arr, zero = [], 0
            for j in range(m):
                if board[i][j] != 0:
                    tmp_arr.append(board[i][j])
                else:
                    zero += 1
            tmp_arr += [0] * zero
            board[i] = tmp_arr

    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                answer += 1

    return answer