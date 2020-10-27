class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def getRange(start, end):
            mid = (start + end) // 2
            if start > end: return [-1, -1]
            if nums[mid] == target:
                l, r = mid, mid
                while l-1 >= 0 and nums[l-1] == target:
                    l -= 1
                while r+1 <= len(nums)-1 and nums[r+1] == target:
                    r += 1
                return [l,r]
            elif nums[mid] < target:
                return getRange(mid+1, end)
            else:
                return getRange(start, mid-1)

        return getRange(0, len(nums) - 1)