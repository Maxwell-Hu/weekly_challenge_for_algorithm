class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup = dict()
        maxLength = 0

        for x in nums:
            if x not in lookup:
                left = lookup.get(x-1, 0)
                right = lookup.get(x+1, 0)
                lookup[x] = left + right + 1
                maxLength = max(maxLength, lookup[x])
                lookup[x - left] = lookup[x]
                lookup[x + right] = lookup[x]
        return maxLength