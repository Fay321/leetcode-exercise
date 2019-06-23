# -*- coding: utf-8 -*-
class Solution(object):
    ''' 遍历数组，剩余步数step不为零的前提下，每次向前移动一步，将当前的num[i]和step相比较取较大者，作为剩余步数step。
    https://blog.csdn.net/yangjingjing9/article/details/76209758'''
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)==1:
            return True
        
        steps = nums[0]  #能够往前再走多少步
        start = 0 
        
        
        while steps!=0:
            start += 1
            steps -= 1
            if start+steps>=len(nums)-1:
                return True
            steps =  max(nums[start], steps)
        return False
        
        
        




class Solution1(object):
    ''' 超时 '''
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        visited = set()   #已经走过的点
        candidate_set = set()  #待检查的点
    

        visited.add(0)  #初始状态
        for c in range(1,nums[0]+1):
            if c <len(nums):
                candidate_set.add(c)
            

        #然后一步步从candidate_set中往后面跳
        while True:
            if candidate_set==set():
                break
            else:
                c = candidate_set.pop()
          
            if c not in visited:
                visited.add(c)
            else:
                continue
            
            for m in range(1,nums[c]+1):
                if m+c<len(nums):
                    candidate_set.add(m+c)
            
            if len(nums)-1 in visited:
                return True
        
        return len(nums)-1 in visited
        
        
        
s = Solution()
print(s.canJump( [0]  ))    
