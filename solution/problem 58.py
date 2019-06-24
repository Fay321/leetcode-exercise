# -*- coding: utf-8 -*-
class Solution(object):
    ''' O(N) 
    将所有数都加入集合中，然后再遍历这些数，因为我们能O(1)的判断某个数是否在集合中，所以我们可以一个个向上或者向下检查。为了避免之后重复检查，我们每查到一个数，都要将其从集合中移除。这样每遇到一个数，都检查它的上下边界，就能找出最长的连续数列。
    https://segmentfault.com/a/1190000003812046
    '''
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        
        nums_set = set(nums)
        max_length = 0
        
        while True:
            if nums_set==set():
                break
            
            a = nums_set.pop()
            length = 1
            l = 1  #往左边找
            r = 1  #往右边找
            
            while True:
                if a+r in nums_set:
                    length += 1
                    nums_set.remove(a+r)
                    r+=1
                else:
                    break
            
            while True:
                if a-l in nums_set:
                    length+=1
                    nums_set.remove(a-l)
                    l += 1
                else:
                    break
            
            max_length = max(max_length,length)
        return max_length
                    
                    
                
            
        
        
        


class Solution1(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #先想个NlogN复杂度的
        final_max = 0
        prev = 0
        for j,v in enumerate(sorted(nums)):
            if j==0:
                prev = v
                max_l = 1
            else:
                if v-prev==1:
                    max_l += 1

                elif v-prev==0:  #忘了考虑到相等的情况[1,2,0,1]，期待输出为3
                    pass
                else:
                    max_l = 1
                
                prev = v
            final_max = max(final_max,max_l)
        return final_max
    
s = Solution()
print(s.longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6]))