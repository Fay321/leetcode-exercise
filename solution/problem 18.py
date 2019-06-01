# -*- coding: utf-8 -*-


class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new_nums = sorted(nums)
        start =  None
        end = None
        for i in range(len(nums)):
            if new_nums[i]==nums[i]:
                pass
            else:
                if start == None:
                    start = i
                end = i
        if start ==None:
            return 0
        else:
            return end-start+1