# -*- coding: utf-8 -*-
# 最简单直接的思路
class Solution1(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        
        lst = []
        for i in range(0,num+1):
            s = 0
            for j in bin(i).split('b')[1]:
                if j=='1':
                    s+= 1
            lst.append(s)
        return lst
    
# 找到一个答案的O(N)
'''
f(n) = f(n/2) + 0, 如果n为偶数
f(n) = f(n/2) + 1, 如果n为奇数
'''
class Solution:
    def countBits(self, num):
        res = [0 for _ in range(num+1)]
        for i in range(1, num + 1):
            if i & 1:##位运算判定奇偶加快速度
                res[i]  = res[i//2] + 1
            else:
                res[i]  = res[i//2]
        return res
    
s = Solution()
print(s.countBits(5))