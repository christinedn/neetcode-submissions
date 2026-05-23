class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        box = [set() for _ in range(9)]

        for r in range(len(board)):
            for c in range(len(board[0])):
                curr_box = (r//3) * 3 + (c//3)
                if board[r][c] == '.':
                    continue
                if board[r][c] in cols[c] or board[r][c] in rows[r] or board[r][c] in box[curr_box]:
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                box[curr_box].add(board[r][c])
        return True
