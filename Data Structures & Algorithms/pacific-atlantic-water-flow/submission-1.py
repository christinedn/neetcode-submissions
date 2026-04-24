class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        dirs = [[0,1], [1,0], [-1,0], [0,-1]]
        pac, atl = set(), set()
        ROWS, COLS = len(heights), len(heights[0])

        def dfs(r, c, visit, prevHeight):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or heights[r][c] < prevHeight or (r,c) in visit:
                return
            visit.add((r,c))
            for dr, dc in dirs:
                dr += r
                dc += c
                dfs(dr, dc, visit, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pac, 0)
            dfs(ROWS-1, c, atl, 0)
        
        for r in range(ROWS): 
            dfs(r, 0, pac, 0)
            dfs(r, COLS-1, atl, 0)
        
        res = []
        for item in pac:
            if item in atl:
                res.append(item)
        return res
