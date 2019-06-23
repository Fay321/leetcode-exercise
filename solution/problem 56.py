class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums==[]:  #边界条件
            return [-1,-1]
        start = len(nums)
        end = 0
        for i,v in enumerate(nums):
            if v==target:
                start = min(i,start)
                end = max(i,start)
        
        if end<start:
            return [-1,-1]
        else:
            return [start,end]
    
s = Solution()
print(s.searchRange(nums = [5,7,7,8,8,10], target = 6))
            
                