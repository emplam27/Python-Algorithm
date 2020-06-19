import sys

sys.stdin = open('../못푼문제/5656_input.txt', 'r')


# 중복순열 만드는 함수
def product(tmp, idx):
    global W, N, min_result

    if min_result == 0:
        return

    if idx == N:
        check(tmp)
        return

    for i in range(W):
        product(tmp + [i], idx + 1)


def check(arr):
    global min_result

    # 배열을 90도 돌려 복사
    board_copy = [[0] * H for _ in range(W)]
    for i in range(H):
        for j in range(W):
            board_copy[W - 1 - j][H - 1 - i] = board[i][j]

    # 백트레킹을 이용하여 터뜨리기
    for a in arr:
        # 선택된 열의 가장 위 블록을 스택에 넣는다.
        stack = list()
        for b in range(H-1, -1, -1):
            if board_copy[a][b] != 0:
                stack.append((a, b, board_copy[a][b]))
                break
        if len(stack) == 0:
            break

        # 벽돌깨기
        while len(stack) > 0:
            r, c, m = stack.pop()
            board_copy[r][c] = 0
            if m == 1:
                continue
            else:
                for d in range(4):
                    for l in range(1, m):
                        nr, nc = r + (dy[d] * l), c + (dx[d] * l)
                        if 0 <= nr < W and 0 <= nc < H and board_copy[nr][nc] != 0:
                            stack.append((nr, nc, board_copy[nr][nc]))
                            board_copy[nr][nc] = 0

        # 백돌 아래로 내리기
        for p in range(W):
            tmp = []
            for q in range(H):
                if board_copy[p][q] != 0:
                    tmp.append(board_copy[p][q])
            tmp += [0] * (H - len(tmp))
            board_copy[p] = tmp

    # 최솟값 구하기
    count = 0
    for i in range(W):
        for j in range(H):
            if board_copy[i][j] != 0:
                count += 1
    if min_result > count:
        min_result = count
    return


for t in range(1, int(input()) + 1):
    N, W, H = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(H)]
    dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]  # 상하좌우

    # 중복순열
    min_result = 0
    for i in range(H):
        for j in range(W):
            if board[i][j] != 0:
                min_result += 1

    product([], 0)

    print('#%d' % t, min_result)


