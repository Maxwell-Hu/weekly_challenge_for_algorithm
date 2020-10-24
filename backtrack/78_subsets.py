class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(track, nums):
            if len(nums) == 0 and track not in res:
                res.append(track)
            for i in range(len(nums)):
                helper(track[:] + [nums[i]], nums[i+1:][:])
                helper(track[:], nums[i+1:][:])
        res = []
        helper([], nums[:])
        return res
