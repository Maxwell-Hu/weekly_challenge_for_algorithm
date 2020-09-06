# -*- coding:utf-8 -*-

class Finder:
    def findKth(self, a, n, K):
        # write code here
        K = n-K
        def helper(left, right):
            pivot = a[left]
            p, q = left, right
            while p < q:
                while a[q] >= pivot and p < q:
                    q -= 1
                a[p] = a[q]
                while a[p] <= pivot and p < q:
                    p += 1
                a[q] = a[p]
            a[p] = pivot
            if p == K:
                return a[p]
            elif p < K:
                return helper(p+1, right)
            else:
                return helper(left, p-1)
        return helper(0, len(a)-1)
