class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        lo, hi = 1, max(piles)
        while lo < hi:
            mid = (lo + hi) // 2
            if sum((x-1)//mid+1 for x in piles) > H:
                lo = mid+1
            else:
                hi = mid
        return hi