# -*- coding: utf-8 -*-

class Solution1(object):
    '''虽然过了leetcode，但是太耗时了（然后查看了leetcode solution，
    和Dynamic Programming的solution思路就是一样的'''
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = dict(zip(range(len(nums)),[1]*len(nums)))  #到第i个位置(包括整个位置）：最长子序列长度
        
        if len(nums)<=1:
            return len(nums)
        
        max_len = 1
        for i in range(1,len(nums)):
            for j in range(0,i):
                if nums[i]>nums[j]:
                    d[i] = max(d[i],d[j]+1)
                    max_len = max(max_len, d[i])
        return max_len
        
class Solution:
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        
        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
                    
        return max(dp)


s = Solution()
print(s.lengthOfLIS([1,3,6,7,9,4,10,5,6]))