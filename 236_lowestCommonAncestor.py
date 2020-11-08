# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pq = []
        def getP(node, path, check):
            if node in check:
                pq.append(path[:]+[node])
                check.remove(node)
                if not len(check):
                    return
            if node.left: getP(node.left, path[:]+[node], check)
            if node.right: getP(node.right, path[:]+[node], check)

        getP(root, [], [p,q])
        for i in range(len(pq[0])-1, -1, -1):
            if pq[0][i] in pq[1]:
                return pq[0][i]


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left: return right
        if not right: return left
        return root