class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        lookup1 = dict()
        lookup2 = dict()
        length = len(A)
        for i in range(length):
            for j in range(length):
                if A[i]+B[j] not in lookup1:
                    lookup1[A[i]+B[j]] = 0
                lookup1[A[i]+B[j]] += 1
                if C[i]+D[j] not in lookup2:
                    lookup2[C[i]+D[j]] = 0
                lookup2[C[i]+D[j]] += 1

        res = 0
        for k1, v1 in lookup1.items():
            if -k1 in lookup2:
                res += v1 * lookup2[-k1]
        return res
