# -*- coding: utf-8 -*-
"""
single-number
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = set()
        
        if len(nums)==1:
            return nums[0]
        
        for a in nums:
            if a in dic:
                dic.remove(a)
            else:
                dic.add(a)
        return dic.pop()
