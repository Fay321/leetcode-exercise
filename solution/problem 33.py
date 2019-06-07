# -*- coding: utf-8 -*-
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        count_dic = {0:0,1:0,2:0}
        for e in nums:
            count_dic[e] += 1
        
        for j in range(len(nums)):
            if j<count_dic[0]:
                nums[j] = 0
            elif j<count_dic[0]+count_dic[1]:
                nums[j] = 1
            else:
                nums[j] = 2