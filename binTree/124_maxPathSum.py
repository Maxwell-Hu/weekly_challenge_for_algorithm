# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def getMaxGain(root):
            if root == None:
                return 0
            left_gain = getMaxGain(root.left)
            right_gain = getMaxGain(root.right)
            root.gain = root.val+max(0, left_gain, right_gain)
            return root.gain

        root_gain = getMaxGain(root)
        self.maxGain = float("-inf")
        def getRes(root):
            if root == None:
                return
            left = 0 if root.left == None else root.left.gain
            right = 0 if root.right == None else root.right.gain
            res = root.val
            if left > 0:
                res += left
            if right > 0:
                res += right
            if res > self.maxGain:
                self.maxGain = res
            getRes(root.left)
            getRes(root.right)
        getRes(root)
        return self.maxGain

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxSum = float('-inf')
        def dfs(root):
            if root == None:
                return (0, 0) # maxGain, maxSum
            leftGain, leftSum = dfs(root.left)
            rightGain, rightSum = dfs(root.right)
            curGain = root.val + max(max(0, leftGain), max(0, rightGain))
            curSum = root.val + max(0, leftGain) + max(0, rightGain)
            if curSum > self.maxSum:
                self.maxSum = curSum
            return (curGain, curSum)
        _ = dfs(root)
        return self.maxSum

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxSum = float('-inf')
        def dfs(root):
            if root == None: return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.maxSum = max(self.maxSum, root.val + max(0, left) + max(0, right))
            return root.val + max(max(0, left), max(0, right))
        _ = dfs(root)
        return self.maxSum
