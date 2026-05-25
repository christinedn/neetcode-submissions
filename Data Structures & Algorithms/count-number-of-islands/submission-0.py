class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = 0

        def findIsland(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == "0" or grid[r][c] == "#":
                return
            grid[r][c] = "#"
            findIsland(r + 1, c) 
            findIsland(r, c + 1) 
            findIsland(r, c - 1) 
            findIsland(r - 1, c) 

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    res += 1
                    findIsland(r, c)
        return res