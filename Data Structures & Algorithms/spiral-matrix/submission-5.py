class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        minRow, maxRow, minCol, maxCol = 0, len(matrix), 0, len(matrix[0])
        res = []
        row = 0
        while minRow < maxRow and minCol < maxCol:
            for col in range(minCol, maxCol):
                res.append(matrix[row][col])
            minRow += 1
            for row in range(minRow, maxRow):
                res.append(matrix[row][col])
            maxCol -= 1

            if minRow < maxRow and minCol < maxCol:
                for col in range(maxCol-1, minCol-1, -1):
                    res.append(matrix[row][col])
                maxRow -= 1
                for row in range(maxRow-1, minRow-1, -1):
                    res.append(matrix[row][col])
                minCol += 1
        return res
