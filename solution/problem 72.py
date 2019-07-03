# -*- coding: utf-8 -*-
"""
把包含正整数的lst分为和相等的子列
"""

import numpy as np
class Solution1(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums==[]: #可能边界
            return False
        
        sum_value = sum(nums)
        if sum_value%2!=0:
            return False
        target = sum_value/2
        
        
        for i,value in enumerate(nums):
            if i==0:
                layer = np.unique( np.array([0, nums[0]]) )
            else:
                layer = np.unique( np.concatenate((layer, layer+value)) )
            
            
            if target in layer:
                return True
            else:
                layer = layer[layer<target]
                if len(layer)==0:
                    return False
        
        return False

#---用动态规划的话，memory用得少些--#
class Solution:
    def canPartition(self, nums):
        numSum=sum(nums)
        if numSum%2!=0:
            return False
        dp=[0]*(numSum+1)
        dp[0]=1
        
        for num in nums:
            for i in range(numSum,-1,-1):
                if dp[i]:
                    dp[num+i]=1
            if dp[int(numSum/2)]==1:
                return True
        return False
        