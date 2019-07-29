# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/linked-list-cycle-ii/submissions/
Linked List Cycle II
"""

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None



class Solution1(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        visited = set()
        node = head
        i = 0
        while node:
            if node not in visited:
                visited.add(node)
            else:
                return node
            i += 1
            node = node.next
        return None
    
'''
使用双指针判断链表中是否有环，慢指针每次走一步，快指针每次走两步，若链表中有环，则两指针必定相遇。
假设环的长度为l，环上入口距离链表头距离为a，两指针第一次相遇处距离环入口为b，则另一段环的长度为c=l-b，由于快指针走过的距离是慢指针的两倍，则有a+l+b=2*(a+b),又有l=b+c，可得a=c，故当判断有环时(slow==fast)时，移动头指针，同时移动慢指针，两指针相遇处即为环的入口。

https://www.jiuzhang.com/solution/linked-list-cycle-ii/
'''   
    
class Solution(object):
   
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = head
        slow = head
        while fast and slow:
            try:
                fast = fast.next.next
                slow = slow.next
                
                if slow==fast:  #有环状
                    break
            except:
                return None  #说明没有环状
        if fast==None:
            return None
        
            
        head_pt = head
        while True:
            if head_pt==slow:
                return head_pt
            else:
                head_pt = head_pt.next
                slow = slow.next
            
            
            