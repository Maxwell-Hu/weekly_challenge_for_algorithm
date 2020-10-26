class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0: return False
        i = len(matrix) - 1
        j = 0
        while 0 <= i <= len(matrix) - 1 and 0 <= j <= len(matrix[0]) - 1:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                i -= 1
            else:
                if i+1 <= len(matrix) - 1 and matrix[i+1][j] < target:
                    i += 1
                elif j+1 <= len(matrix[0]) - 1:
                    j += 1
                else:
                    return False
        return False