# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
root是preorder序列的第一个节点
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if preorder==[]:
            return 
        
        root_val = preorder[0]
        
        #确定左右子树
        i = inorder.index(root_val)
                
        left_tree_inorder = inorder[:i]
        right_tree_inorder = inorder[(i+1):]
        n  = len(left_tree_inorder)
        left_tree_preorder = preorder[1:1+n]
        right_tree_preorder =preorder[1+n:]
        
        root = TreeNode(root_val)
        root.left = self.buildTree(left_tree_preorder, left_tree_inorder)
        root.right = self.buildTree(right_tree_preorder, right_tree_inorder)
        return root