# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def getDepth(root, depth):
            if root == None:
                return depth-1
            return max(getDepth(root.left, depth+1), getDepth(root.right, depth+1))
        return getDepth(root, 1)


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None: return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
