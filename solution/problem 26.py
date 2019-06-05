# -*- coding: utf-8 -*-

from scipy.special import comb

class Solution1(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        
        m = n//2
        count = 1
        for i in range(1, m+1):
            M = i + (n-2*i)
            count += comb(M,i)
        return int(count)

class Solution:
    '''用动态规划  表示到第i步梯子在内共有多少种走法 '''
    def climbStairs(self, n):
        steps = [1,1]
        for i in range(2,n+1):
            steps.append(steps[i-1] + steps[i-2])
        return steps[n]    
    
s = Solution()
print(s.climbStairs(4))