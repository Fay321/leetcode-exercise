# -*- coding: utf-8 -*-
from copy import deepcopy
class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        bottom_line = []
        right_line = []
        for one_row in grid:
            right_line.append(max(one_row))
            
            if bottom_line ==[]:
                bottom_line = deepcopy(one_row)  #注意这里要用deepcopy，否则会改变grid
            else:
                for j in range(len(one_row)):
                    bottom_line[j] = max(bottom_line[j],one_row[j])
       
        out = 0
        new_grid = deepcopy(grid)
        for row_id in range(len(grid)):
            for column_id in range(len(grid[row_id])):
                value =  max( min(bottom_line[column_id], right_line[row_id])- grid[row_id][column_id],0)
                new_grid[row_id][column_id] = max( min(bottom_line[column_id], right_line[row_id]), grid[row_id][column_id])
                out += value
        return out

if __name__=='__main__':        
    grid = [ [3, 0, 8, 4], 
      [2, 4, 5, 7],
      [9, 2, 6, 3],
      [0, 3, 1, 0] ]
    a=Solution()
    print(a.maxIncreaseKeepingSkyline(grid))