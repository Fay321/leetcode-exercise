# -*- coding: utf-8 -*-


# ver 1(4760 ms, 11.7 MB)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] ==target:
                    return [i,j]


# ver2 (1868 ms	12.2 MB)
class Solution2(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            a = nums[i]
            b = target - a
            if b in set(nums):  
                for j in range(i+1,len(nums)):
                    if nums[j] == b:
                        return [i,j]      