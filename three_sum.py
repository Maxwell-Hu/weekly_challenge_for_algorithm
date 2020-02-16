class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i,num in enumerate(nums):
            if i>0 and nums[i-1] == nums[i]:
                continue
            outputs = self.twoSum(-num, nums[i+1:])
            if len(outputs):
                for output in outputs:
                    res.append([num]+output)
        
        tmp = set()
        for ll in res:
            tmp.add(tuple(sorted(ll)))
        return [ll for ll in tmp]

    def twoSum(self, target, nums: List[int]) -> List[List[int]]:
        hashmap = {}
        output = []
        for i,num in enumerate(nums):
            if hashmap.get(target - num) is not None:
                output.append([num, target - num])
            hashmap[num] = i
        return output
