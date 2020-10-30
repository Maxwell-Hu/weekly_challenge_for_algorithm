class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lookup = set()
        cur_len = 0
        max_len = 0
        left = 0
        for i in range(len(s)):
            cur_len += 1
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
            if cur_len > max_len: max_len = cur_len
            lookup.add(s[i])
        return max_len