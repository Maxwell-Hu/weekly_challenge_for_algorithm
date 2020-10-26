class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        res = []
        i = 0
        while i <= len(intervals) - 1:
            start = i
            while i < len(intervals) - 1 and intervals[i+1][0] <= max([x[1] for x in intervals[start: i+1]]):
                i += 1
            res.append([intervals[start][0], max([x[1] for x in intervals[start: i+1]])])
            i += 1
        return res