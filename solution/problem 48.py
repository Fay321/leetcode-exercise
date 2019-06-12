# -*- coding: utf-8 -*-
"""
我们遍历矩阵的每一个点，对每个点都尝试进行一次深度优先搜索，如果搜索到1，就继续向它的四周搜索。同时我们每找到一个1，就将其标为0，这样就能把整个岛屿变成0。我们只要记录对矩阵遍历时能进入多少次搜索，就代表有多少个岛屿。
"""

class Solution1(object):
    ''' 1060ms，耗时长 '''
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid==[]:  #需要考虑边界
            return 0
        num = 0
        n =len(grid)
        m = len(grid[0])
        
        while self.check_contain_one(grid):
            start = None
            for i in range(n):
                for j in range(m):
                    if grid[i][j]=='1' and start==None:
                        start = (i,j)  #起始位置
                        grid[i][j] = '0'
                        
                        stack = [start]  #记录和(i,j)相邻的位置
                        while stack:
                            i,j = stack.pop()
                            if i>=1 and grid[i-1][j]=='1':
                                stack.append((i-1,j))
                                grid[i-1][j] = '0'
                            if i+1<n and grid[i+1][j]=='1':
                                stack.append((i+1,j))
                                grid[i+1][j] = '0'
                            if j-1>=0 and grid[i][j-1]=='1':
                                stack.append((i,j-1))
                                grid[i][j-1] = '0'
                            if j+1<m and grid[i][j+1]=='1':
                                stack.append((i,j+1))
                                grid[i][j+1] = '0'
                        num +=1
        return num
                        
    def check_contain_one(self,matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]=='1':
                    return True
        return False
    
#------------- DFS-----------------------------#
class Solution:
    ''' 144ms '''
    def numIslands(self, grid):
        num_islands = 0
    
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == '1':
                    num_islands += 1
                    self.island_dfs(grid, row, column)
        
        return num_islands
    
    def island_dfs(self, grid, row, column):
        min_row, max_row = 0, len(grid) - 1
        min_column, max_column = 0, len(grid[0]) - 1
        
        if (not min_row <= row <= max_row) or (not min_column <= column <= max_column):
            return
        elif grid[row][column] != '1':
            return
        else:
            grid[row][column] = '0'
            self.island_dfs(grid, row-1, column)
            self.island_dfs(grid, row+1, column)
            self.island_dfs(grid, row, column-1)
            self.island_dfs(grid, row, column+1)