# -*- coding: utf-8 -*-
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)<=1:
            return [nums]
        elif len(nums)==2:
            return [nums, nums[::-1]]
        else:
            pass
        
        final_out = []
        for i in range(len(nums)):
            e = nums[i]
            left_lst = nums[:i]+nums[(i+1):]
            out_lst = [[e]+lst for lst in self.permute(left_lst)]
            final_out += out_lst
        return final_out
        
s = Solution()
print(s.permute([1,2,3]))