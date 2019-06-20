# -*- coding: utf-8 -*-
from itertools import product
from collections import Counter

class Solution1(object):
    ''' 用dp[i][j]记录了到算到nums[i]，值为j的个数 '''
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        
        #lst[i]= sum(nums[i+1:])，这个是用来确认计算到第i个位置的上下界的（也就是如果超过这个范围，则说明这个数不用再继续处理下去）
        lst = [0]
        upper_bound = 0
        for j in range(len(nums)-1,0,-1):
            upper_bound += nums[j]
            lst.append(upper_bound)
        lst = lst[::-1]
        
       
        dic = dict()  #到第j个位置 {到这个位置数值为i：多少次}
        for j,value in enumerate(nums):
            dic[j] = Counter()
            if j==0:
                for s in [value,-value]:
                    dic[j][s] += 1
            else:
                
                for s0,pos_neg in product(dic[j-1].keys(),[1,-1]):
                    s = s0+value*pos_neg
                    if s>S+lst[j-1] or s<S-lst[j-1]:
                        pass
                    else:
                        dic[j][s] +=  dic[j-1][s0]
                        
        count = 0
        for e,e_n in dic[len(nums)-1].items():
            if e==S:
                count+=e_n
        return count
    
s = Solution1()
print(s.findTargetSumWays([1,1,1,1,1],3))