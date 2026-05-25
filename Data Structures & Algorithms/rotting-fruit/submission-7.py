# push rotting orange onto the stack
# increment second
# rot surrounding oranges
# push those ^ surronding oranges onto the deque
# increment second
# rot surrounding oranges

# while deque is not empty, increment time

# go through 2d array if there are no more fresh fruit return time. else, return -1

# how do you find the coordinates of the rotting oranges? where do you save it? onto the deque
# 
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
            
        d = deque()
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res = 0
        freshFruitExist = False

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    d.append((r, c))
                if grid[r][c] == 1:
                    freshFruitExist = True
        
        if not freshFruitExist and not d:
            return 0

        # while there are still rotten oranges and there are surrounding oranges to make rotten
        # while deque exists and surrounding elements are 1

        while d:
            res = res + 1
            for i in range(len(d)):
                r, c = d.popleft()
                for dr, dc in dirs:
                    dr += r
                    dc += c
                    if dr < 0 or dc < 0 or dr == ROWS or dc == COLS:
                        continue
                    elif grid[dr][dc] == 1:
                        grid[dr][dc] = 2
                        d.append((dr, dc))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
        return res - 1
        
        

        