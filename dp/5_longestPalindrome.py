class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[-1]*len(s) for _ in range(len(s))]
        length = 0
        res = ''
        for i in range(len(s)-1, -1, -1):
            for j in range(i,len(s)):
                if s[i] == s[j]:
                    if i == j:
                        dp[i][j] = 1
                    elif i == j-1:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = dp[i+1][j-1]+2 if dp[i+1][j-1] > 0 else 0
                else:
                    dp[i][j] = 0
                if dp[i][j] > length:
                    length = dp[i][j]
                    res = s[i:j+1]
        return res
