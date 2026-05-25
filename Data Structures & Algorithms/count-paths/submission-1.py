class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 and n == 1:
            return 1
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        dp[m-1][n-2], dp[m-2][n-1] = 1, 1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if (i == m - 1 and j == n - 2) or (i == m - 2 and j == n - 1):
                    continue
                dp[i][j] = dp[i+1][j] + dp[i][j+1]

        return dp[0][0]
                