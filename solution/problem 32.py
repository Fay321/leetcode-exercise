# -*- coding: utf-8 -*-
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height)<=2:
            return 0
        
        dic = dict()  #第几个位置：（这个格子本身高度,左侧最大值，右侧最大值）  积水高度就是max(min(左侧最大值，右侧最大值)-这个格子本身高度, 0 )
          
        for i in range(len(height)):
            dic[i] = [height[i]]
        
        for i in range(len(height)):
            if i==0:
                dic[i].append(0)
            else:
                dic[i].append(max(dic[i-1][1],height[i-1]))
        
        for i in range(len(height)-1,0,-1):
            if i==len(height)-1:
                dic[i].append(0)
            else:
                dic[i].append(max(dic[i+1][2],height[i+1]))
        
        num = 0
        for i in range(1,len(height)-1):
            num += max(min(dic[i][1],dic[i][2])-dic[i][0], 0)
        return num
        
       
        
'''看了解答https://leetcode.com/problems/trapping-rain-water/discuss/17554/Share-my-one-pass-Python-solution-with-explaination
后，发现自己没注意到的一个点在于：
左侧最大值递增，右侧最大值递减
'''

s = Solution()
print(s.trap( [0,1,0,2,1,0,1,3,2,1,2,1]))
        
        
        
        
            
