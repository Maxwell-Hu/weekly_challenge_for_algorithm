# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.res = []
        def dfs(root):
            if root == None:
                self.res.append(None)
                return
            self.res.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return self.res

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        self.cur = 0
        def dfs():
            if data[self.cur] == None:
                return None
            newNode = TreeNode(data[self.cur])
            self.cur += 1
            if self.cur >= len(data): return
            newNode.left = dfs()
            self.cur += 1
            if self.cur >= len(data): return
            newNode.right = dfs()
            return newNode
        root = dfs()
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
