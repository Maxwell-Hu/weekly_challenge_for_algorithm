class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[float('inf')] * (n+1) for _ in range(m+1)]
        dp[1][1] = grid[0][0]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if i==1 and j==1: continue
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i-1][j-1]
        return dp[m][n]

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == j == 0: continue
                if i==0: grid[i][j] += grid[i][j-1]
                elif j==0: grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] += min(grid[i][j-1], grid[i-1][j])
        return grid[-1][-1]
