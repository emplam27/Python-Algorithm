import sys

sys.stdin = open("2636_input.txt", "r")


def check(a, b):
    stack = [[a, b]]

    while len(stack) > 0:

        r, c = stack.pop()
        visited[r][c] = 1

        for d in range(4):
            nr, nc = r + dy[d], c + dx[d]

            if 0 <= nr < R and 0 <= nc < C and visited[nr][nc] == 0:
                # 치즈이면 없에야할 배열에 추가하기
                if arr[nr][nc] == 1:
                    arr[nr][nc] += 1
                # 0이면 DFS 진행
                elif arr[nr][nc] == 0:
                    stack.append([nr, nc])

    return


R, C = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]

count1 = 1
result = []
while count1:

    # 치즈찾아 남은치즈갯수 구하기
    count1 = 0
    for i in range(R):
        for j in range(C):
            if arr[i][j] == 1:
                count1 += 1
            elif arr[i][j] == 2:
                arr[i][j] = 0

    result.append(count1)

    if count1 != 0:
        visited = [[0] * C for _ in range(R)]
        check(0, 0)


print(len(result)-1)
print(result[-2])