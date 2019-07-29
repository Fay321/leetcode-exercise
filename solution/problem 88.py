# -*- coding: utf-8 -*-
"""
Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution1(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        node = head
        lst = []
        while node:
            lst.append(node)
            node = node.next

        if n==len(lst): #去掉头部
            return lst[1] if len(lst)>=2 else None
        elif n!=len(lst) and n==1: #去掉最后一个
            lst[-n-1].next = None
            return lst[0]
        else:
            lst[-n-1].next = lst[-n+1]
            return lst[0]