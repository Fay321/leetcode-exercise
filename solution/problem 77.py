# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 21:34:36 2019

@author: fay
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution1(object):
    '''尝试了Memory O(N)的方法'''
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        contain_node_set = set()
        node = headA
        while node:
            contain_node_set.add(node)
            node = node.next
            
        node = headB
        while node:
            if node in contain_node_set:
                return node
            node = node.next
        return 
    
    
'''
memory O(1)
分别遍历两个链表，得到分别对应的长度。然后求长度的差值，把较长的那个链表向后移动这个差值的个数，
然后一一比较即可。 
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        length_A = 0
        node = headA
        while node:
            length_A += 1
            node = node.next
        
        length_B = 0
        node = headB
        while node:
            length_B += 1
            node = node.next
            
        if length_A>length_B:
            i = 0
            while i<length_A-length_B:
                headA = headA.next
                i += 1
        elif length_A<length_B:
            i = 0
            while i<length_B-length_A:
                headB = headB.next
                i += 1
        else: 
            pass
        
        
        #这样headA， headB等长
        while headA and headB:
            if headA==headB:
                return headA
            headA = headA.next
            headB = headB.next
        return 
