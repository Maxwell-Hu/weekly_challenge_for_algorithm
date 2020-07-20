class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            left = right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
            if i < len(s)-1:
                left, right = i, i+1
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    res += 1
                    left -= 1
                    right += 1
        return res