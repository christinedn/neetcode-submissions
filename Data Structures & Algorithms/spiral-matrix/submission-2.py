class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        min_col, max_col = 0, len(matrix[0])
        min_row, max_row = 0, len(matrix)
        res = []
        row = 0
        while min_col < max_col and min_row < max_row:
            for col in range(min_col, max_col):
                res.append(matrix[row][col])
            min_row += 1
            for row in range(min_row, max_row):
                res.append(matrix[row][col])
            max_col -= 1

            if min_col < max_col and min_row < max_row:
                for col in range(max_col-1, min_col-1, -1):
                    res.append(matrix[row][col])
                max_row -= 1
                for row in range(max_row - 1, min_row - 1, -1):
                    res.append(matrix[row][col])
                min_col += 1

        return res