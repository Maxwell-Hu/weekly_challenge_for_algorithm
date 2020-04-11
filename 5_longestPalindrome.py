class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0: return ''
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1
        for j in range(1, len(s)):
            for i in range(j-1, -1, -1):
                if s[i] == s[j]:
                    if i+2 == j:
                        dp[i][j] = 3
                    elif i+1 == j:
                        dp[i][j] = 2
                    else:
                        if dp[i+1][j-1] == j-i-1:
                            dp[i][j] = dp[i+1][j-1] + 2
                        else:
                            dp[i][j] = max(dp[i+1][j], dp[i][j-1])
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])

        res_i, res_j = 0, len(s)-1
        if dp[res_i][res_j] == 1:
            return s[res_i]
        while True:
            if dp[res_i+1][res_j-1] == dp[res_i][res_j]:
                res_i, res_j = res_i + 1, res_j - 1
            elif dp[res_i+1][res_j] == dp[res_i][res_j]:
                res_i, res_j = res_i + 1, res_j
            elif dp[res_i][res_j-1] == dp[res_i][res_j]:
                res_i, res_j = res_i, res_j-1
            else:
                break
        return s[res_i:res_j+1]
