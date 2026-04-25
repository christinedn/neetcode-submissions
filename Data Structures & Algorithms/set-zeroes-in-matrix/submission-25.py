class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        isRowZero = False
        isColZero = False
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r == 0 and matrix[r][c] == 0:
                    isRowZero = True
                if c == 0 and matrix[r][c] == 0:
                    isColZero = True
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0
        # go through first row/col and make zeros
        for r in range(1, len(matrix)):
            if matrix[r][0] == 0:
                for c in range(len(matrix[0])):
                    matrix[r][c] = 0
                    
        for c in range(1, len(matrix[0])):
            if matrix[0][c] == 0:
                for r in range(len(matrix)):
                    matrix[r][c] = 0
                
        if isRowZero == True:
            for c in range(len(matrix[0])):
                matrix[0][c] = 0
        
        if isColZero == True:
            for r in range(len(matrix)):
                matrix[r][0] = 0
        