# 1시간 10분

# 주사위의 이동에 대해 심각하게 고민할 것
# 주사위가 이동함에 따라 주사위를 어떤식으로 배치해야할지 고민해야 한다.



import sys
sys.stdin = open('input.txt', 'r')


N, M, X, Y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
orders = list(map(int, input().split()))

# 주사위 구성 : 굴리면 기존의 숫자들이 어디로 이동하는지
# 정상        우       좌       상       하
#   1         1        1        0        5
# 3 0 2     5 3 0    0 2 5    3 4 2    3 1 2
#   4         4        4        5        0
#   5         2        3        1        4
# 1 <=> 6, 3 <=> 4, 2 <=> 5

dice = [
    [0, 0, 0, 0, 0, 0],  # 각 면이 가지고 있는 수
    # 우, 좌, 상, 하로 굴렸을 때, 맨 위에 어떠한 숫자로 바뀌는지
    [3, 1, 0, 5, 4, 2],  # 우
    [2, 1, 5, 0, 4, 3],  # 좌
    [4, 0, 2, 3, 5, 1],  # 상
    [1, 5, 2, 3, 0, 4],  # 하
]

dy, dx = [0, 0, 0, -1, 1], [0, 1, -1, 0, 0]

# 시작할 때 맨 윗면이 1, 바닥면이 6인 상태로 시작
# 항상 인덱스 마지막자리가 맨 밑으로 오기 때문에 인덱스 마지막자리를 바꿔야 한다.
r, c = X, Y
for order in orders:
    # print('order:', order)
    if 0 <= r + dy[order] < N and 0 <= c + dx[order] < M:

        # 좌표변경
        r, c = r + dy[order], c + dx[order]

        # 주사위 굴리기
        tmp = [0] * 6
        for i in range(6):  # 복사
            tmp[i] = dice[0][i]
        for i in range(6):  # 이동
            dice[0][i] = tmp[dice[order][i]]

        # 주사위 바닥면 바꾸기
        # 칸 == 0 이면 주사위에 있는 수가 칸에 복사
        if board[r][c] == 0:
            board[r][c] = dice[0][-1]
        # 칸 != 0 이면 칸에있는 수가 주사위의 바닥으로 복사, 칸 == 0
        else:
            dice[0][-1] = board[r][c]
            board[r][c] = 0

        print(dice[0][0])
