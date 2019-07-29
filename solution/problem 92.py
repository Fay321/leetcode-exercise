# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/sort-list/
归并排序：https://www.cnblogs.com/chengxiao/p/6194356.html
trick:快慢指针
code ref: https://www.cnblogs.com/zuoyuan/p/3699508.html
"""

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def mergeList(self, head1, head2):
        head =  ListNode(0)
        dummy = head
        while head1 and head2:
            if head1.val< head2.val:
                dummy.next = head1
                dummy = dummy.next
                head1 = head1.next
            else:
                dummy.next = head2
                dummy = dummy.next
                head2 = head2.next
        
        if head1==None and head2!=None:
            dummy.next = head2
        elif head1!=None and head2==None:
            dummy.next = head1
        return head.next
    
    
    
    
    
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None or head.next==None:
            return head
        
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next    
        
        #一半
        head1 = head
        head2 = slow.next
        slow.next = None
        head1 = self.sortList(head1)
        head2 = self.sortList(head2)
        head_final = self.mergeList(head1, head2)
        return head_final