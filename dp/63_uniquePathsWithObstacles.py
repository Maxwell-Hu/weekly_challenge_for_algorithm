class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        import copy
        dp = copy.deepcopy(obstacleGrid)
        dp[0][0] = 0 if obstacleGrid[0][0] else 1
        for i in range(1,len(obstacleGrid)):
            dp[i][0] = 0 if obstacleGrid[i-1][0] or obstacleGrid[i][0] else dp[i-1][0]
        for i in range(1,len(obstacleGrid[0])):
            dp[0][i] = 0 if obstacleGrid[0][i-1] or obstacleGrid[0][i] else dp[0][i-1]
        for i in range(1,len(dp)):
            for j in range(1,len(dp[i])):
                if obstacleGrid[i][j]:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
