# -*- coding: utf-8 -*-


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        
        ''' 思路：先上下翻转，再沿着对角线进行翻转'''
        row_num = len(matrix)
        
        #上下翻转
        for row_id in range(row_num//2):
            matrix[row_id], matrix[row_num-row_id-1] = matrix[row_num-row_id-1], matrix[row_id] 
        
        #沿着对角线翻转
        for row_id in range(row_num):
            for col_id in range(0,row_id):
                matrix[row_id][col_id], matrix[col_id][row_id] = matrix[col_id][row_id], matrix[row_id][col_id]

        
s = Solution()
print(s.rotate([
  [1,2,3],
  [4,5,6],
  [7,8,9]
]))