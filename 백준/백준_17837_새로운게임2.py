import sys
sys.stdin = open("input.txt", "r")

# 1시간 20분
# 문제 잘 읽기. 말이 4개 이상 쌓이면 종료


# <해야할 일>
# 1. 각 칸에 말들을 어떤 자료구조를 이용해서 올려야 하는지 고민해볼 필요가 있다.
#   각 2차원 배열에 어떤 말이 올라가있는지 구하는 3차원 배열로 가보는것도 좋을 듯 하다
#   리스트를 끊어가면서 작업해야 할 듯 한데.. 리스트 관련 함수들을 많이 써야할 듯
# 2. 각 말이 어디에 위치해 있는지를 알 수 있는 배열도 필요해야 할 듯 싶다.
#   3차원 배열을 항상 순회하면서 찾기에는 문제가 있으니까. 적어도 r, c값이라도
# 3. 말이 4개이상 쌓이면 게임이 종료되고, 1000보다 크면 -1이다.
# 4. 각 색깔에 맞게 잘 해볼것..


N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]  # 0은 흰색, 1은 빨간색, 2는 파란색
pieces = [list(map(int, input().split())) for _ in range(K)]
dy, dx = [0, 0, -1, 1], [1, -1, 0, 0]  # 우 좌 상 하

position = [[[] for _ in range(N)] for _ in range(N)]  # 3차원 배열
for index, piece in enumerate(pieces):
    position[piece[0] - 1][piece[1] - 1].append(index)  # 말 배치
    pieces[index] = [piece[0] - 1, piece[1] - 1, piece[2] - 1]  # 말 위치, 이동방향 정리


def game():
    turn = 1
    while turn <= 1000:
        for index, (r, c, direction) in enumerate(pieces):
            nr, nc = r + dy[direction], c + dx[direction]

            # 범위를 벗어났거나 파란색이면
            if not 0 <= nr < N or not 0 <= nc < N or board[nr][nc] == 2:
                # 방향을 반대로 바꾸고
                if pieces[index][2] == 0: pieces[index][2] = 1
                elif pieces[index][2] == 1: pieces[index][2] = 0
                elif pieces[index][2] == 2: pieces[index][2] = 3
                elif pieces[index][2] == 3: pieces[index][2] = 2
                nr, nc = r + dy[pieces[index][2]], c + dx[pieces[index][2]]  # 방향 갱신
                # 범위를 벗어나거나 파란색이면 그대로 있고, 이동할 수 있으면 이동
                if not 0 <= nr < N or not 0 <= nc < N or board[nr][nc] == 2:
                    continue

            # 하얀색이면
            if board[nr][nc] == 0:
                # 위치에서 말을 찾아 움직이며 기존 말이 있다면 그 위에 말을 쌓고
                tmp_arr = []
                for i in range(len(position[r][c])):
                    if position[r][c][i] == index:
                        tmp_arr = position[r][c][i:]
                        position[nr][nc].extend(tmp_arr)
                        position[r][c] = position[r][c][:i]
                        break

                # 이동한 말들의 이동정보를 갱신해준다.
                for moved_piece in tmp_arr:
                    pieces[moved_piece] = [nr, nc, pieces[moved_piece][2]]

                # 말이 4개 이상 쌓이면 종료료
                if len(position[nr][nc]) >= 4:
                    return turn
                continue

            # 빨간색이면
            if board[nr][nc] == 1:
                # 위치에서 말을 찾아 움직이며 기존 말이 있다면 그 위에 순서를 반대로 해서 쌓고
                tmp_arr = []
                for i in range(len(position[r][c])):
                    if position[r][c][i] == index:
                        tmp_arr = position[r][c][i:]
                        tmp_arr.reverse()
                        position[nr][nc].extend(tmp_arr)
                        position[r][c] = position[r][c][:i]
                        break

                # 이동한 말들의 이동정보를 갱신해준다.
                for moved_piece in tmp_arr:
                    pieces[moved_piece] = [nr, nc, pieces[moved_piece][2]]

                # 말이 4개 이상 쌓이면 종료료
                if len(position[nr][nc]) >= 4:
                    return turn
                continue

        turn += 1
    return -1

print(game())
