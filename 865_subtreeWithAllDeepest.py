# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        depth = {}
        def getDepth(root, dep):
            depth[root] = dep
            if root.left:
                getDepth(root.left, dep + 1)
            if root.right:
                getDepth(root.right, dep + 1)
        getDepth(root, 1)
        maxDepth = max(depth.values())

        def getNode(root):
            if not root or depth.get(root, None) == maxDepth:
                return root
            L, R = getNode(root.left), getNode(root.right)
            return root if L and R else L or R

        return getNode(root)