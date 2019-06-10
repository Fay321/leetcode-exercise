# -*- coding: utf-8 -*-

class Solution1(object):
    '''对每一行判断是否有target值'''
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for row_id in range(len(matrix)):
            l = 0
            r = len(matrix[row_id])-1
            while l<=r:
                if matrix[row_id][l]>target:
                    break
                elif matrix[row_id][l]==target:
                    return True
                else:
                    l += 1

                if matrix[row_id][r] == target:
                    return True
                elif matrix[row_id][r]<target:
                    break
                else:
                    r -= 1
        return False
    
    
class Solution(object):
    '''更快的一个思路：从右上角开始查找 '''
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        #观察数据后，从右上角开始查找
        if len(matrix)==0:
            return False
        
        col = len(matrix[0])-1
        row = 0
        while row<len(matrix) and col>=0:
            v = matrix[row][col]
            if v==target:
                return True
            elif v<target:
                row += 1
            else:
                col -=1
        return False