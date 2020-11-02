class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        sumH = 0
        q = []
        for i in range(1, len(heights)):
            if heights[i] > heights[i-1]:
                heapq.heappush(q, heights[i]-heights[i-1])
                if len(q) > ladders:
                    sumH += heapq.heappop(q)
                if sumH > bricks:
                    return i-1
        return len(heights) - 1