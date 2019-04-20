# -*- coding: utf-8 -*-
#在一列数组中取出一个或多个不相邻数，使其和最大

class Solution1(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        
        elif len(nums)<=2 and len(nums)>=1:
            return max(nums)
        
        s_a = nums[0]  #到i位置总和最大值
        s_b = max(nums[1], s_a)   #到i+1位置总和最大值
        
        for j in range(2,len(nums)):
            e = nums[j]
            if s_a + e>= s_b:
                s_a, s_b = s_b, s_a + e
            else:
                s_a = s_b
        return s_b

class Solution2(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        elif len(nums)<=2:
            return max(nums)
        else:
            pass
        
        dic = dict()  #记录 到i位置最大和
        dic[0] = nums[0]
        dic[1] = max(nums[0],nums[1])
        for j in range(2, len(nums)):
            e = nums[j]
            if e+dic[j-2]>= dic[j-1]:
                dic[j] = e+dic[j-2]
            else:
                dic[j] = dic[j-1]
        
        return dic[len(nums)-1]
        