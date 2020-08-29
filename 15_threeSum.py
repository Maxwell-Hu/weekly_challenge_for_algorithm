class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        # [-4, -1, -1, 0, 1, 2]
        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i-1] == nums[i]:
                continue
            left, right = i+1, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == -nums[i]:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] > -nums[i]:
                    right -= 1
                else:
                    left += 1
        return res

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, v1 in enumerate(nums[:-2]):
            if v1 > 0: break
            if i>0 and nums[i] == nums[i-1]: continue
            lookup = set()
            tmp = set()
            for j, v2 in enumerate(nums[i+1:]):
                if -v1 - v2 in lookup:
                    tmp.add((v1, -v1-v2, v2))
                lookup.add(v2)
            res.extend(tmp)
        return list(map(list, res))
