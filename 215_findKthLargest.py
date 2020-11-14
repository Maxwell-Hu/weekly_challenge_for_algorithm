class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        for i in range(n, -1, -1):
            self.heapify(nums, n, i)

        res = nums[0]
        for i in range(n-1, -1, -1):
            if i == n-k:
                res = nums[0]
                break
            nums[i], nums[0] = nums[0], nums[i]
            self.heapify(nums, i, 0)
        return res

    def heapify(self, nums, n, i):
        l = 2 * i + 1
        r = 2 * i + 2
        largest = i

        if l < n and nums[largest] < nums[l]:
            largest = l

        if r < n and nums[largest] < nums[r]:
            largest = r

        if largest != i:
            nums[largest], nums[i] = nums[i], nums[largest]
            self.heapify(nums, n, largest)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import random
        if not nums: return None

        left, right = 0, len(nums) - 1

        while left <= right:
            index = self.__partition(nums, left, right)
            if len(nums)-index == k:
                return nums[index]
            elif len(nums)-index < k:
                right = index - 1
            else:
                left = index + 1

    def __partition(self, nums, left, right):
        ri = random.randint(left, right)
        nums[left], nums[ri] = nums[ri], nums[left]
        pivot = nums[left]
        j = left

        for i in range(left+1, right+1):
            if nums[i] < pivot:
                j += 1
                nums[j], nums[i] = nums[i], nums[j]

        nums[j], nums[left] = nums[left], nums[j]
        return j