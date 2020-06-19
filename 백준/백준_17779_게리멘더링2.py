import sys
sys.stdin = open("input.txt", "r")


# 17770 게리멘더링2

# <해야할 일>
# 1. 선거구를 5개로 나누기, 나누는 방법은 여러가지가 있으므로, 완전탐색 해야함.
#   문제에서 선거구를 어떤 수식으로 구할것인지 언질을 줬기 때문에 참고가능
# 2. 선거구를 나눴으면, 5번 선거구는 모양이 불규칙해 가장 나중에 구하고,
#   나머지 선거구는 범위가 정해져 있으므로, 5번 선거구를 피해 for문을 이용하여 구한다.

# <주의할 점>
# 좌표 시작이 (1, 1)
# d1, d2 >= 1, x >= 1, y >= 2



def check(r, c, d_1, d_2):
    global min_result

    visited = [[0] * N for _ in range(N)]
    values = [0] * 5  # 선거구의 값들을 저장할 배열

    # 5번 선거구 경계선 만들기
    for i in range(d_1 + 1):
        visited[r + i][c - i] = 5
    for i in range(1, d_2 + 1):
        visited[r + i][c + i] = 5
    for i in range(1, d_2 + 1):
        visited[r + d_1 + i][c - d_1 + i] = 5
    for i in range(1, d_1):
        visited[r + d_2 + i][c + d_2 - i] = 5

    # 각 선거구 값 구하기
    # 1번
    for i in range(r + d_1):
        for j in range(c + 1):
            if visited[i][j] == 5:
                break
            values[0] += board[i][j]
            visited[i][j] = 1
    # 2번
    for i in range(r + d_2 + 1):
        for j in range(N-1, c, -1):
            if visited[i][j] == 5:
                break
            values[1] += board[i][j]
            visited[i][j] = 2

    # 3번
    for i in range(r + d_1, N):
        for j in range(c - d_1 + d_2):
            if visited[i][j] == 5:
                break
            values[2] += board[i][j]
            visited[i][j] = 3

    # 4번
    for i in range(N-1, r + d_2, -1):
        for j in range(N-1, c - d_1 + d_2 - 1, -1):
            if visited[i][j] == 5:
                break
            values[3] += board[i][j]
            visited[i][j] = 4

    # 5번
    values[4] = sum_board - values[0] - values[1] - values[2] - values[3]

    tmp_result = max(values) - min(values)
    if min_result > tmp_result:
        min_result = tmp_result

    return


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
sum_board = 0
for i in range(N):
    sum_board += sum(board[i])

min_result = 2**30
for r in range(N - 2):  # 0 <= r <= N-2
    for c in range(1, N-1):  # 1 <= c <= N-1
        for d_1 in range(1, N-1):  # d_1, d_2 >= 1
            for d_2 in range(1, N-1):
                if 0 <= r < r + d_1 + d_2 < N and 0 <= c - d_1 < c < c + d_2 < N:
                    check(r, c, d_1, d_2)

print(min_result)