# -*- coding: utf-8 -*-

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

''' 二叉树的中序遍历顺序为左-根-右 '''
''' 思路：递归'''
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
       
        if root!=None and root.left == None and root.right==None:
            return [root.val]
        if root==None:
            return []
        
        order = self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        return order



''' 用栈：
思路是从根节点开始，先将根节点压入栈，然后再将其所有左子结点压入栈，然后取出栈顶节点，保存节点值，再将当前指针移到其右子节点上，若存在右子节点，则在下次循环时又可将其所有左子结点压入栈中
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root ==None:
            return []
        
        stack = []
        out_lst = []
      
        
        while root or stack:
            #这个根节点的所有左节点
            while root:
                stack.append(root)
                root = root.left
            
            #然后看栈的元素
            while stack:
                e = stack.pop()
                out_lst.append(e.val)
                if e.right!=None:
                    print('aaaa')
                    root = e.right
                    break
          
        return out_lst
                