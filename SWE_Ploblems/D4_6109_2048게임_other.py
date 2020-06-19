import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T + 1):
    N, S = map(str, input().split())
    N = int(N)
    board = [list(map(int, input().split())) for _ in range(N)]

    if S == 'up':
        direct = 0
    elif S == 'right':
        direct = 1
    elif S == 'down':
        direct = 2
    else:
        direct = 3

    # 상 우 하 좌
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    # 방향이 위일때
    # if direct == 0:
    # 첫번째줄부터 세로방향으로 검사하면서 돌려보자.
    # 본인값은 변수로 저장해서 가지고 있고, 다른것들을 둘러보면서 검사한다.
    # for j in range(N):
    #     for i in range(N):  # 세로방향으로 반복문을 돌린다.
    # 지금의 숫자와 다른숫자가 아래 있다면, 그대로 있는다
    # 지금의 숫자와 같은 숫자가 있다면 리스트 중 같은거를 빼버리고 모든 숫자를 당겨온 뒤, 맨뒤에다가 0을 추가한다
    # 지금의 숫자 뒤에 0이 있다면, 0을 지우고 리스트를 당겨온 후, 맨 뒤에다가 0을 집어넣는다. 이 경우에는 같은자리를 한번 더 검사한다.

    if S == 'up':
        for j in range(N):
            for i in range(N-1):

                while True:
                    k = 1
                    if board[i][j] == board[i+k][j]:
                        board[i][j] *= 2
                        board[i+k][j] = 0
                        break
                    elif board[i][j] == 0 and board[i+k][j] != 0:
                        board[i][j] = board[i+k][j]
                        board[i + k][j] = 0
                        continue

                    elif board[i][j] != 0 and board[i+k][j] == 0:
                        l = k
                        while i+l < N:
                            if board[i+l][j] == 0:
                                l += 1
                                continue
                            if board[i+l][j] != 0:
                                if board[i][j] == board[i+l][j]:
                                    board[i][j] *= 2
                                    board[i + l][j] = 0
                                    break
                                if board[i][j] != board[i+l][j]:
                                    board[i + k][j] = board[i+l][j]
                                    board[i + l][j] = 0
                                    break
                        break
                    elif board[i][j] + board[i+k][j] != board[i][j] * 2:
                        break

    for i in range(N):
        print(board[i])

    # if direct == 1:
    #     for j in range(N-1, 0, -1):
    #         for i in range(N):
    #             print(my_func(i, j, direct))
    #
    # if direct == 2:
    #     for i in range(N-1, 0, -1):
    #         for j in range(N):
    #             print(my_func(i, j, direct))
    #
    # if direct == 3:
    #     for j in range(N):
    #         for i in range(N):
    #             print(my_func(i, j, direct))





