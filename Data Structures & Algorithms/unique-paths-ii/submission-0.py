class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1] == 1: return 0
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * COLS for _ in range(ROWS)]
        
        dp[-1][-1] = 1


        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                if obstacleGrid[r][c] == 1:
                    continue
                if r+1 < ROWS and obstacleGrid[r+1][c] != 1:
                    dp[r][c] += dp[r+1][c] 
                if c+1 < COLS and obstacleGrid[r][c+1] != 1:
                    dp[r][c] += dp[r][c+1]
        return dp[0][0]

