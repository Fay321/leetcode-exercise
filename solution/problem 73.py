# -*- coding: utf-8 -*-
'''主要需要画坐标轴，把几种情况想清楚，这样好确定怎样的情况下更新left_index,
怎样情况更新right_index

后续：https://segmentfault.com/a/1190000004288601
'''

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums==[]: #可能边界
            return -1
        
        a = nums[0]
        b = nums[-1]
        if b<target<a:
            return -1
        if a==target:
            return 0
        elif b==target:
            return len(nums)-1
        
    
        left_index = 0
        right_index = len(nums) #左闭右开
        while left_index<right_index:
    
            m_index = (left_index+right_index)//2
            
            m = nums[m_index]
            if m==target:
                return m_index
            
            if m<=b:
                if m<target<b:
                    left_index = m_index+1
                else: 
                    right_index = m_index
            if m>=a:
                if a<target<m:
                    right_index = m_index
                else:
                    left_index = m_index+1
        return -1