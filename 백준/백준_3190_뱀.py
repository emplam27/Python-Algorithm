# 1시간
# 구현하고자 하는 부분에 맞는 자료구조를 적는 연습 하기
# 좋은 발상의 전환이 가능해짐


import sys

sys.stdin = open("input.txt", "r")




# <해야할 일>
# 뱀은 0, 0에서 우측방향으로, 길이는 1로 시작한다
# 이동방향에 사과가 없으면 꼬리를 한칸 줄인다
# 이동방향에 사과가 있으면 꼬리를 줄이지 않는다
# 벽에 닿거나 자기 몸에 닿게되면 게임이 끝나게된다
#
# 방향의 전환은 해당 초가 끝난 후에 바뀌게 된다
# 오른쪽 왼쪽으로만 전환이 주어진다

# <특이점>
# 1차원 배열로 뱀의 정보를 저장할 경우에는 꼬리 머리를 이동하는게 용이하지만,
# 자신 몸에 부딪히는 것 때문에 항상 이동할 때 마다 뱀 배열을 탐색해줘야한다.

# 2차원 배열을 이용하게 되면 범위에 대한 탐색은 편하지만 꼬리에 대한 처리가 어렵게 된다.
# 꼬리를 처리할 수 있다면 괜찮은데

# 위 둘을 합쳐서 활용하면 좋을 듯 하다.
# 몸 배열을 리스트로도, 2차원배열로도 활용해서 자신몸에 부딪히는것과 범위를 벗어나는 것은 2차원 배열로,
# 꼬리의 처리는 리스트로 활용하자. deque 사용하면 빠를듯

# <순서>
# 방향설정은 나머지값으로 활용한다. 방향을 애초에 방향값을 101로 잡아야겠다. 빼던 더하던 상관없게
# 뱀이 사과를 먹을 때 마다 1차원 배열의 길이가 증가하게 된다.
# 꼬리 부분이 줄어들때는 항상 뱀 배열에서 popleft 이후에 반환값을 이용해서 2차원 배열에서 없에준다.
# 이동이 끝난 후, 방향전환


from collections import deque


N = int(input())
K = int(input())
apples = [list(map(int, input().split())) for _ in range(K)]
L = int(input())
moves = [list(input().split()) for _ in range(L)]
for i in range(L):
    moves[i][0] = int(moves[i][0])
dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]  # 상 우 하 좌


# 보드 만들기
board = [[0] * N for _ in range(N)]
for i in range(K):  # 사과추가
    board[apples[i][0] - 1][apples[i][1] - 1] = 2


# 뱀 초기위치
snake = deque()
snake.append([0, 0])
board[0][0], r, c = 1, 0, 0
direction = 101  # 우방향
time, move_count = 0, 0

# moves를 편하게 사용하기 위해
moves.append([0, 0])

while True:
    # 이동
    nr, nc = r + dy[direction % 4], c + dx[direction % 4]
    time += 1  # 시간추가
    # 범위 안에서
    if 0 <= nr < N and 0 <= nc < N:

        if board[nr][nc] == 0:              # 빈곳이라면
            board[nr][nc] = 1               # 머리 이동
            snake.append([nr, nc])          # 머리 추가
            tail_r, tail_c = snake.popleft()  # 꼬리 빼기
            board[tail_r][tail_c] = 0       # 꼬리 이동
            r, c = nr, nc                   # 머리좌표 갱신

        elif board[nr][nc] == 2:            # 사과라면
            board[nr][nc] = 1               # 머리 이동
            snake.append([nr, nc])          # 머리 추가
            r, c = nr, nc  # 머리좌표 갱신

        else:                               # 뱀이라면
            break                           # 끝

    else:  # 범위를 벗어나면
        break  # 끝

    # 이동이 완료되면 방향전환
    if time == moves[move_count][0]:
        if moves[move_count][1] == 'L':
            direction -= 1  # 왼쪽
        else:
            direction += 1  # 오른쪽
        move_count += 1  # 카운트 추가

print(time)
