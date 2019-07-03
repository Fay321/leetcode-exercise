# -*- coding: utf-8 -*-
'''
想到了合适的递推式
https://leetcode.com/problems/unique-binary-search-trees/
'''

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        #递推的思路
        dp = dict()  #为n时有几棵不同BST
        dp[0] = 1 #为了方便计算引入这个1
        dp[1] = 1
        dp[2] = 2  
        
        if 1<=n<=2:
            return dp[n]
        
        for j in range(3, n+1):
            dp[j] = 0
            for k in range(1,j+1):
                dp[j] += 1*dp[k-1]*dp[j-k]
        return dp[n]