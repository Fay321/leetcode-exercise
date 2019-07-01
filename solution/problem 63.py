# -*- coding: utf-8 -*-
'''https://leetcode.com/problems/binary-tree-level-order-traversal/
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        layer = [root]
        next_layer = [] #记录下一层的节点
        out_lst = []
        
        while layer:
            lst = [] 
            for node in layer:
                if node==None:
                    continue
                
                lst.append(node.val)
                
                if node.left!=None:
                    next_layer.append(node.left)
                if node.right!=None:
                    next_layer.append(node.right)
           
            layer = next_layer
            next_layer = []
            if lst!=[]:
                out_lst.append(lst)
            
        return out_lst