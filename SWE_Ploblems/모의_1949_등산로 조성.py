import sys

sys.stdin = open('input2.txt', 'r')


# 검사하는 함수
def check(i, j, arr):
    global result

    # 백트레킹으로 검사
    stack = []
    stack.append((i, j, 1))

    while len(stack):
        r, c, t = stack.pop()

        if t > result:
            result = t

        for d in range(4):
            nr = r + dy[d]
            nc = c + dx[d]
            if 0 <= nr < N and 0 <= nc < N and arr[r][c] > arr[nr][nc]:
                stack.append((nr, nc, t + 1))



T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]

    # 가장 높은 높이를 알아낸 후, 리스트화 한다.
    max_h = 0
    max_height = set()
    for i in range(N**2):
        if arr[i // N][i % N] > max_h:
            max_h = arr[i // N][i % N]
    for i in range(N ** 2):
        if arr[i // N][i % N] == max_h:
            max_height.add((i // N, i % N))

    # 돌아가면서 한곳씩 땅을 깎는다.
    result = 0
    for m in range(N ** 2):
        for n in range(1, K + 1):
            arr[m // N][m % N] -= n

            # 가장 높은곳 리스트에 있는 위치들을 검사한다.
            # 검사시, 깎는 위치가 최대높이 리스트에 있는 위치라면, 검사 리스트에서 제외한다.
            for i, j in max_height:
                if i == m // N and j == m % N:
                    continue
                check(i, j, arr)

            # 다시 채워주며 리스트를 원래대로 되돌린다.
            arr[m // N][m % N] += n

    print('#{} {}'.format(t, result))