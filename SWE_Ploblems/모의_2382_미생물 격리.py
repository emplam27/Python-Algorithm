import sys

sys.stdin = open("2382_input.txt", "r")

for t in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(K)]

    # 상 1 하 2 좌 3 우 4
    dy, dx = [0, -1, 1, 0, 0], [0, 0, 0, -1, 1]

    for _ in range(M):
        move = list()
        # 각 요소는 (세로, 가로, 미생물 수, 이동방향 순서)
        for r, c, m, d in board:

            # 이동
            nr, nc = r + dy[d], c + dx[d]

            # 가장자리로 이동했다면, 방향을 반대로 바꾸고 미생물 수를 반으로 줄인다.
            if nr == 0 or nr == N-1 or nc == 0 or nc == N-1:
                m = m // 2
                if m == 0:
                    continue
                if d == 1:
                    d = 2
                elif d == 2:
                    d = 1
                elif d == 3:
                    d = 4
                else:
                    d = 3
                move.append([nr, nc, m, d])
                continue

            # 가장자리에 닿는 케이스를 제외하고 모두 움직여주기
            move.append([nr, nc, m, d])

        # 모두 움직이게 한 후, 중복된 미생물을들 찾아 합쳐주고 방향 정하기
        # 미생물들이 이동한 곳을 visited 배열에 값과 함께 표시한다.
        # 미생물이 이동한 곳이 기존 미생물이 있던 곳이라면, visited 배열에 있는 값과
        # 현재 미생물의 값을 비교하여, 더 큰쪽의 방향을 따르고 visited 값을 갱신한다.
        move_board = [[0] * N for _ in range(N)]
        visited = [[0] * N for _ in range(N)]
        direction = [[0] * N for _ in range(N)]
        for r, c, m, d in move:
            if visited[r][c] == 0:
                move_board[r][c] = m
                visited[r][c] = m
                direction[r][c] = d
            else:
                if visited[r][c] < m:
                    move_board[r][c] += m
                    visited[r][c] = m
                    direction[r][c] = d
                else:
                    move_board[r][c] += m


        # 배열을 순회하면서 board에 넣어주기
        board = []
        for i in range(N):
            for j in range(N):
                if visited[i][j] != 0:
                    board.append([i, j, move_board[i][j], direction[i][j]])

    # 결과값
    result = 0
    for c in range(len(board)):
        result += board[c][2]
    print('#%d' %t, result)





