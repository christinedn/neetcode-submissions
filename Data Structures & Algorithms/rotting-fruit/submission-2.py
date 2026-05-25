class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh, time = 0, 0
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r, c])
                if grid[r][c] == 1:
                    fresh += 1
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc 
                    if row < 0 or row > ROWS - 1 or col < 0 or col > COLS - 1 or grid[row][col] != 1:
                        continue
                    grid[row][col] = 2
                    fresh -= 1
                    q.append([row, col])
            time += 1
        return time if fresh == 0 else -1
                    

        