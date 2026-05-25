class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # create a boolean (cell) that tells us if the row needs to be zeroed out
        cell = False
        # if cell == 0, it means we need to set that corresponding row/col to 0
        ROWS, COLS = len(matrix), len(matrix[0])
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    # set col (boolean) to 0
                    matrix[0][c] = 0
                    # set row (boolean) to 0
                    if r == 0:
                        cell = True
                    else:
                        matrix[r][0] = 0

        for i in range(1, ROWS):
            if matrix[i][0] == 0:
                for c in range(COLS):
                    matrix[i][c] = 0
                    
        for i in range(COLS):
            if matrix[0][i] == 0:
                for r in range(ROWS):
                    matrix[r][i] = 0
        
        if cell:
            for c in range(COLS):
                matrix[0][c] = 0
        