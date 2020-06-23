class Solution:
    def waysToChange(self, n: int) -> int:
        coins = [1, 5, 10, 25]
        dp = [1] + [0] * n
        for coin in coins:
            for i in range(coin, n+1):
                dp[i] = dp[i-coin] + dp[i]

        return dp[-1] % 1000000007
