# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root==None:
            return root
        
        out = self.dfs(root)
        prev = root
        if len(out)<=1:
            return root
        else:
            for e in out[1:]:
                prev.left = None
                prev.right = TreeNode(e)
                prev = prev.right
        
        
        
    def dfs(self,node):
        '''得到这个node下所有节点'''
        out_lst = [node.val]
        if node.left:
            out_lst += self.dfs(node.left)
        if node.right:
            out_lst += self.dfs(node.right)
        return out_lst