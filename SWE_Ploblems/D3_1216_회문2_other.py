def check_pal(K):
    # 길이가 K 인 회문이 있나 검사
    for i in range(N):
        for j in range(N - K + 1):
            # j 열 부터 시작하는 k 길이의 회문검사
            tmp = board[i][j:j + K]     # 가로 회문 검사대상
            tmp2 = zboard[i][j:j + K]    # 세로 회문 검사대상
            if tmp == tmp[::-1] or tmp2 == tmp2[::-1]:
                return True
    return False

for t in range(10):
    num = int(input())
    N = 100
    board = [list(input()) for _ in range(N)]
    # 전치행렬 만들어주기 :  (x,x) 를 기준으로 대칭
    zboard = list(zip(*board))

    # 회문의 길이를 줄여가면서 해당길이의 회문이 존재하는지 확인
    result = 0
    for i in range(N, 0, -1):
        if check_pal(i):
            result = i
            break

    print('#%d' % t, result)
