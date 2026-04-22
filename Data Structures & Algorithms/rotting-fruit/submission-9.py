class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        # count number of fresh fruit
        fresh = 0
        q = deque()
        res = 0
        dirs = [[1,0],[0,1],[-1,0],[0,-1]]
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c)) 
                elif grid[r][c] == 1:
                    fresh += 1

        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                # go every adjacent direction to make rotten
                for dr, dc in dirs:
                    dr += r
                    dc += c
                    if dr < 0 or dr == ROWS or dc < 0 or dc == COLS: # out of bounds
                        continue
                    if grid[dr][dc] == 1:
                        grid[dr][dc] = 2
                        q.append((dr, dc))
                        fresh -= 1
            res += 1
        
        if fresh > 0:
            return -1
        else:
            return res



