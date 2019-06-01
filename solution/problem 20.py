# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #注意这个边界条件（深度为0）
        if root==None:
            return 0
    
        if root.left == None and root.right==None:
            return 1
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right))+1