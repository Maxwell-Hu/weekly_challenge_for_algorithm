class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 0: return 0
        m,n = len(matrix), len(matrix[0])
        store = [[0]*n for _ in range(m)]

        def getLength(i, j):
            if i<0 or j<0:
                return 0
            elif store[i][j] != 0:
                return store[i][j]
            else:
                length1 = getLength(i-1, j) if i-1 >= 0 and matrix[i-1][j] < matrix[i][j] else 0
                length2 = getLength(i+1, j) if i+1 < m and matrix[i+1][j] < matrix[i][j] else 0
                length3 = getLength(i, j-1) if j-1 >= 0 and matrix[i][j-1] < matrix[i][j] else 0
                length4 = getLength(i, j+1) if j+1 < n and matrix[i][j+1] < matrix[i][j] else 0
                store[i][j] = max(length1, length2, length3, length4) + 1
                return store[i][j]

        res = 0
        for i in range(m):
            for j in range(n):
                if res < getLength(i, j):
                    res = getLength(i, j)
        return res
