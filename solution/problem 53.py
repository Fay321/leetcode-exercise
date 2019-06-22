# -*- coding: utf-8 -*-
''' 这个思路很巧， 看subarray=k是否存在，转为 一个array和为B，如果其子串和为B-k存在，则剩余的那部分子串肯定和为k'''

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        count = {0:1}   #{子串[0:n]和为s:出现的次数}
        num = 0
        sum_value = 0
        for e in nums:
            sum_value += e
            if sum_value-k in count:   #注意先查sum_value-k是否在count中，再更新count：例子# 考虑nums=[0,0,0]这种情况
                num += count[sum_value-k]
            
            
            if sum_value not in count:
                count[sum_value] = 1
            else:
                count[sum_value] += 1
              
        return num



class Solution1(object):
    ''' 超时  (思路有点类似于暴力搜索，用的两层for循环）'''
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        
        dic = dict()  #{到第i位置(包括）：sub_array和为j的个数}
        num = 0
        for j,e in enumerate(nums):
            dic[j] = dict()
            if e==k:
                num +=1
            
            dic[j][e] = 1
            if j==0:
                continue
            for s in dic[j-1]:
                if s!=0:
                    dic[j][s+e] = dic[j-1][s]
                else:
                    dic[j][s+e] += dic[j-1][s]
                
                if s+e==k:
                    num += dic[j-1][s]
            dic.pop(j-1)
        
        return num
        
        
s = Solution()
print(s.subarraySum([0,0,0,0,0,0,0,0,0,0],0))