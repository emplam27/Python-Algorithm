import sys

sys.stdin = open("input2.txt", "r")

# cr, cc = 출발위치, d = 방향
def check(cr, cc, nr, nc, d, value, visited):
    global max_result

    if d > 3:
        return

    if d == 3:
        if nr == cr and nc == cc:
            if value > max_result:
                max_result = value
            return

    if d <= 3 and 0 <= nr + dy[d] < N and 0 <= nc + dx[d] < N and board[nr + dy[d]][nc + dx[d]] not in visited:
        visited.append(board[nr + dy[d]][nc + dx[d]])
        check(cr, cc, nr + dy[d], nc + dx[d], d, value + 1, visited)
        visited.pop()

    if d < 3 and 0 <= nr + dy[d + 1] < N and 0 <= nc + dx[d + 1] < N and board[nr + dy[d + 1]][nc + dx[d + 1]] not in visited:
        visited.append(board[nr + dy[d + 1]][nc + dx[d + 1]])
        check(cr, cc, nr + dy[d + 1], nc + dx[d + 1], d + 1, value + 1, visited)
        visited.pop()






for t in range(1, int(input()) + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    dy, dx = [1, 1, -1, -1], [-1, 1, 1, -1]  # 좌하, 우하, 우상, 좌상

    max_result = 0
    for i in range(N-2):
        for j in range(1, N-1):
            visited = []
            check(i, j, i, j, 0, 0, visited)

    if max_result == 0:
        max_result = -1
    print('#%d' %t, max_result)
