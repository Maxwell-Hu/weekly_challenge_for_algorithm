# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None: return []
        left = [root]
        right = []
        res = []
        while len(left) or len(right):
            if len(left):
                res.append([node.val for node in left])
            right = []
            for node in left[::-1]:
                if node.right:
                    right.append(node.right)
                if node.left:
                    right.append(node.left)
            if len(right):
                res.append([node.val for node in right])

            left = []
            for node in right[::-1]:
                if node.left:
                    left.append(node.left)
                if node.right:
                    left.append(node.right)
        return res
