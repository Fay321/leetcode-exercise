# -*- coding: utf-8 -*-


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        
        for i in range(len(nums)):
            e = nums[i]
            if e==0 or i==0:  #这个位置就不左移，如果e非零，再看左侧的是否有0。这个效率低，其实应该想从左往右移更好些
                pass
            else:
                for j in range(i-1,-1,-1):
                    if nums[j]==0 and (nums[j-1]!=0 or j==0):
                        nums[i], nums[j] = nums[j], nums[i]  
                   

        
s = Solution()
s.moveZeroes([0,1,0,3,12])
        