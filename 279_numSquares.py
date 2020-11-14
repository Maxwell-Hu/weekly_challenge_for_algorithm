class Solution:
    def numSquares(self, n: int) -> int:
        lookup = set([1])
        dp = [i for i in range(n+1)]
        for i in range(1, n+1):
            if int(i**0.5)**2 not in lookup:
                lookup.add(int(i**0.5)**2)
            dp[i] = min([1+dp[i-x] for x in lookup])
        return dp[-1]