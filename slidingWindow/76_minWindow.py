class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def helper(lookup, window):
            for kk,_ in lookup.items():
                if window[kk] < lookup[kk]:
                    return False
            return True

        left=0; res=''; minLength=len(s)
        lookup = {x: t.count(x) for x in t}
        window = {x: 0 for x in t}
        for right in range(len(s)):
            if s[right] in window: 
                window[s[right]] += 1
                while helper(lookup, window) > 0:
                    if right - left < minLength:
                        minLength = right - left
                        res = s[left: right+1]
                    if s[left] in window:
                        window[s[left]] -= 1
                    left += 1
        return res
