class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1
        res = sorted(count.items(), key=lambda x: x[1], reverse=True)
        return [x[0] for x in res[:k]]
