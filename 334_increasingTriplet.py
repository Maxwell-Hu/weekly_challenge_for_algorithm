class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        small, mid = float('inf'), float('inf')
        for num in nums:
            if num <= small:
                small = num
            elif num < mid:
                mid = num
            elif num > mid:
                return True
        return False
