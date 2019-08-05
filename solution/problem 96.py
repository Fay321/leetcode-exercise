# -*- coding: utf-8 -*-
'''
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        lst = []
        prev_layer = [root]
        while prev_layer:
            new_layer = []
            for node in prev_layer:
                lst.append(node.val if node!=None else None)
                if node:
                    new_layer += [node.left,node.right]
            prev_layer = new_layer
        return str(lst)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        lst = eval(data)
        if len(lst)<=1:
            return None
        
        head = TreeNode(lst[0])
        prev_layer = [head]
        next_layer = []
        idx = 1
        
        while idx<=len(lst)-1:
        
            for node in prev_layer:
                
                a = TreeNode( lst[idx] ) if lst[idx]!=None else None
                b = TreeNode( lst[idx+1]) if lst[idx+1]!=None else None
                node.left = a
                node.right = b
                
                if a!=None:
                    next_layer.append(a)
                if b!=None:
                    next_layer.append(b)
                    
                idx += 2
            prev_layer = next_layer
        return head
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))