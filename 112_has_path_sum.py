# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None:
            if root.val == sum:
                return True
            else:
                return False
        return self.hasPathSum(root.left, sum-root.val) \
                or self.hasPathSum(root.right, sum-root.val)


class Solution_iteration:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        stack = [(root, sum)]
        res = False
        while stack:
            curr = stack.pop()
            if curr[0].left is None and curr[0].right is None:
                if curr[0].val == curr[1]:
                    res = True
                    break
            if curr[0].left:
                stack.append((curr[0].left, curr[1]-curr[0].val))
            if curr[0].right:
                stack.append((curr[0].right, curr[1]-curr[0].val))
        return res
