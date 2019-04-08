# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/palindrome-number/submissions/
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        a = str(x)
        b = a[::-1]
        return a==b