class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        fl, sl = len(first), len(second)
        if abs(fl - sl) >= 2:
            return False
        for i in range(min(fl, sl)):
            if first[i] == second[i]:
                continue
            else:
                return first[i:] == second[i+1:] or first[i+1:] == second[i:] or \
                first[i+1:] == second[i+1:]
        return True
