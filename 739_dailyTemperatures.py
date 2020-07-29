class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        res = [0] * len(T)
        for i, num in enumerate(T):
            if len(stack) == 0:
                stack.append((i,num))
                continue
            if stack[-1][1] < num:
                while len(stack):
                    if stack[-1][1] >= num: break
                    res[stack[-1][0]] = i - stack[-1][0]
                    stack.pop()
            stack.append((i, num))
        return res
