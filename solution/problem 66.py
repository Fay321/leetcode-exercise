# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/minimum-path-sum/
"""

class Solution1(object):
    '''尝试用动态规划
        反思：不要用太多其他额外操作，这样耗时
    '''
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        #dp[(i,j)] 从起点到(i,j)位置最小路径
        dp = dict()
        q = []
        q.append( (0,0) )  #这些点的坐标往右边、下面走
        dp[(0,0)] = grid[0][0]
        
        i_max = len(grid)
        j_max = len(grid[0])
        
        while q:
                loc = q.pop()
                i,j  = loc
                
                #往右边走
                if i+1 <i_max:
                    if (i+1,j) not in dp:
                        dp[(i+1,j)] = dp[(i,j)]+grid[i+1][j]
                    else:
                        dp[(i+1,j)]  = min( dp[(i,j)]+grid[i+1][j],   dp[(i+1,j)] )
                    q.append((i+1,j))
                        
                #往下走
                if j+1 < j_max:
                    if (i,j+1) not in dp:
                        dp[(i,j+1)] = dp[(i,j)]+grid[i][j+1]
                    else:
                        dp[(i,j+1)] = min(dp[i,j+1],  dp[(i,j)]+grid[i][j+1])
                    q.append((i,j+1))
        #print(dp)      
        return dp[(i_max-1,j_max-1)]



class Solution:
    '''思路就是动态规划 '''
    def minPathSum(self, grid):
        m = len(grid); n = len(grid[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1, n):
            dp[0][i] = dp[0][i-1] + grid[0][i]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[m-1][n-1]
        