# -*- coding: utf-8 -*-
"""
最开始没想到思路

https://blog.csdn.net/fuxuemingzhu/article/details/79132336

BST的右子树都比该节点大，所以修改次序是右–>中–>左。用一个变量储存遍历过程中所有有节点之和就得到了所有的比当前把该节点的值更大的和，然后修改为该变量的值即可。
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        #BST树：右>中>左
        self.sum = 0
        
        def update(cur):
            if cur==None:
                return
            
            update(cur.right)
            self.sum += cur.val
            cur.val = self.sum
            update(cur.left)
        
        update(root)
        return root           
        
