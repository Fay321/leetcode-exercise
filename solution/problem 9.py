# -*- coding: utf-8 -*-

# find-all-numbers-disappeared-in-an-array
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        one_set = set([i for i in range(1,n+1)])
        one_set = one_set - set(nums)
        return list(one_set)