# -*- coding: utf-8 -*-

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        
        
        if t1==None and t2==None:
            return None
        elif t1==None and t2!=None:
            return t2
        elif t1!=None and t2==None:
            return t1

        start = TreeNode(self.sum_none(t1.val, t2.val))
        start.left = self.mergeTrees(t1.left, t2.left)
        start.right = self.mergeTrees(t1.right, t2.right)
        return start
    
    def sum_none(self,a,b):
        if a==None:
            a = 0
        if b==None:
            b = 0
        return a+b