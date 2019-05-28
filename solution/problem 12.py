# -*- coding: utf-8 -*-
'''https://leetcode.com/problems/integer-to-roman/submissions/'''
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        dic = {1:'I',4:'IV', 5:'V', 9:'IX',
              10:'X', 40:'XL', 50:'L', 90:'XC',
              100:'C',400:'CD', 500:'D', 900:'CM', 1000:'M'}
        
        sorting_lst = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        string = ''
        
        for e in sorting_lst:
            beishu = num//e
            string += beishu*dic[e]
            num = num % e
        return string
                