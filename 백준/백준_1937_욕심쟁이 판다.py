import sys

sys.stdin = open("input.txt", "r")

"""
BFS는 너무 느리기에 DFS를 사용해야 함. 하지만 반복문을 사용한 BFS, DFS로 하면 시간초과남
재귀함수를 이용한 DFS를 이용해야 함


<해야할 일>
1. DP로 풀어야 한다고 했으니 메모를 위한 dp배열 만들기
2. BFS 들어가면서 dp에 최대 거리 찍어주기, 최대거리를 갱신할 수 있다면 dp에서 갱신
"""
import sys
sys.setrecursionlimit(100000)


def dfs(r, c):
    if dp[r][c]:
        return dp[r][c]

    dp[r][c] = 1
    for d in range(4):
        nr, nc = r + dy[d], c + dx[d]
        if 0 <= nr < N and 0 <= nc < N and field[r][c] < field[nr][nc]:
            dp[r][c] = max(dp[r][c], 1 + dfs(nr, nc))
    return dp[r][c]


N = int(input())
field = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]

max_result = 0
for i in range(N ** 2):
    if dp[i // N][i % N] == 0:
        max_result = max(max_result, dfs(i // N, i % N))

print(max_result)
