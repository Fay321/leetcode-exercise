# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/merge-k-sorted-lists/
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if lists==[]:
            return None
        
        lst = []
        for l in lists:
            while l:
                lst.append(l.val)
                l = l.next
        
        lst = sorted(lst)
        node = dummy = ListNode(0)
        for a in lst:
            node.next = ListNode(a)
            node = node.next
        return dummy.next



class Solution1(object):
    ''' 超时 '''
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if lists==[]:
            return None
        
        dummy = ListNode(0)
        node = dummy
        
        inf = float('inf')
        while True:
            compare_value = []
            for a in lists:
                compare_value.append(a.val if a!=None else inf)
            
            min_value = min(compare_value)
            
            if set(compare_value) == {inf}:
                return dummy.next
            
            min_index = compare_value.index(min_value)
            if lists[min_index]:
                lists[min_index] = lists[min_index].next
            
            node.next = ListNode(min_value)
            node = node.next