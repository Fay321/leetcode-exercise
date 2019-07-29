# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/next-permutation/
next permutation 题意理解:https://blog.csdn.net/qq_29600137/article/details/86628763
"""

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums)<=1:
            return 
        
        index_one = None
        for i in range(len(nums)-1, 0, -1):
            a, b = nums[i-1], nums[i]
            if a<b:  
                index_one = i-1
                break
        
        if index_one==None:
            nums.sort()
            return
        
        v = None
        for j in range(index_one+1, len(nums)):
            c = nums[j]
            if c>a and (v==None or c<v):
                v = c
                index_two = j
        
        #替换index_one, index_two的元素
        nums[index_one], nums[index_two] = nums[index_two], nums[index_one]
        
        #从index_one之后是递增
        for j in range(len(nums)-index_one-1, 0, -1):
            for k in range(len(nums)-1, len(nums)-j, -1):
                if nums[k]<nums[k-1]:
                    nums[k-1],nums[k] = nums[k],nums[k-1]