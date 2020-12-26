import sys

sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline

'''
아스키코드 변경 후 리스트로 방문배열 확인
'''


def DFS(r, c, count):
    global max_count

    for direction in range(4):
        nr, nc = r + dy[direction], c + dx[direction]
        if 0 <= nr < R and 0 <= nc < C and board[nr][nc] not in visited:
            tmp_value = board[nr][nc]
            visited.add(tmp_value)
            max_count = max(max_count, count + 1)
            DFS(nr, nc, count + 1)
            visited.remove(tmp_value)


R, C = map(int, read().rstrip().split())
board = [list(read().rstrip()) for _ in range(R)]
dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]
visited = set()
visited.add(board[0][0])
max_count = 0

DFS(0, 0, 1)
print(max_count)