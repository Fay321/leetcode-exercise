# -*- coding: utf-8 -*-
"""
这个参考https://zxi.mytechroad.com/blog/tree/leetcode-337-house-robber-iii/
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            #选这个node这棵最大值，左边子树的最大值，右边子树的最大值
            if root==None:
                return 0,0,0  
            l, ll, lr = dfs(root.left)
            r, rl, rr = dfs(root.right)
            return max(l+r, root.val+ll+lr+rl+rr), l, r
        return dfs(root)[0]