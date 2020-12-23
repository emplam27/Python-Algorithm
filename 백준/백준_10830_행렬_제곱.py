import sys

sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline


def check_modular(power):
    def mod_1000(num):
        return num % 1000

    def multiple_matrix(matrix_a, matrix_b):
        new_matrix = []
        for r in range(N):
            tmp_arr = []
            for c in range(N):
                tmp_result = 0
                for v in range(N):
                    tmp_result += (matrix_a[r][v] * matrix_b[v][c])
                tmp_arr.append(tmp_result)
            new_matrix.append(tmp_arr)
        return [list(map(mod_1000, value)) for value in new_matrix]

    if power == 1:
        return [list(map(mod_1000, value)) for value in matrix]

    value = check_modular(power // 2)
    if power % 2:
        return multiple_matrix(multiple_matrix(value, value), matrix)
    else:
        return multiple_matrix(value, value)


N, B = map(int, read().rstrip().split())
matrix = [list(map(int, read().rstrip().split())) for _ in range(N)]

matrix = check_modular(B)
for index in range(N):
    print(*matrix[index])
