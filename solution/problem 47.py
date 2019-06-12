# -*- coding: utf-8 -*-
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        #忘了考虑边界条件了
        if nums==[]:
            return []
        
        
        out_lst = []
        max_loc = None  #记录这个窗口中最大值所处位置，及最大值
        max_value = None
        for i in range(len(nums)-k+1):
            window_start = i
            window_end = window_start + k #左闭右开
            
            if max_value==None:
                max_value = nums[window_start]
                max_loc = window_start
                for j in range(window_start+1,window_end):
                    e = nums[j]
                    if e>=max_value:
                        max_value = e
                        max_loc = j
                out_lst.append(max_value)
            else:
                if nums[window_end-1]>=max_value:
                    max_value = nums[window_end-1]
                    max_loc = window_end-1
                elif nums[window_end-1]<max_value and window_end-max_loc<=k:
                    pass #这种情况max_value也不变
                elif nums[window_end-1]<max_value and window_end-max_loc>k:
                    #更新max_value
                    max_value= nums[window_start]
                    max_loc = window_start
                    for j in range(window_start+1, window_end):
                        e = nums[j]
                        if e>=max_value:
                            max_value = e
                            max_loc = j
                else:
                    raise
                out_lst.append(max_value)
        return out_lst