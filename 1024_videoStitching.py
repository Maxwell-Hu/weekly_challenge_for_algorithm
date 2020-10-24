class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        start, end = -1, 0
        candidates = []
        while True:
            tmp = [x for x in clips if start <= x[0] <= end and x[1] > end]
            if len(tmp) == 0:
                break
            q = max(tmp, key=lambda x: x[1])
            if q in candidates:
                break
            start, end = q[0], q[1]
            candidates.append(q)
            if end >= T:
                break
        if end < T or len(candidates) == 0:
            return -1
        return len(candidates)
