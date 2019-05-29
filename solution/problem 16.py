# -*- coding: utf-8 -*-
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  #从小到大排序
        
        out_lst = []
        for j in range(len(nums)-2):
            if j>0 and nums[j]==nums[j-1]:  #同样去重数字，降低时间复杂度.这样就不需要后面再去掉重复了
                continue
            c = nums[j]
            target_a_add_b = -c
            
            out_lst += self.find_two_sum_target(nums[j+1:], target_a_add_b)
            
        return out_lst
            
    
    
    def find_two_sum_target(self, lst,target):
        '''把lst中两个元素加起来为target的两个元素找出来，返回
        [[a,b, -(a+b)]]
        '''
        out_lst_part = []
        i = 0
        j = len(lst)-1
        while True:        
            if i>=j:
                break
            
            a = lst[i]
            b = lst[j]
            if a+b == target:
                out_lst_part += [[a,b,-target]]
                i += 1
                
                # 后面增加的，去重 降低时间复杂度的
                while j>i:
                    if lst[j]==lst[j-1]:
                        j -=1
                    else:
                        break
                while i<j:
                    if lst[i]==lst[i-1]:
                        i += 1
                    else:
                        break
                
            elif a+b<target:
                i += 1
            else: #a+b>target
                j -= 1
            
  
        return out_lst_part
            
            
            
            
            
            
            
            
        
        
a = Solution()
       
a.threeSum( [-1,0,1,0])
        
        
        
        
        