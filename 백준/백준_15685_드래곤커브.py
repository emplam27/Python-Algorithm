import sys
sys.stdin = open("input.txt", "r")


# 15685 드래곤커브

# 1시간 30분
# 100칸이어서 101개의 2차원배열이 필요. 문제 꼼꼼히 읽을 것


# <해야할 일>
# 1. 커브 만들기: 돌아가면서 0세대부터 한단계씩 만들어 나가는 로직이 필요함
#   꼭짓점을 찍어야 하는데, 이전세대의 꼭짓접들을 끝점을 기준으로 시계방향 90도 돌려 찍어야함
#   꼭짓점을 저장해 놓는것이 아닌 이동방법을 저장해 놓은 후, 방향만 바꿔주는 방식으로 하자.
#   끝점의 좌표는 공유하고, 이전 세대의 이동방법을 끝점에서 방향만 바꿔 실행해 주는 방법으로
#   다음세대 커브를 찾고, 수행된 방법은 다시 이동방법에 저장된다.
#   다음세대 커브는 이전세대들의 이동방법을 역행으로 수행하며, 시계 반대방향으로 돌린 것이다.

# 2. 정사각형 찾기
#   꼭짓점(1)을 찾은 후 우, 하, 우하 지점에 꼭짓점(1)이 있는지 확인


def make_dragon_curve(x, y, d, generation):

    end_point_x, end_point_y, direction = x, y, d  # 시작점
    board[y][x] = 1  # 시작점 찍어주기

    # 0세대 이동은 특이하여 따로 해주기
    current_generation = 0
    board[y + dy[d]][x + dx[d]] = 1  # 0세대 이동 찍어주기
    moves = [d]  # 0세대 이동
    end_point_y += dy[d]
    end_point_x += dx[d]

    while current_generation < generation:

        current_generation += 1  # 세대 올리기

        current_move = []  # 이번 세대의 이동방법을 저장할 배열

        for move in moves[::-1]:  # 이전세대의 이동방법을 역행하면서
            # 시계 반대방향으로 돌린 이동을 수행
            end_point_y += dy[(move + 1) % 4]
            end_point_x += dx[(move + 1) % 4]
            board[end_point_y][end_point_x] = 1  # 현재 위치 찍어주기
            # 이동 저장하기
            current_move.append((move + 1) % 4)

        # 모든 이동이 끝난 후, 이전세대 이동방법에 더해주기
        moves.extend(current_move)

    return


N = int(input())
dragon_curves = [list(map(int, input().split())) for _ in range(N)]
board = [[0] * 101 for _ in range(101)]
dy, dx = [0, -1, 0, 1], [1, 0, -1, 0]  # 우, 상, 좌, 하

for dragon_curve in dragon_curves:
    make_dragon_curve(*dragon_curve)

square = 0
for r in range(100):
    for c in range(100):
        if board[r][c] and board[r + 1][c] and board[r][c + 1] and board[r + 1][c + 1]:
            square += 1

print(square)

