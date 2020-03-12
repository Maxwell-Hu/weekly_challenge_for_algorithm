# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

class Solution_iterative:
    def invertTree(self, root: TreeNode) -> TreeNode:
        stack = []
        if root:
            stack.append(root)
        while stack:
            p = stack.pop()
            p.left, p.right = p.right, p.left
            if p.left:
                stack.append(p.left)
            if p.right:
                stack.append(p.right)
        return root
