import sys

sys.stdin = open("input.txt", "r")

for t in range(1, 11):
    N = int(input())
    maze = [list(input()) for _ in range(16)]

    print(maze)

    # 시작점 찾기
    for i in range(16):
        for j in range(16):
            if maze[i][j] == '2':
                si, sj = i, j
                break

    # 진행하다가 꺾는지점이 나오면 무조건 꺾기
    # 1 7개로 둘러쌓인 부분이 나오면 멈추기
    # 이전 꺾인 지점까지 돌아가면서 1로 바꾸기
    # 꺾인 지점에서 다른길로 갈 수 있는지 검사하고, 다시 1로 둘러쌓여있으면 이전행위 반복

    # 시작방향 정해주기
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    direct = 0
    # 0:상, 1:우상 , 2:우 , 3:우하, 4:하, 5:좌하, 6:좌, 7:좌상
    for i in range(8):
        if maze[si + dy[i]][sj + dx[i]] == '0':
            direct = i
            maze[si][sj] = '0'
            break

    # 시작점부터 진행하기
    r = si + dy[direct]
    c = sj + dx[direct]
    nr = 0
    nc = 0
    result = 0

    while True:

        # 도착점을 만나면 종료
        if maze[r][c] == '3':
            result = 1
            break

        # 주변이 1로 둘러쌓여있으면 본인 자리를 1로 바꾸고 이전위치로 돌아가기
        cnt1 = 0
        for i in range(8):
            if maze[r + dy[i]][c + dx[i]] == '1':
                cnt1 += 1
        if cnt1 == 7:
            maze[r][c] = '1'
            r -= dy[direct]
            c -= dx[direct]
            continue

        # 진행방향이 상, 하 일때는 좌, 우에 0이 있는지 확인
        elif direct == 0 or direct == 4:
            if maze[r][c + 1] == '0':
                direct = 2
                nr = r + dy[direct]
                nc = c + dx[direct]
            elif maze[r][c - 1] == '0':
                direct = 6
                nr = r + dy[direct]
                nc = c + dx[direct]
            else:
                nr = r + dy[direct]
                nc = c + dx[direct]
            r = nr
            c = nc

        # 진행방향이 좌, 우 일때는 상, 하에 0이 있는지 확인
        elif direct == 2 or direct == 6:
            if maze[r - 1][c] == '0':
                direct = 0
                nr = r + dy[direct]
                nc = c + dx[direct]
            elif maze[r + 1][c] == '0':
                direct = 4
                nr = r + dy[direct]
                nc = c + dx[direct]
            else:
                nr = r + dy[direct]
                nc = c + dx[direct]
            r = nr
            c = nc



    print(result)