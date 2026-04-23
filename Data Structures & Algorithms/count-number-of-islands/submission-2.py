class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        res = 0
        ROWS, COLS = len(grid), len(grid[0])
        def markIsland(r, c):
            if r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] == '0' or grid[r][c] == '#':
                return
            # grd[r][c] will have to be 1 at this point. 
            grid[r][c] = '#'
            for dr, dc in dirs:
                markIsland(dr + r, dc + c)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    res += 1
                    markIsland(r, c)
        return res