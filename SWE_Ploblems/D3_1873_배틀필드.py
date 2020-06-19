import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T + 1):
    H, W = map(int, input().split())
    arr = [list(map(str, input().split())) for _ in range(H)]
    N = int(input())
    orders = input()

    # field 만들어주기
    field = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            field[i][j] = arr[i][0][j]

    # direct 0 : 상, 1: 우, 2: 하, 3: 좌
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    order_list = ['U', 'R', 'D', 'L']
    tank_list = ['^', '>', 'v', '<']

    # 시작하자마자 전차가 바라보는 방향, 현재 좌표가 필요함
    r = 0
    c = 0
    for i in range(H):
        for j in range(W):
            for k in range(4):
                if field[i][j] == tank_list[k]:
                    direct = k
                    r, c = i, j

    # orders 를 확인하면서 명령을 내린다.
    for order in orders:

        # S 명령일 경우
        if order == 'S':
            nr = r
            nc = c
            while True:
                nr = nr + dy[direct]
                nc = nc + dx[direct]
                if nr < 0 or nc < 0 or nr >= H or nc >= W:
                    break
                if field[nr][nc] == '#':
                    break
                if field[nr][nc] == '*':
                    field[nr][nc] = '.'
                    break

        else:
            for k in range(4):
                if order == order_list[k]:
                    direct = k
                    nr = r + dy[direct]
                    nc = c + dx[direct]
                    if nr < 0 or nc < 0 or nr >= H or nc >= W:
                        field[r][c] = tank_list[direct]
                    elif field[nr][nc] == '.':
                        field[r][c] = '.'
                        field[nr][nc] = tank_list[direct]
                        r = nr
                        c = nc
                    elif field[nr][nc] == '#' or field[nr][nc] == '-' or field[nr][nc] == '*':
                        field[r][c] = tank_list[direct]

    print('#%d' % t, end=' ')
    for i in range(H):
        for j in range(W):
            print(field[i][j], end='')
        print()



