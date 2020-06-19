T = int(input())
for t in range(1,T+1):
    in_str = input()
    # 그림을 그릴 이차원 배열 준비하기
    n = len(in_str) # 문자열의 길이
    # 높이 : 5, 너비 : 4n+1
    board =[['.']*(4*n+1) for _ in range(5)]

    # 다이아몬드 무늬 출력하기
    # 글자 위치 잡아주고,  다이아 몬드 모양 위치 잡아주기
    # 다이아 몬드 무늬를 출력하기 위한, 델타 작성하기
    dr = [-2, -1, 0, 1, 2, 1, 0, -1]
    dc = [0, 1, 2, 1, 0, -1, -2, -1]
    for i in range(n):
        x = 4*i+2
        board[2][x] = in_str[i]

        # 델타 순회하면서, x,y 변경 시키고 '#' 출력
        # 글자 위치를 (0,0) 기준으로 잡고 시계방향으로 # 무늬를 작성해준다.
        for j in range(8):
            tr = 2 + dr[j]
            tc = x + dc[j]
            board[tr][tc] = "#"

    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j],end="")
        print()
