# -*- coding: utf-8 -*-
"""
Diameter of Binary Tree
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return 0
        
        self.max_length = 0
        def dfs(node):
            '''确定node左边长度，右侧长度'''
            if node.left:
                left_h = 1+ max(dfs(node.left) )
            else:
                left_h = 0
            
            if node.right:
                right_h = 1+ max(dfs(node.right))
            else:
                right_h =0
                
            self.max_length = max(self.max_length, left_h+right_h)
            return left_h, right_h
        
        dfs(root)
        return self.max_length   