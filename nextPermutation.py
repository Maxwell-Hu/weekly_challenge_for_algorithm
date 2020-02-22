class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-2, -1, -1):
            # Return result if ---
            if nums[i] < nums[-1]:
                # Find idx.
                idx = len(nums) - 1
                for j in range(i+1, len(nums)-1):
                    if nums[j] > nums[i]:
                        idx = j
                        break
                nums[i], nums[idx] = nums[idx], nums[i]
                for j in range(len(nums)-1, i+1, -1):
                    if nums[j] < nums[j-1]:
                        nums[j], nums[j-1] = nums[j-1], nums[j]
                return nums

            # Resort from i to len(nums)-1
            tmp = nums[i]
            for j in range(i,len(nums)-1):
                nums[j] = nums[j+1]
            nums[-1] = tmp
        return nums
