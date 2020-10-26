class Solution:
    def longestMountain(self, A: List[int]) -> int:
        if len(A) <= 2: return 0
        candidates = []
        for i in range(1, len(A)-1):
            if A[i] > A[i-1] and A[i] > A[i+1]:
                candidates.append(i)
        
        maxLength = 0
        for i in candidates:
            l = i - 1
            r = i + 1
            while l > 0 and A[l] > A[l-1]:
                l -= 1
            while r < len(A) - 1 and A[r] > A[r+1]:
                r += 1
            if r - l + 1 > maxLength:
                maxLength = r - l + 1
        return maxLength