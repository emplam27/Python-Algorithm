"""
DP 활용
금액별로 올 수 있는 메모를 남긴다. 해당 금액으로 방문할 수 있는 위치를 기록한다.
방문배열은 모든 방향에서 찍을 수 있도록 3차원 배열을 이용한다.
코너를 한번 돌기 위해서는 600원이 필요하며, 0원에서 바로 코너를 돌 수 없기 때문에 600원까지는 직진밖에 할 수 없다.
700원부터 검사를 시작한다. 직진을 위해서는 바로 전 금액의 메모를, 코너를 위해서는 600원 전 금액의 메모를 참고한다.
"""


def solution(board):
    N = len(board)
    # 4 방향의 방문을 모두 검사할 수 있게 한다.
    visited = [[[0] * 4 for _ in range(N)] for _ in range(N)]
    dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]  # 우:0, 하:1, 좌:2, 상: 3

    # 일정 금액을 소모하여 올 수 있는 경우를 저장하는 배열
    cache = [[] for _ in range(7)]

    # 600원까지는 우, 하 방향으로 직진밖에 할 수 없다. 벽이 있다면 막히고, 종료한다.
    for i in range(0, 7):  # 우방향
        if i >= N: break
        if board[0][i] == 1: break
        cache[i].append([0, i, 0])
        visited[0][i][0] = 1

    for i in range(0, 7):  # 하방향
        if i >= N: break
        if board[i][0] == 1: break
        cache[i].append([i, 0, 1])
        visited[i][0][1] = 1

    # 700원부터 검사를 시작한다.
    # 직진은 바로 전 price를 참고하고, 커브는 6번째 전 price를 참고한다. (코너 도는데 600원)
    for price in range(7, 25 * 25 * 5):

        tmp_price = []
        # 직진하는 경우: 바로 전 price를 참고해서 방향 그대로 전진
        for r, c, d in cache[price - 1]:
            nr, nc = r + dy[d], c + dx[d]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc][d] and not board[nr][nc]:
                visited[nr][nc][d] = 1
                tmp_price.append([nr, nc, d])

        # 커브를 도는 경우: 600원 전 price를 참고해서 방향을 꺾고 전진
        for r, c, d in cache[price - 6]:
            for change_d in range(d % 2 - 1, d % 2 + 2, 2):  # 방향 꺾기
                nr, nc = r + dy[change_d], c + dx[change_d]
                if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc][change_d] and not board[nr][nc]:
                    visited[nr][nc][change_d] = 1
                    tmp_price.append([nr, nc, change_d])

        # (N, N)에도착했다면 종료. 현재 금액이 최소금액임
        if 1 in visited[N - 1][N - 1]:
            break
        cache.append(tmp_price)

    return price * 100