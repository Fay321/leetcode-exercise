# -*- coding: utf-8 -*-
"""
判断链表是否构成回文
Palindrome Linked List
https://leetcode.com/problems/palindrome-linked-list/
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        lst = [] #记录这个链表的值
        while head:
            lst.append(head.val)
            head = head.next
        
        if lst==lst[::-1]:
            return True
        else:
            return False