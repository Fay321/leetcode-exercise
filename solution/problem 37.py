# -*- coding: utf-8 -*-

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        res_lst = []
        for i in range(len(nums)):
            if i==0:
                res_lst.append(nums[i])
            else:
                res_lst.append(max(nums[i]+res_lst[i-1],nums[i]))
        
        max_value = max(res_lst)
        return max_value