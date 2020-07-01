class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            tmp = [dp[j] for j in range(i) if nums[j] < nums[i]]
            if len(tmp)==0: continue
            max_length = max(tmp)
            dp[i] = max_length + 1
        return max(dp)
