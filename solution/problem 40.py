# -*- coding: utf-8 -*-
'''最开始想的是挨着算两两柱子形成的容器容量。但这个会超时。
核心点在于：用最左、最右两个柱子作为开端；而两个柱子中最低的那个限制了容量，所以要想
宽度减少而容量增加只可能是高度变高，所以把两个柱子中较低的那个指针往中间移动
'''

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height)<=1:
            return 0  
        
        l = 0
        r = len(height)-1
        left_h = height[l]
        right_h = height[r]
        max_value = (r-l)*min(left_h,right_h)
        while True:
            if left_h<=right_h:
                l += 1
            else:
                r -= 1
            
            if l>=r:
                break
            
            left_h = height[l]
            right_h = height[r] 
            value = (r-l)*min(left_h,right_h)
            if value>max_value:
                max_value = value
        return max_value
        