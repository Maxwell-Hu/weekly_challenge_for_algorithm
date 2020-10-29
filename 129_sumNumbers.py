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