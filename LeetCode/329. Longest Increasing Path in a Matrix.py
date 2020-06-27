class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        def dfs(r, c):
            if dp[r][c]:
                return dp[r][c]

            dp[r][c] = 1
            for d in range(4):
                nr, nc = r + dy[d], c + dx[d]
                if 0 <= nr < R and 0 <= nc < C and matrix[r][c] < matrix[nr][nc]:
                    dp[r][c] = max(dp[r][c], 1 + dfs(nr, nc))
            return dp[r][c]

        R, C = len(matrix), len(matrix) and len(matrix[0])
        dp = [[0] * C for _ in range(R)]
        dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]

        # 모든 경우의 수에서 BFS 실행하기
        max_result = 0
        for i in range(R):
            for j in range(C):
                if dp[i][j] == 0:
                    max_result = max(max_result, dfs(i, j))

        return max_result