# -*- coding: utf-8 -*-
"""
判断链表是否有环
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None



class Solution1(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        set_record = set()
        while head:
            if head in set_record:
                return True
            else:
                set_record.add(head)
            head = head.next
        
        return False
    
    
'''
快慢指针：
https://blog.csdn.net/willduan1/article/details/50938210
设置一个快指针fp和一个慢指针sp，两个指针起始同时指向head节点，其中快指针每次走两步，慢指针每次走一步，那么如果链表有环的话他们一定能够相遇。可以想象两个人同时从操场上起跑，其中甲的速度是乙速度的2倍，那么当乙跑完一圈的时候甲也跑了两圈，他们一定能够相遇。
'''

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head==None:  #边界条件
            return False
        
        slow = head.next
        
        if head.next==None:
            return False
        else:
            fast = head.next.next
        
        while slow and fast:    
            if slow==fast:
                return True
            slow = slow.next
            
            if fast.next==None:
                return False
            else:
                fast = fast.next.next
        return False