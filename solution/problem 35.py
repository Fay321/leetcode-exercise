# -*- coding: utf-8 -*-
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left_product =  dict()   #nums[0]*   *nums[i-1]
        right_product = dict()   #nums[i+1]*    *nums[end]
        
        for i in range(len(nums)):
            if i ==0:
                left_product[i] = 1
            else:
                left_product[i] = left_product[i-1]*nums[i-1]
        
        for j in range(len(nums)-1,-1,-1):
            if j ==len(nums)-1:
                right_product[j] = 1
            else:
                right_product[j] = right_product[j+1]*nums[j+1]
        
        
        out_lst =[]
        for k in range(len(nums)):
            value = left_product[k]*right_product[k]
            out_lst.append(value)
        return out_lst