# -*- coding: utf-8 -*-
from itertools import product


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        out_lst = []
        for selection in product([0,1],repeat=len(nums)):
            one_lst = []
            for i  in range(len(nums)):
                if selection[i]==1:
                    one_lst.append(nums[i])
            out_lst.append(one_lst)
        return out_lst
    
    
s= Solution()
print(s.subsets([1,2,3]))
                    