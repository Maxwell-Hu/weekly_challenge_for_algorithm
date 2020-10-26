class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = int((left + right) / 2)
            if nums[mid] == target:
                return mid
            if (nums[left]<=target<nums[mid]) or (nums[left]>nums[mid] and target<nums[mid]) or\
                (nums[left]>nums[mid] and target>=nums[left]):
                right = mid-1
            else:
                left = mid+1
        return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif (nums[mid] < target <= nums[right]) or (nums[mid] > nums[right] and \
                target > nums[mid]) or (nums[mid] > nums[right] and target <= nums[right]):
                left = mid + 1
            else:
                right = mid - 1
        return -1