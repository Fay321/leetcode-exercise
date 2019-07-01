# -*- coding: utf-8 -*-
"""
检查是否为对称树
https://leetcode.com/problems/symmetric-tree

1）边界条件 空树
2） [None,3] [None,3]这种不是对称数，注意要考虑空节点
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        #看左右子树每一层节点是否对称
        if root==None:
            return True
        
     
      
        left_node_lst = [root.left]
        right_node_lst = [root.right]
        
        
        while left_node_lst and right_node_lst:
            if len(left_node_lst)!=len(right_node_lst):
                return False
            
            left_value = []
            right_value = []
            left_node_next_layer = []
            right_node_next_layer = []
            
            #左侧
            for node in left_node_lst:
                if node==None:
                    left_value.append(node)
                else:
                    left_value.append(node.val)              
                    left_node_next_layer.append(node.left)
                    left_node_next_layer.append(node.right)
            
            # 右侧
            for node in right_node_lst:
                if node==None:
                    right_value.append(node)
                else:
                    right_value.append(node.val)
                    right_node_next_layer.append(node.left)
                    right_node_next_layer.append(node.right)
            
            right_node_lst = right_node_next_layer
            left_node_lst = left_node_next_layer
            #print(left_value, right_value)
            if left_value!=right_value[::-1]:
                return False
        return True
            