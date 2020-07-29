class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0: return []
        self.mapper = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl',
                        '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        self.res = []
        self.incursive('', digits)
        return self.res

    def incursive(self, s, digits):
        if len(digits) == 0:
            self.res.append(s)
            return
        for ch in self.mapper[digits[0]]:
            self.incursive(s+ch, digits[1:])
