# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root: return 0
        nums = []
        def getNum(num):
            res = num[0]
            for n in num[1:]:
                res = res*10 + n
            return res

        def getPath(root, path):
            if not root.left and not root.right:
                nums.append(path[:]+[root.val])
            if root.left:
                getPath(root.left, path[:]+[root.val])
            if root.right:
                getPath(root.right, path[:]+[root.val])

        getPath(root, [])
        print(nums)
        return sum([getNum(x) for x in nums])

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def getSum(root, s):
            if not root: return 0
            new_s = s * 10 + root.val
            if not root.left and not root.right:
                return new_s
            return getSum(root.left, new_s) + getSum(root.right, new_s)
        return getSum(root, 0)