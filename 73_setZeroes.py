class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        column = []
        row = []
        def setZero(row, column):
            for i in row:
                for k in range(0, len(matrix[0])):
                    matrix[i][k] = 0
            for j in column:
                for k in range(0, len(matrix)):
                    matrix[k][j] = 0

        i, j = 0, 0
        while i<len(matrix) and j<len(matrix[0]):
            if matrix[i][j] == 0:
                if i not in row:
                    row.append(i)
                if j not in column:
                    column.append(j)
            if j+1 > len(matrix[0]) - 1:
                i += 1
                j = 0
            else:
                j += 1
        setZero(row, column)
        return matrix

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        column, row = set(), set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row.add(i)
                    column.add(j)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in row or j in column:
                    matrix[i][j] = 0