# -*- coding: utf-8 -*-
"""
dynamic programing.  以当前点(x,y) = '1' 为右下角的最大正方形的边长

f(x,y) = min( f(x-1,y), f(x,y-1), f(x-1,y-1)) + 1.

"""

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix==[]:
            return 0
        
        dp = dict()  #记录(i,j)位置为右下角的正方形最大边长
        max_area  = 0
        nrow = len(matrix)
        ncol = len(matrix[0])
        
        for i in range(nrow):
            for j in range(ncol):
                dp[(i,j)] = 0
                
                if i==0:
                    e = matrix[0][j]
                    if e=='1':
                        dp[(0,j)] = 1
                        max_area = 1
                
                if j==0:
                    e = matrix[i][0]
                    if e=='1':
                        dp[(i,0)] =1 
                        max_area = 1
        
        
        # 递推
        for i in range(1, nrow):
            for j in range(1, ncol):
                e = matrix[i][j]
                if e=='1':
                    dp[(i,j)] = min(dp[(i-1,j-1)], dp[(i-1,j)], dp[(i,j-1)]) + 1
                    max_area = max(max_area, dp[(i,j)]**2)
        #print(dp)
        return max_area
                
        