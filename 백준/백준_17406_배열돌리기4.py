import sys
sys.stdin = open('input.txt', 'r')


from itertools import permutations


def rotate(board, n, m, k):

    for i in range(1, k + 1):

        # 배열 가져오기
        r, c, d = (n - 1) - i, (m - 1) - i, 0
        numbers = []
        while len(numbers) < 8*i:
            numbers.append(board[r][c])
            if r + dy[d] < (n - 1) - i or r + dy[d] > (n - 1) + i or c + dx[d] < (m - 1) - i or c + dx[d] > (m - 1) + i:
                d += 1
            r, c = r + dy[d], c + dx[d]

        # 한칸이동
        numbers = [numbers[-1]] + numbers[:-1]

        # 배열 옮기기
        r, c, d = (n - 1) - i, (m - 1) - i, 0
        while len(numbers) > 0:
            board[r][c] = numbers.pop(0)
            if r + dy[d] < (n - 1) - i or r + dy[d] > (n - 1) + i or c + dx[d] < (m - 1) - i or c + dx[d] > (m - 1) + i:
                d += 1
            r, c = r + dy[d], c + dx[d]

    return


def check(arr, moves):
    global min_result

    board = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            board[i][j] = arr[i][j]

    for n, m, k in moves:
        rotate(board, n, m, k)

    for i in range(N):
        tmp = sum(board[i])
        if min_result > tmp:
            min_result = tmp
    return


N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
move = [list(map(int, input().split())) for _ in range(K)]
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]  # 우, 하, 좌, 상

move_perms = list(permutations(move, len(move)))

min_result = 2**30
for moves in move_perms:
    check(arr, moves)

print(min_result)