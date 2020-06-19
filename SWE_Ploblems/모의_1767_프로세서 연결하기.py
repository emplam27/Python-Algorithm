import sys

sys.stdin = open('1767_input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]  # 상 우 하 좌

    # 맨 바깥쪽 프로세서들을 제외하고, 어떤 경우에서든 연결이 가능한 프로세서를 선별한다.
    available = []
    for i in range(1, N-1):
        for j in range(1, N-1):
            if board[i][j] == 1:
                for d in range(4):
                    tmp = False
                    r, c = i, j
                    while tmp == False:
                        nr = r + dy[d]
                        nc = c + dx[d]
                        if board[nr][nc] == 1:
                            break
                        elif nr == 0 or nr == N-1 or nc == 0 or nc == N-1:
                            available.append((i, j))
                            tmp = True
                            break
                        r, c = nr, nc
                    if tmp:
                        break


    # 선별한 프로세서를 기준으로 프로세서 하나씩 사방으로 연결해보며 최대갯수, 최소길이를 잰다.
    # 재귀함수를 사용한다.

    sum_connect = 0
    sum_distance = 0
    max_connect = 0
    collect = []

    def check(idx, sum_connect, sum_distance):
        global max_connect, min_distance

        if idx == len(available):
            if sum_connect >= max_connect:
                max_connect = sum_connect
                collect.append((sum_connect, sum_distance))
            return

        i, j = available[idx]

        # 네방향으로 가게 한다.
        for d in range(4):
            r, c = i, j
            distance = 0
            # 진행하는 방향에서 1을 만날경우 다시 돌아오면서 0 으로 바꿔주고, 연결 안됐다고 하고 다음함수로 넘어가기
            # 끝에 닿았다면 진행했다고 표시, 거리체크하고 다음함수로 넘어가기
            while True:
                nr = r + dy[d]
                nc = c + dx[d]
                if board[nr][nc] == 1:
                    while not (r == i and c == j):
                        board[r][c] = 0
                        nr, nc = r - dy[d], c - dx[d]
                        r, c = nr, nc
                    # 다음함수 실행
                    check(idx + 1, sum_connect, sum_distance)
                    break

                elif board[nr][nc] == 0:
                    board[nr][nc] = 1
                    distance += 1
                    r, c = nr, nc
                    if nr == 0 or nr == N-1 or nc == 0 or nc == N-1:
                        sum_connect += 1
                        sum_distance += distance
                        check(idx + 1, sum_connect, sum_distance)
                        sum_connect -= 1
                        sum_distance -= distance
                        while not (r == i and c == j):
                            board[r][c] = 0
                            nr, nc = r - dy[d], c - dx[d]
                            r, c = nr, nc

                        break

    check(0, 0, 0)
    collect_distance = []
    for a in collect:
        if a[0] == max_connect:
            collect_distance.append(a)

    min_distance = 10000
    for a, b in collect_distance:
        if b < min_distance:
            min_distance = b
    print('#%d' % t, min_distance)
