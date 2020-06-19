import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T + 1):
    N, S = input().split()
    N = int(N)
    board = [list(map(int, input().split())) for _ in range(N)]

    # 방향에 맞게 밀어내기
    # up일 경우 위쪽으로 밀어내기
    if S == 'up':
        # 세로방향 우선순회
        for i in range(N): # N * N 행렬이기 때문에 세로 줄이 N개임
            for j in range(N-1):
                # j번째 숫자와 같은 숫자가 있는지 검색
                for k in range(j+1, N): # 검사 대상 뒤부터 검색 :: while 문 대용으로 사용할 수 있다.
                    if board[k][i] != 0:
                        if board[k][i] == board[j][i]:
                            board[j][i] *= 2
                            board[k][i] = 0
                        break   # 0이 아니라면 더이상 검사할 필요가 없다.
                                # 같다면 합치면 되고, 다르면 이후것은 볼 필요가 없음

            # 다 합쳐짐
            # 빈칸 메꾸기
            for i in range(N):  # 모든 열에 대해서 빈칸을 메꾸어야 한다.
                for j in range(N-1):
                    # 빈칸이면, 뒤쪽에 위치한 숫자중에 가장 가까운 숫자 가져오기
                    if board[j][i] == 0:
                        for k in range(j+1, N):
                            if board[k][i] != 0:
                                board[j][i] = board[k][i]
                                board[k][i] = 0
                                break
        for i in range(len(board)):
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





