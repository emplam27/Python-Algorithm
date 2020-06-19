import sys

sys.stdin = open('input.txt', 'r')


def cnts(n):
    global cnt
    stack = [n]
    while stack:
        x, y, z = stack.pop(0)
        if len(z) == 7:
            if visit.get(z) == None:
                cnt += 1
                visit[z] = 1
            continue
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < 4 and 0 <= ny < 4:
                stack.append([nx, ny, z + board[nx][ny]])


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for t in range(1, int(input()) + 1):
    board = [list(input().split()) for _ in range(4)]
    stack = []
    visit = {}
    cnt = 0
    for i in range(4):
        for j in range(4):
            cnts([i, j, board[i][j]])

    print('#{} {}'.format(t, cnt))
