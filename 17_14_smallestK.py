class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        def sort(nums):
            if len(nums) <= 1:
                return nums
            left = [num for num in nums[1:] if num <= nums[0]]
            right = [num for num in nums[1:] if num > nums[0]]
            if len(left) >= k-1:
                return sort(left) + [nums[0]]
            return sort(left) + [nums[0]] + sort(right)
        sorted_arr = sort(arr)
        return sorted_arr[:k]
