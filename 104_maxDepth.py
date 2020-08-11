# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def getDepth(root, depth):
            if root==None:
                return depth
            return max(getDepth(root.left, depth+1), getDepth(root.right, depth+1))
        return getDepth(root, 0)
