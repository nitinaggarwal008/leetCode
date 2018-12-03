# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        m = [float('-inf')]
        def dfs(root):
            v = root.val
            l = dfs(root.left) if root.left else 0
            r = dfs(root.right) if root.right else 0
            res = max(v, v+l, v+r)
            m[0] = max(res, m[0], v+l+r)
            return res
        dfs(root)
        return m[0]                
