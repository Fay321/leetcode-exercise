# -*- coding: utf-8 -*-
"""

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root==None:
            return 0
        else:
            return self.pathSumVer2(root, sum, False)
    
    def pathSumVer2(self, root, sum, ifStart):
        '''ifStart=True说明之前已经选了某个点了，就必须选到底了'''
        num = 0
        
        if root.val == sum:
            num += 1  #注意这里不是return 1
       
        if ifStart==False:
            if root.left:
                num += self.pathSumVer2(root.left, sum, False)
                num += self.pathSumVer2(root.left, sum-root.val, True)  
            if root.right:
                num += self.pathSumVer2(root.right, sum, False)
                num += self.pathSumVer2(root.right, sum-root.val, True)
        else:
            if root.left:
                num += self.pathSumVer2(root.left, sum-root.val, True)
            if root.right:
                num += self.pathSumVer2(root.right, sum-root.val, True)
               
        return num