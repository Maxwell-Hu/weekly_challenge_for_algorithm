class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def findMedian(arr1, arr2, k):
            if not arr1 or not arr2:
                res = arr1[k-1] if arr1 else arr2[k-1]
                return res
            if k == 1:
                res = arr1[0] if arr1[0] < arr2[0] else arr2[0]
                return res
            k1 = len(arr1)-1 if len(arr1) < (k)//2 else (k)//2-1
            k2 = len(arr2)-1 if len(arr2) < (k)//2 else (k)//2-1
            if arr1[k1] < arr2[k2]:
                return findMedian(arr1[k1+1:][:], arr2, k-k1-1)
            else:
                return findMedian(arr1, arr2[k2+1:][:], k-k2-1)

        if (len(nums1)+len(nums2))%2:
            return findMedian(nums1, nums2, (len(nums1)+len(nums2)+1)//2)
        else:
            return (findMedian(nums1, nums2, (len(nums1)+len(nums2))//2) + findMedian(nums1, nums2, (len(nums1)+len(nums2))//2 + 1)) / 2