class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack(nums, [])
        return self.res

    def backtrack(self, nums, track):
        if len(nums) == len(track):
            self.res.append(track[:])
            return
        for num in nums:
            if num in track:
                continue
            track.append(num)
            self.backtrack(nums, track)
            track.pop()
