# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 16:56:41 2019

@author: fay
"""

class Solution(object):
    '''超时'''
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # dp[(i,j)] 从i到j（左闭右闭）的左括号、右括号个数.(如果右括号比左括号多了，则说明这个子串后面再怎么添加都不会是有效的了)
        dp = dict()
        max_len = 0
        n = len(s)
        
        #初始化
        for i in range(n):
            e = s[i]
            if e=='(':
                dp[(i,i)] = 1,0
            else:
                dp[(i,i)] = 0,1
                
        
        for j in range(1,n):
            for i in range(0,j):
                e = s[j]
                if e==')':
                    dp[(i,j)] = dp[(i,j-1)][0], dp[(i,j-1)][1]+1
                    
                    if dp[(i,j)][1]>dp[(i,j)][0]:
                        dp[(i,j)] = dp[(i,j)][0], float('inf')
    
                    if s[i]=='(' and dp[(i,j)][0]==dp[(i,j)][1]:
                        max_len = max(max_len, j-i+1)
                    
                else:
                    dp[(i,j)] = dp[(i,j-1)][0]+1, dp[(i,j-1)][1]
              
        return max_len
    
    
class Solution(object):
    '''ref:https://blog.csdn.net/XX_123_1_RJ/article/details/80973518'''
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [-1]  #初始位置放个-1
        max_len = 0
        for i,e in enumerate(s):
            if e=='(':
                stack.append(i)
            else:
                j = stack.pop()
                    
                if stack==[]:
                    stack.append(i)
                else:
                    max_len = max(max_len, i-stack[-1])
        return max_len