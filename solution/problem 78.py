'''
https://leetcode.com/problems/add-two-numbers/
两个链表代表数字，求和
'''


# -*- coding: utf-8 -*-
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        head = None
        prev = None
        s2_before = 0
        
        while l1 or l2 or  s2_before:  #注意处理5+5=10这类情况
            a = l1.val if l1!=None else 0
            b = l2.val if l2!=None else 0
            s = a+b+s2_before
            s1, s2 = s%10, s//10  #当前位，进位
           
            
            if head==None:  
                head = ListNode(s1)
                prev = head
            else:
                prev.next = ListNode(s1)
                prev = prev.next
            
            if l1:
                l1 = l1.next
            else:
                l1 = None
                
            if l2:
                l2 = l2.next
            else:
                l2 = None
            
            s2_before = s2
        return head