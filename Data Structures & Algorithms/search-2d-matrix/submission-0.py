class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        l = 0
        r = ROWS * COLS - 1
        while l <= r:
            m = (l+r)//2

            row = m // COLS
            col = m % COLS
            val = matrix[row][col]
            if target == val:
                return True
            elif target < val:
                r = m - 1
            else:
                l = m + 1
        return False