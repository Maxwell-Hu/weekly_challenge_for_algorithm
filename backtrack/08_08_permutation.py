class Solution:
    def permutation(self, S: str) -> List[str]:
        def backtrack(track, s):
            if track in lookup:
                return
            if len(s) == 0:
                res.append(track)
            lookup.append(track)
            for i,ch in enumerate(s):
                backtrack(track+ch, s[:i]+s[i+1:])
        res = []
        lookup = []
        backtrack('', S)
        return res
