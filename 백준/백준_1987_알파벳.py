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
        if 0 <= nr < R and 0 <= nc < C and not visited[board[nr][nc]]:
            visited[board[nr][nc]] = 1
            max_count = max(max_count, count + 1)
            DFS(nr, nc, count + 1)
            visited[board[nr][nc]] = 0


R, C = map(int, read().rstrip().split())
board = [list(map(lambda x: ord(x) - 65, read().rstrip())) for _ in range(R)]
dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]
visited = [0] * 26
visited[board[0][0]] = 1
max_count = 1

DFS(0, 0, 1)
print(max_count)
