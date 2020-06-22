# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        return self.helper(root.left, root.right)

    def helper(self, root1: TreeNode, root2: TreeNode):
        if root1 == None and root2 == None:
            return True
        elif (root1 == None and root2 != None) or (root1 != None and root2 == None) or (root1.val != root2.val):
            return False
        return self.helper(root1.left, root2.right) and self.helper(root1.right, root2.left)
