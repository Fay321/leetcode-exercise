# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/edit-distance/

ref: https://blog.csdn.net/xygy8860/article/details/46929835
"""

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        
        dp = dict()  #[i,j] 长度为i到长度为j的字符转化
        #初始化
        for j in range(0,n+1):
            dp[(0,j)] = j
        for i in range(0,m+1):
            dp[(i,0)] = i
            
        #递推
        for i in range(1,m+1): 
            for j in range(1,n+1):
                if word1[i-1]==word2[j-1]:
                    dp[(i,j)] = dp[(i-1,j-1)]
                else:
                    dp[(i,j)] = min( dp[(i,j-1)]+1,
                                    dp[(i-1,j)]+1,
                                    dp[(i-1,j-1)]+1)
        return dp[(m,n)]