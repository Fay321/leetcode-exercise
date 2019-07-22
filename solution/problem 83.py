# -*- coding: utf-8 -*-
import numpy as np
from copy import deepcopy

class Solution1(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        nrow = len(board)
        ncol = len(board[0])
        
        for i in range(nrow):
            for j in range(ncol):
                e = board[i][j]
                if e==word[0]:
                    loc_array = np.zeros((nrow, ncol))
                    loc_array[i][j] = 1
                    
                    if self.one_start((i,j),loc_array, board, word[1:]):
                        return True
        return False
    
    
    def one_start(self, start_loc, loc_array, board, word_left):
        '''给定了要找的位置 (start_loc)，查看loc_array看可以往垂直还是水平方向找，
        word_left就是剩下要找的'''
        if word_left=='':
            return True
        
        
        row, col = start_loc
        nrow = len(board)
        ncol = len(board[0])
        loc_array[(row,col)] = 1
      
        #判断上下左右哪个值等于word_left[0]
        if col+1 < ncol and board[row][col+1]==word_left[0] and loc_array[row][col+1]!=1:
            if self.one_start((row,col+1), deepcopy(loc_array), board, word_left[1:]):  #debug: deepcopy() 这样在前面修改了loc_array不会影响到后面的
                return True
        if col-1>=0 and board[row][col-1]==word_left[0] and loc_array[row][col-1]!=1:
            if self.one_start((row,col-1), deepcopy(loc_array), board, word_left[1:]):
                return True
               
        if row+1<nrow and board[row+1][col] == word_left[0] and loc_array[row+1][col] !=1:
            if self.one_start((row+1,col), deepcopy(loc_array), board, word_left[1:]):
                return True
                
        if row-1>=0 and board[row-1][col] ==word_left[0] and loc_array[row-1][col]!=1:
            if self.one_start((row-1,col), deepcopy(loc_array), board, word_left[1:]):
                return True
      
        return False
        
class Solution(object):
    '''https://www.jianshu.com/p/1625480b71f3'''
    def __init__(self):
        self.word = ""
        
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.word = word
        for row_num in range(len(board)):
            for col_num in range(len(board[0])):
                if self.search(board, row_num, col_num, 0):
                    return True
                
        return False
        
    def search(self, board, x, y, pos):
        if self.word[pos] == board[x][y]:
            if pos == len(self.word) - 1: #pos表示这是看的word[pos]位置
                return True
            else:
                temp = board[x][y]
                board[x][y] = None
                if x + 1 < len(board) and self.search(board, x + 1, y, pos + 1):
                    return True
                if x - 1 >= 0 and self.search(board, x - 1, y, pos + 1):
                    return True
                if y + 1 < len(board[0]) and self.search(board, x, y + 1, pos + 1):
                    return True
                if y - 1 >= 0 and self.search(board, x, y - 1, pos + 1):
                    return True
                board[x][y] = temp  #这里是恢复board[x][y]位置的值
                return False
        else:
            return False        


s = Solution1()
print(s.exist(board =[
        ["A","B","C","E"],
        ["S","F","E","S"],
        ["A","D","E","E"]],
word = "ABCESEEEFS"))   #遇到这种S到E既可以左边，也可以右边的情况了
