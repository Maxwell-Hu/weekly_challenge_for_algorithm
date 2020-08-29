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

class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        if k==0 or k>len(arr): return []
        import heapq
        heap = []
        for i in arr[:k]:
            heapq.heappush(heap, -i)
        for i in arr[k:]:
            if i < -heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, -i)
        res = [-i for i in heap]
        return res
