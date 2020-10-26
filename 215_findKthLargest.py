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