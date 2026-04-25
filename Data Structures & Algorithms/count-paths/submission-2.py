class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [ [1 for i in range(n)] for j in range(m)]
        ROWS, COLS = m, n
        for r in range(ROWS-2, -1, -1):
            for c in range(COLS-2, -1, -1):
                grid[r][c] = grid[r+1][c] + grid[r][c+1]
        return grid[0][0]
