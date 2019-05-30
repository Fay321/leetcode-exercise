# -*- coding: utf-8 -*-
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #维护两个数组，到这个数为止（包括这个数），最大的乘积、最小乘积值
        nums_large = []
        nums_small = []
        
        for i in range(len(nums)):
            if i==0: #初始值
                nums_large.append(nums[i])
                nums_small.append(nums[i])
                max_value = nums[i]
            else:
                large_value = max(nums_small[i-1]*nums[i], nums_large[i-1]*nums[i],nums[i])
                small_value = min(nums_small[i-1]*nums[i], nums_large[i-1]*nums[i], nums[i])
                max_value = max(large_value, max_value)
                nums_large.append(large_value)
                nums_small.append(small_value)
        return max_value