class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        dirs = [[1,0], [0,1], [-1,0], [0,-1]]
        def dfs(r, c, i, visited):
            if i == len(word):
                return True
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r,c) in visited or board[r][c] != word[i]:
                return False
            visited.add((r,c))
            for dr, dc in dirs:
                if dfs(r+dr, c+dc, i+1, visited):
                    return True
            visited.remove((r, c))
            return False

        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, 0, visited):
                    return True
        return False