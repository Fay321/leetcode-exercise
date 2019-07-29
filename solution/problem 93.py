# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/validate-binary-search-tree/
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            return self.valid(root, None , None)
        else:
            return True
    
    def valid(self, node, min_value, max_value):
        
        
        if min_value and max_value and min_value<node.val<max_value:
            pass
        elif min_value==None and max_value!=None and node.val<max_value:
            pass
        elif min_value!=None and max_value==None and node.val>min_value:
            pass
        elif min_value==None and max_value==None:
            pass
        else:
            return False
        
        if node.left:
            left = self.valid(node.left, min_value, min(max_value, node.val) if max_value!=None else node.val)
        else:
            left = True
            
        if node.right:
            right = self.valid(node.right, max(min_value,node.val) if min_value!=None else node.val , max_value)
        else:
            right = True
        
        
        if left and right:
            return True
        else:
            return False