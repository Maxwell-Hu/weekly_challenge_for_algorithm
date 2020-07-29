class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dp = [0] * len(s)
        strs = ''
        maxLength = 0
        for i,ch in enumerate(s):
            if ch not in strs:
                strs += ch
                maxLength += 1
                dp[i] = maxLength
            else:
                idx = strs.index(ch)
                strs = strs[idx+1:] + ch
                maxLength = len(strs)
                dp[i] = maxLength
        return max(dp) if dp else 0
