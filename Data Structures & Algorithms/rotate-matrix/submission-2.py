class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # transpose
        for r in range(len(matrix)):
            for c in range(r, len(matrix)):
                temp = matrix[r][c]
                matrix[r][c] = matrix[c][r]
                matrix[c][r] = temp
        for row in matrix:
            row.reverse()
        
        