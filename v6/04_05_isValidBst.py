# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def valid(root, mi, ma):
            if root == None: return True
            if root.val <= mi:
                return False
            if root.val >= ma:
                return False
            return valid(root.left, mi, root.val) and valid(root.right, root.val, ma)
        return valid(root, -float('inf'), float('inf'))
