class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*(n+1) for _ in range(m+1)]
        dp[1][1] = 1

        for i in range(1, m+1):
            for j in range(1, n+1):
                if i == 1 and j == 1: continue
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        print(dp)
        return dp[m][n]

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * m
        for i in range(n-1):
            for j in range(1,m):
                dp[j] = dp[j-1] + dp[j]
        return dp[-1]
