class Solution:
    def numTrees(self, n: int) -> int:
        self.dp = [0] * (n+1)
        self.dp[0], self.dp[1] = 1,1
        for i in range(2,n+1):
            for j in range(i):
                self.dp[i] += self.dp[j] * self.dp[i-j-1]
        return self.dp[-1]

