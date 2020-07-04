class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        dp = [[0]*(len(A)+1) for _ in range(len(B)+1)]
        max_length = 0

        for i in range(1, len(B)+1):
            for j in range(1, len(A)+1):
                if A[j-1]==B[i-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    max_length = max(max_length, dp[i][j])
        return max_length
