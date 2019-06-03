# -*- coding: utf-8 -*-

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        first = None
        while True:
            if l1==None and l2==None:  #边界条件分细致点没有出错
                break
            if l2==None and l1!=None:
                if first==None:
                    first = ListNode(l1.val)
                    prev = first
                else:
                    prev.next = ListNode(l1.val)
                    prev = prev.next
                l1 = l1.next
            elif l1==None and l2!=None:
                if first==None:
                    first = ListNode(l2.val)
                    prev = first
                else:
                    prev.next = ListNode(l2.val)
                    prev = prev.next
                l2 = l2.next
            else:
                if (l1.val < l2.val or l1.val==l2.val):
                    if first==None:
                        first = ListNode(l1.val)
                        prev = first
                    else:
                        prev.next = ListNode(l1.val)
                        prev = prev.next
                    l1 = l1.next
                else:
                    if first==None:
                        first = ListNode(l2.val)
                        prev = first
                    else:
                        prev.next = ListNode(l2.val)
                        prev = prev.next
                    l2 = l2.next
             
        return first