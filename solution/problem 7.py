# -*- coding: utf-8 -*-
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = dict()
        for e in nums:
            if e in count:
                count[e] += 1
            else:
                count[e] = 1
            
            if count[e]>int(len(nums)/2):
                return e
        