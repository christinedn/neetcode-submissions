class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        def makeRowColZero(i, j):
            # make col 0
            for c in range(COLS):
                matrix[i][c] = 0

            # make row 0
            for r in range(ROWS):
                matrix[r][j] = 0
        zero = []
        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    zero.append([i, j])
        
        for i, j in zero:
            makeRowColZero(i, j)
        
        