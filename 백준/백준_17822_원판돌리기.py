import sys

sys.stdin = open("17822_input.txt", "r")

# tmp가 0인경우를 생각하지 않아 런타임에러
# 예외 케이스를 항상 생각해야한다.
# 0으로 지정해주는 수가 나오게 되면, 예외케이스가 발생할 수 있음을 꼭 명심하자.



def search(rr, cc, m, visited):

    change_list = [[rr, cc]]
    stack = [[rr, cc]]
    while len(stack) > 0:
        r, c = stack.pop()
        visited[r][c] = 1
        for d in range(4):
            nr, nc = r + dy[d], c + dx[d]
            # 인접은 상하좌우다. 배열의 좌우로 넘어갈 경우에는 맨끝으로 이동시켜준다.
            if nc < 0:
                nc = M - 1
            elif nc > M - 1:
                nc = 0

            # 돌아가면서 확인하는데, 인접한 수들이 같은수가 나올 경우에는 다 0으로 바꿔준다.
            if 0 <= nr < N and board[nr][nc] == m and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                change_list.append([nr, nc])
                stack.append([nr, nc])

    if len(change_list) > 1:
        for r, c in change_list:
            board[r][c] = 0
        return True


def check(x, d, k):
    # x의 배수번째 원판을 돌린다.
    for i in range(x-1, N, x):
        if M > 1 and k != M:
            if d == 1:
                board[i] = board[i][k:] + board[i][:k]
            else:
                board[i] = board[i][-k:] + board[i][:-(k)]

    # visited활용, BFS
    visited = [[0] * M for _ in range(N)]
    is_change = False
    for r in range(N):
        for c in range(M):
            if visited[r][c] == 0 and board[r][c] != 0:
                if search(r, c, board[r][c], visited):
                    is_change = True

    # 한번도 숫자가 바뀌지 않았을 때
    if not is_change:
        avg, tmp = 0, 0
        for r in range(N):
            for c in range(M):
                if board[r][c] != 0:
                    avg += board[r][c]
                    tmp += 1

        if avg != 0 and tmp != 0:
            avg /= tmp

            for r in range(N):
                for c in range(M):
                    if board[r][c] != 0 and board[r][c] > avg:
                        board[r][c] -= 1
                    elif board[r][c] != 0 and board[r][c] < avg:
                        board[r][c] += 1
    return


N, M, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
move = [list(map(int, input().split())) for _ in range(T)]
# x의 배수 원판, 방향(0:시계, 1:반시계), k칸 회전
dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]

result = 0
if M > 0:
    for x, d, k in move:
        check(x, d, k)

    for i in range(N):
        for j in range(M):
            if board[i][j] != 0:
                result += board[i][j]

print(result)