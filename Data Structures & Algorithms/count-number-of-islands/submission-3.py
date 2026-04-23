class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        q = deque()
        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        def bfs(r, c):
            q.append((r,c))
            grid[r][c] = 0
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    dr += r
                    dc += c
                    if dr < 0 or dr >= ROWS or dc < 0 or dc >= COLS or grid[dr][dc] == '0':
                        continue
                    q.append((dr, dc))
                    grid[dr][dc] = '0'
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    bfs(r, c)
                    res += 1
        return res

