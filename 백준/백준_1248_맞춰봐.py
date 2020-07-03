import sys

sys.stdin = open("input.txt", "r")

"""
-10 ~ 10
일단 각 숫자들의 부호는 i와 j가 같을때를 이용해 알아낼 수 있다.
N개짜기 순열을 만들어서, 부호조건에 맞게 바꿔준 뒤, 각 조건에 맞는지 확인 
.. 시간초과로 실패

순열과 중복순열을 사용하니 시간초과. 그렇다면 각각 되는 숫자를 판별하면서 나갈 필요가 있음
각 숫자별로 조건에 부합하는지 따져보자.
"""


def check(candidate):

    # candidate의 구간합 비교
    for i in range(len(candidate)):
        for j in range(i, len(candidate)):

            # 구간합 구하기
            tmp_result = 0
            for k in range(i, j + 1):
                tmp_result += candidate[k]

            # 구간합들 중 조건에 부합하지 않으면 False 반환
            if matrix[i][j] == '+' and tmp_result <= 0:
                return False
            elif matrix[i][j] == '-' and tmp_result >= 0:
                return False
            elif matrix[i][j] == '0' and tmp_result != 0:
                return False

    # 조건에 모두 부합하면 결과물 반환
    return True


def find_numbers(idx, candidate):

    if idx >= N:
        print(*candidate)
        exit(0)
        return

    for num in range(-10, 11):
        # operator 조건에 맞으면서
        if (operators[idx] == '-' and num < 0) or (operators[idx] == '+' and num > 0) \
                or (operators[idx] == '0' and num == 0):
            # 구간합 조건에 부합한다면,
            if check(candidate + [num]):
                # 재귀함수 실행
                find_numbers(idx + 1, candidate + [num])


N = int(input())
tmp_matrix = list(input())
operators = list()
matrix = [[0] * N for _ in range(N)]

# matrix 정리해주기
tmp = 0
for i in range(N):
    for j in range(i, N):
        matrix[i][j] = tmp_matrix[tmp]
        tmp += 1

# 각 수들은 matrix[i][i]와 같은 부호를 같는다.
for i in range(N):
    operators.append(matrix[i][i])

find_numbers(0, [])
